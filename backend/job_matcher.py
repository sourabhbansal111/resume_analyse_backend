from typing import List, Dict

# Try to import scikit-learn, but make it optional
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

class JobMatcher:
    def __init__(self):
        self.vectorizer = None
        if SKLEARN_AVAILABLE:
            try:
                self.vectorizer = TfidfVectorizer()
            except:
                self.vectorizer = None
    
    def calculate_match_score(self, resume_skills: List[str], job_required_skills: List[str], 
                             job_preferred_skills: List[str] = None) -> Dict:
        """
        Calculate match score between resume skills and job requirements
        
        Args:
            resume_skills: List of skills extracted from resume
            job_required_skills: Required skills for the job
            job_preferred_skills: Preferred skills for the job
            
        Returns:
            Dictionary with match score and analysis
        """
        resume_skills_lower = [s.lower() for s in resume_skills]
        required_skills_lower = [s.lower() for s in job_required_skills]
        preferred_skills_lower = [s.lower() for s in (job_preferred_skills or [])]
        
        # Find matching skills
        matching_required = [s for s in required_skills_lower if s in resume_skills_lower]
        matching_preferred = [s for s in preferred_skills_lower if s in resume_skills_lower]
        
        # Missing skills
        missing_required = [s for s in required_skills_lower if s not in resume_skills_lower]
        missing_preferred = [s for s in preferred_skills_lower if s not in resume_skills_lower]
        
        # Calculate scores
        required_score = len(matching_required) / len(required_skills_lower) * 100 if required_skills_lower else 0
        preferred_score = len(matching_preferred) / len(preferred_skills_lower) * 100 if preferred_skills_lower else 0
        
        # Overall score (70% required, 30% preferred)
        overall_score = (required_score * 0.7) + (preferred_score * 0.3)
        
        # Use TF-IDF for semantic similarity
        semantic_score = self._calculate_semantic_similarity(
            resume_skills, job_required_skills + (job_preferred_skills or [])
        )
        
        # Combine exact match and semantic similarity
        final_score = (overall_score * 0.7) + (semantic_score * 0.3)
        
        return {
            'overall_score': round(final_score, 2),
            'required_score': round(required_score, 2),
            'preferred_score': round(preferred_score, 2),
            'matching_required_skills': matching_required,
            'matching_preferred_skills': matching_preferred,
            'missing_required_skills': missing_required,
            'missing_preferred_skills': missing_preferred,
            'total_required_skills': len(required_skills_lower),
            'total_preferred_skills': len(preferred_skills_lower),
            'matched_required_count': len(matching_required),
            'matched_preferred_count': len(matching_preferred)
        }
    
    def _calculate_semantic_similarity(self, resume_skills: List[str], job_skills: List[str]) -> float:
        """Calculate semantic similarity using TF-IDF (if available) or simple word overlap"""
        if not resume_skills or not job_skills:
            return 0.0
        
        # If scikit-learn is available, use TF-IDF
        if SKLEARN_AVAILABLE and self.vectorizer:
            try:
                # Combine skills into text
                resume_text = ' '.join(resume_skills)
                job_text = ' '.join(job_skills)
                
                # Vectorize
                vectors = self.vectorizer.fit_transform([resume_text, job_text])
                
                # Calculate cosine similarity
                similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
                
                return similarity * 100  # Convert to percentage
            except:
                pass
        
        # Fallback: Simple word overlap similarity
        resume_words = set(word.lower() for skill in resume_skills for word in skill.split())
        job_words = set(word.lower() for skill in job_skills for word in skill.split())
        
        if not job_words:
            return 0.0
        
        intersection = resume_words & job_words
        union = resume_words | job_words
        
        if not union:
            return 0.0
        
        # Jaccard similarity
        similarity = len(intersection) / len(union) if union else 0.0
        return similarity * 100
    
    def match_with_all_jobs(self, resume_skills: List[str], jobs: List[Dict]) -> List[Dict]:
        """
        Match resume with all available jobs
        
        Args:
            resume_skills: Skills extracted from resume
            jobs: List of job dictionaries
            
        Returns:
            List of matched jobs with scores, sorted by score
        """
        matches = []
        
        for job in jobs:
            match_result = self.calculate_match_score(
                resume_skills,
                job.get('required_skills', []),
                job.get('preferred_skills', [])
            )
            
            matches.append({
                'job_id': job['id'],
                'company_id': job.get('company_id'),
                'company_name': job.get('company_name', 'Unknown Company'),
                'company_logo': job.get('company_logo'),
                'company_website': job.get('company_website'),
                'job_title': job['title'],
                'job_description': job.get('description', ''),
                'experience_level': job.get('experience_level', ''),
                'location': job.get('location'),
                'salary_range': job.get('salary_range'),
                'match_score': match_result['overall_score'],
                'required_score': match_result['required_score'],
                'preferred_score': match_result['preferred_score'],
                'matching_required_skills': match_result['matching_required_skills'],
                'matching_preferred_skills': match_result['matching_preferred_skills'],
                'missing_required_skills': match_result['missing_required_skills'],
                'missing_preferred_skills': match_result['missing_preferred_skills'],
                'total_required_skills': match_result['total_required_skills'],
                'total_preferred_skills': match_result['total_preferred_skills'],
                'matched_required_count': match_result['matched_required_count'],
                'matched_preferred_count': match_result['matched_preferred_count']
            })
        
        # Sort by match score (descending)
        matches.sort(key=lambda x: x['match_score'], reverse=True)
        
        return matches
    
    def generate_improvement_tips(self, missing_skills: List[str], job_title: str) -> List[str]:
        """Generate improvement tips based on missing skills"""
        tips = []
        
        if not missing_skills:
            tips.append("Great! You have all the required skills for this position.")
            return tips
        
        tips.append(f"To improve your match for {job_title}, consider learning or highlighting:")
        
        # Categorize missing skills

        # =========================
        # Programming Languages
        # =========================
        programming_langs = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'python','java','javascript','typescript','c++','c#',' c ',
                'go','rust','kotlin','swift','php','ruby','scala','perl',
                'shell','bash','powershell','matlab',' r '
            ])
        ]

        # =========================
        # Core Computer Science
        # =========================
        core_cs = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'data structures','algorithms','oop','oops',
                'object oriented programming',
                'design patterns','system design',
                'operating systems','computer networks','dbms',
                'multithreading','concurrency','memory management'
            ])
        ]

        # =========================
        # Web Fundamentals
        # =========================
        web_fundamentals = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'html','css','sass','bootstrap','tailwind',
                'responsive design','cross browser'
            ])
        ]

        # =========================
        # Frontend Frameworks
        # =========================
        frontend = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'react','redux','next.js',
                'angular','vue','nuxt',
                'vite','webpack'
            ])
        ]

        # =========================
        # Backend & APIs
        # =========================
        backend = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'node.js','express','nestjs',
                'django','django rest','flask','fastapi',
                'spring','spring boot',
                'asp.net','laravel','rails',
                'rest api','graphql','grpc',
                'web sockets','api development',
                'authentication','authorization',
                'jwt','oauth','session management'
            ])
        ]

        # =========================
        # Databases
        # =========================
        databases = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'sql','mysql','postgresql','sqlite','oracle',
                'mongodb','redis','dynamodb','cassandra',
                'elasticsearch','neo4j','pl/sql'
            ])
        ]

        # =========================
        # Cloud & DevOps
        # =========================
        cloud_devops = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'aws','azure','gcp','cloud',
                'ec2','s3','rds','lambda','cloud functions',
                'docker','kubernetes',
                'ci/cd','jenkins','github actions',
                'terraform','ansible',
                'linux','unix',
                'nginx','apache',
                'load balancing','auto scaling'
            ])
        ]

        # =========================
        # Monitoring & Logging
        # =========================
        monitoring_logging = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'monitoring','prometheus','grafana',
                'elk','log monitoring'
            ])
        ]

        # =========================
        # Testing & QA
        # =========================
        testing = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'unit testing','integration testing',
                'pytest','junit','jest','mocha',
                'selenium','cypress',
                'tdd','bdd','test driven'
            ])
        ]

        # =========================
        # Data Science & Analytics
        # =========================
        data_science = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'data analysis','data preprocessing',
                'feature engineering','data modeling',
                'pandas','numpy','matplotlib','seaborn',
                'jupyter','etl','statistics'
            ])
        ]

        # =========================
        # Machine Learning & AI
        # =========================
        ml_ai = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'machine learning','deep learning',
                'supervised learning','unsupervised learning',
                'neural networks',
                'tensorflow','pytorch','keras','scikit-learn',
                'nlp','natural language processing',
                'computer vision','opencv',
                'transformers','hugging face',
                'llms','chatbots',
                'recommendation systems',
                'model evaluation','model deployment',
                'mlops','cuda'
            ])
        ]

        # =========================
        # Mobile Development
        # =========================
        mobile = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'android','ios','react native','flutter','xamarin','xcode'
            ])
        ]

        # =========================
        # Security
        # =========================
        security = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'security','web security','cloud security',
                'owasp','xss','csrf','sql injection',
                'encryption','hashing'
            ])
        ]

        # =========================
        # Tools & Collaboration
        # =========================
        tools = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'git','github','gitlab',
                'jira','confluence',
                'code review','pull requests'
            ])
        ]

        # =========================
        # Software Methodologies & Architecture
        # =========================
        methodologies = [
            s for s in missing_skills
            if any(k in s.lower() for k in [
                'agile','scrum','kanban',
                'microservices',
                'monolithic',
                'serverless',
                'distributed systems',
                'performance tuning'
            ])
        ]

        softskill = [
            s for s in missing_skills
            if any(tool in s.lower() for tool in [
                'communication', 'leadership', 'teamwork',
                'problem solving', 'critical thinking',
                'analytical thinking',
                'project management', 'time management',
                'collaboration', 'adaptability',
                'creativity', 'attention to detail',
                'decision making', 'initiative',
                'ownership', 'conflict resolution',
                'mentorship', 'presentation skills',
                'documentation', 'multitasking'
            ])
        ]
        # ======================
        # Suggestions Formatter
        # ======================
        if programming_langs:
            tips.append(f"• Programming Languages: {', '.join(programming_langs)}")

        if core_cs:
            tips.append(f"• Core CS Concepts: {', '.join(core_cs[:3])}")

        if web_fundamentals:
            tips.append(f"• Web Fundamentals: {', '.join(web_fundamentals[:3])}")

        if frontend:
            tips.append(f"• Frontend Skills: {', '.join(frontend[:3])}")

        if backend:
            tips.append(f"• Backend & APIs: {', '.join(backend[:3])}")

        if databases:
            tips.append(f"• Databases: {', '.join(databases[:3])}")

        if cloud_devops:
            tips.append(f"• Cloud & DevOps: {', '.join(cloud_devops[:3])}")

        if monitoring_logging:
            tips.append(f"• Monitoring & Logging: {', '.join(monitoring_logging[:3])}")

        if testing:
            tips.append(f"• Testing & QA: {', '.join(testing[:3])}")

        if data_science:
            tips.append(f"• Data Science & Analytics: {', '.join(data_science[:3])}")

        if ml_ai:
            tips.append(f"• Machine Learning & AI: {', '.join(ml_ai[:3])}")

        if mobile:
            tips.append(f"• Mobile Development: {', '.join(mobile[:3])}")

        if security:
            tips.append(f"• Security: {', '.join(security[:3])}")

        if tools:
            tips.append(f"• Tools & Collaboration: {', '.join(tools[:3])}")

        if methodologies:
            tips.append(f"• Software Architecture & Practices: {', '.join(methodologies[:3])}")


        if softskill:
            tips.append(f"• Softskill: {', '.join(softskill[:3])}")
        # General tips
        if len(missing_skills) > 5:
            tips.append("• Consider taking online courses or certifications for the missing skills")
            tips.append("• Build projects demonstrating these skills")
            tips.append("• Update your resume to highlight any related experience")
        
        return tips

