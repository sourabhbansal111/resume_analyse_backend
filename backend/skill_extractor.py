import re
from typing import List, Set
from collections import Counter

# Try to import SpaCy, but make it optional
try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False

class SkillExtractor:
    def __init__(self):
        self.nlp = None
        if SPACY_AVAILABLE:
            try:
                self.nlp = spacy.load("en_core_web_sm")
            except (OSError, IOError):
                # SpaCy model not found, continue without it
                self.nlp = None
        
        # Common technical skills database
        self.technical_skills = {

                # =========================
                # Programming Languages
                # =========================
                'python', 'java', 'javascript', 'typescript', 'c++', 'c', 'c#', 'go', 'rust',
                'kotlin', 'swift', 'php', 'ruby', 'scala', 'r', 'matlab', 'perl',
                'shell', 'bash', 'powershell',

                # =========================
                # Core Computer Science
                # =========================
                'data structures', 'algorithms', 'object oriented programming', 'oops','oop',
                'object oriented programming',
                'design patterns', 'system design', 'operating systems',
                'computer networks', 'dbms',
                'multithreading', 'concurrency', 'memory management',

                # =========================
                # Web Fundamentals
                # =========================
                'html', 'css', 'sass', 'bootstrap', 'tailwind css',
                'responsive design', 'cross browser compatibility',

                # =========================
                # Frontend Frameworks
                # =========================
                'react', 'redux', 'next.js',
                'angular', 'vue', 'nuxt.js',
                'vite', 'webpack',

                # =========================
                # Backend Frameworks
                # =========================
                'node.js', 'express', 'nestjs',
                'django', 'django rest framework', 'flask', 'fastapi',
                'spring', 'spring boot',
                'asp.net', 'laravel', 'rails',

                # =========================
                # APIs & Communication
                # =========================
                'rest api', 'graphql', 'grpc',
                'web sockets', 'api development',
                'authentication', 'authorization',
                'jwt', 'oauth', 'session management',

                # =========================
                # Databases (SQL & NoSQL)
                # =========================
                'sql', 'mysql', 'postgresql', 'sqlite', 'oracle',
                'mongodb', 'redis', 'dynamodb', 'cassandra',
                'elasticsearch', 'neo4j',

                # =========================
                # Cloud Platforms
                # =========================
                'aws', 'azure', 'gcp',
                'aws ec2', 'aws s3', 'aws rds', 'aws lambda',
                'cloud functions', 'cloud security',
                'load balancing', 'auto scaling',

                # =========================
                # DevOps & Infrastructure
                # =========================
                'docker', 'kubernetes',
                'ci/cd', 'jenkins', 'github actions',
                'terraform', 'ansible',
                'nginx', 'apache',
                'linux', 'unix',

                # =========================
                # Monitoring & Logging
                # =========================
                'prometheus', 'grafana',
                'elk stack', 'log monitoring',

                # =========================
                # Testing & Quality Assurance
                # =========================
                'unit testing', 'integration testing',
                'pytest', 'junit',
                'jest', 'mocha',
                'selenium', 'cypress',
                'test driven development', 'tdd', 'bdd',

                # =========================
                # Data Science & Analytics
                # =========================
                'data analysis', 'data preprocessing',
                'feature engineering',
                'pandas', 'numpy',
                'matplotlib', 'seaborn',
                'jupyter',

                # =========================
                # Machine Learning & AI
                # =========================
                'machine learning', 'deep learning',
                'supervised learning', 'unsupervised learning',
                'neural networks',
                'tensorflow', 'pytorch', 'keras',
                'scikit-learn',
                'natural language processing', 'nlp',
                'computer vision',
                'transformers', 'hugging face',
                'llms', 'chatbots',
                'recommendation systems',
                'model evaluation', 'model deployment',
                'mlops',

                # =========================
                # Mobile Development
                # =========================
                'android', 'ios',
                'react native', 'flutter', 'xamarin',

                # =========================
                # Security
                # =========================
                'web security', 'owasp',
                'sql injection', 'xss', 'csrf',
                'encryption', 'hashing',

                # =========================
                # Version Control & Tools
                # =========================
                'git', 'github', 'gitlab',
                'git workflows', 'pull requests',
                'code review',
                'jira', 'confluence',

                # =========================
                # Software Methodologies
                # =========================
                'agile', 'scrum', 'kanban',
                'microservices', 'monolithic architecture',
                'serverless architecture'

                'firebase','etl','data modeling',
                'distributed systems','kafka','opencv',
                'cuda','performance tuning','xcode',
                'statistics','cloud','monitoring',
                'security',
            }

            # =========================
            # Soft Skills
            # =========================
        self.soft_skills = {
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
            }

    
    def extract_skills(self, resume_text: str) -> List[str]:
        """
        Extract skills from resume text using NLP
        
        Args:
            resume_text: Text content from resume
            
        Returns:
            List of extracted skills
        """
        skills = set()
        text_lower = resume_text.lower()
        
        # Extract technical skills
        for skill in self.technical_skills:
            skill_lower = skill.lower()
            escaped_skill = re.escape(skill_lower)
        
            # Use \b for normal words, lookarounds for symbol-based skills
            if skill_lower.isalnum():
                pattern = r'\b' + escaped_skill + r'\b'
            else:
                pattern = r'(?<!\w)' + escaped_skill + r'(?!\w)'
        
            if re.search(pattern, text_lower, re.IGNORECASE):
                skills.add(skill)

        
        # Extract soft skills
        for skill in self.soft_skills:
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if re.search(pattern, text_lower, re.IGNORECASE):
                skills.add(skill)
        
        # Look for skills section explicitly
        skills_section = self._find_skills_section(resume_text)
        if skills_section:
            skills.update(self._extract_from_skills_section(skills_section))
        
        # Use NLP to find noun phrases that might be skills (if SpaCy is available)
        if self.nlp:
            try:
                doc = self.nlp(resume_text)
                # Extract technical terms (nouns that are likely technologies)
                for chunk in doc.noun_chunks:
                    chunk_text = chunk.text.lower().strip()
                    if len(chunk_text) > 2 and len(chunk_text) < 30:
                        # Check if it's a known technology or tool
                        if any(tech in chunk_text for tech in ['api', 'framework', 'library', 'tool', 'platform']):
                            skills.add(chunk_text)
            except:
                # If NLP processing fails, continue without it
                pass
        
        return sorted(list(skills))
    
    def _find_skills_section(self, text: str) -> str:
        """Find the skills section in resume"""
        lines = text.split('\n')
        skills_section = ""
        in_skills_section = False
        
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ['skills', 'technical skills', 'competencies', 'proficiencies']):
                in_skills_section = True
                continue
            
            if in_skills_section:
                if line.strip() and not line.strip()[0].isdigit():
                    skills_section += line + " "
                else:
                    break
        
        return skills_section


    def _extract_from_skills_section(self, skills_text: str) -> Set[str]:
        skills = set()

        # Split using ALL delimiters
        parts = re.split(r'[,\n;|\-•]+', skills_text.lower())

        # Sort to make order deterministic
        known_skills = sorted(self.technical_skills | self.soft_skills, key=str.lower)

        for part in parts:
            skill = part.strip()
            if len(skill) <= 2:
                continue

            for known_skill in known_skills:
                if skill == known_skill.lower():
                    skills.add(known_skill)
                    break

        return skills

    
    def normalize_skill(self, skill: str) -> str:
        """Normalize skill name (e.g., 'Python' -> 'python')"""
        return skill.lower().strip()

