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

        programming_langs = [
            s for s in missing_skills
            if any(lang in s.lower() for lang in [
                'python', 'java', 'javascript', 'typescript', 'c++', 'c#',
                'go', 'rust', 'kotlin', 'swift', 'php', 'ruby', 'scala'
            ])
        ]

        core_cs = [
            s for s in missing_skills
            if any(cs in s.lower() for cs in [
                'data structures', 'algorithms', 'oops', 'object oriented',
                'system design', 'operating systems', 'dbms', 'computer networks'
            ])
        ]

        frontend = [
            s for s in missing_skills
            if any(fe in s.lower() for fe in [
                'html', 'css', 'react', 'angular', 'vue',
                'next.js', 'nuxt.js', 'tailwind', 'bootstrap'
            ])
        ]

        backend = [
            s for s in missing_skills
            if any(be in s.lower() for be in [
                'node', 'express', 'django', 'flask', 'fastapi',
                'spring', 'spring boot', 'asp.net', 'laravel', 'rails'
            ])
        ]

        databases = [
            s for s in missing_skills
            if any(db in s.lower() for db in [
                'sql', 'mysql', 'postgresql', 'mongodb',
                'redis', 'oracle', 'sqlite', 'dynamodb', 'cassandra', 'neo4j'
            ])
        ]

        cloud_devops = [
            s for s in missing_skills
            if any(cd in s.lower() for cd in [
                'aws', 'azure', 'gcp',
                'docker', 'kubernetes',
                'ci/cd', 'jenkins', 'terraform', 'ansible',
                'linux'
            ])
        ]

        testing = [
            s for s in missing_skills
            if any(test in s.lower() for test in [
                'testing', 'pytest', 'junit',
                'selenium', 'cypress', 'tdd', 'bdd'
            ])
        ]

        data_ai = [
            s for s in missing_skills
            if any(ai in s.lower() for ai in [
                'machine learning', 'deep learning', 'nlp',
                'computer vision', 'tensorflow', 'pytorch',
                'scikit', 'pandas', 'numpy', 'mlops', 'llm'
            ])
        ]

        security = [
            s for s in missing_skills
            if any(sec in s.lower() for sec in [
                'security', 'owasp', 'jwt', 'oauth',
                'xss', 'csrf', 'sql injection', 'encryption'
            ])
        ]

        tools = [
            s for s in missing_skills
            if any(tool in s.lower() for tool in [
                'git', 'github', 'gitlab', 'jira', 'confluence'
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

        if frontend:
            tips.append(f"• Frontend Skills: {', '.join(frontend[:3])}")

        if backend:
            tips.append(f"• Backend Frameworks: {', '.join(backend[:3])}")

        if databases:
            tips.append(f"• Databases: {', '.join(databases[:3])}")

        if cloud_devops:
            tips.append(f"• Cloud & DevOps: {', '.join(cloud_devops[:3])}")

        if testing:
            tips.append(f"• Testing & QA: {', '.join(testing[:3])}")

        if data_ai:
            tips.append(f"• Data Science & AI: {', '.join(data_ai[:3])}")

        if security:
            tips.append(f"• Security: {', '.join(security[:3])}")

        if tools:
            tips.append(f"• Tools & Collaboration: {', '.join(tools[:3])}")

        # General tips
        if len(missing_skills) > 5:
            tips.append("• Consider taking online courses or certifications for the missing skills")
            tips.append("• Build projects demonstrating these skills")
            tips.append("• Update your resume to highlight any related experience")
        
        return tips

