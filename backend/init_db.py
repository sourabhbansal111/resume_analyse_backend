"""
Initialize database with sample companies and job roles
"""
from database import Database

def init_sample_data():
    """Add sample companies and job roles to the database"""
    db = Database()
    
    # Sample companies
    companies = [
    {'name': 'Microsoft', 'description': 'Enterprise software, cloud, and AI', 'logo_url': '', 'website': 'https://microsoft.com'},
    {'name': 'Google', 'description': 'Search, AI, cloud, and large-scale systems', 'logo_url': '', 'website': 'https://google.com'},
    {'name': 'Meta', 'description': 'Social platforms, AR/VR, AI', 'logo_url': '', 'website': 'https://meta.com'},
    {'name': 'Amazon', 'description': 'E-commerce and cloud computing', 'logo_url': '', 'website': 'https://amazon.com'},
    {'name': 'Apple', 'description': 'Consumer devices and software ecosystem', 'logo_url': '', 'website': 'https://apple.com'},
    {'name': 'Netflix', 'description': 'Streaming and distributed systems', 'logo_url': '', 'website': 'https://netflix.com'},
    {'name': 'Tesla', 'description': 'EVs, robotics, and AI automation', 'logo_url': '', 'website': 'https://tesla.com'},
    {'name': 'Uber', 'description': 'Real-time mobility platforms', 'logo_url': '', 'website': 'https://uber.com'},
    {'name': 'Airbnb', 'description': 'Marketplace and scalable platforms', 'logo_url': '', 'website': 'https://airbnb.com'},
    {'name': 'Spotify', 'description': 'Music streaming and recommendation systems', 'logo_url': '', 'website': 'https://spotify.com'},
    {'name': 'Adobe', 'description': 'Creative software and cloud products', 'logo_url': '', 'website': 'https://adobe.com'},
    {'name': 'Salesforce', 'description': 'CRM and enterprise cloud', 'logo_url': '', 'website': 'https://salesforce.com'},
    {'name': 'IBM', 'description': 'Enterprise AI and research', 'logo_url': '', 'website': 'https://ibm.com'},
    {'name': 'Oracle', 'description': 'Databases and enterprise software', 'logo_url': '', 'website': 'https://oracle.com'},
    {'name': 'NVIDIA', 'description': 'AI computing and GPUs', 'logo_url': '', 'website': 'https://nvidia.com'},
    {'name': 'LinkedIn', 'description': 'Professional networking and data platforms', 'logo_url': '', 'website': 'https://linkedin.com'},
    {'name': 'Stripe', 'description': 'Online payments and APIs', 'logo_url': '', 'website': 'https://stripe.com'},
    {'name': 'Atlassian', 'description': 'Developer productivity tools', 'logo_url': '', 'website': 'https://atlassian.com'},
    {'name': 'Snowflake', 'description': 'Cloud data warehouse', 'logo_url': '', 'website': 'https://snowflake.com'},
    {'name': 'PayPal', 'description': 'Digital payments', 'logo_url': '', 'website': 'https://paypal.com'},
    {'name': 'Intel', 'description': 'Semiconductors and system software', 'logo_url': '', 'website': 'https://intel.com'},
    {'name': 'SAP', 'description': 'Enterprise business software', 'logo_url': '', 'website': 'https://sap.com'},
    { 'name': 'TechCorp', 'description': 'Leading technology company specializing in software solutions', 'logo_url': '', 'website': 'https://techcorp.com' }, 
    { 'name': 'DataFlow Inc', 'description': 'Data analytics and machine learning solutions provider', 'logo_url': '', 'website': 'https://dataflow.com' }, 
    { 'name': 'CloudSystems', 'description': 'Cloud infrastructure and DevOps services', 'logo_url': '', 'website': 'https://cloudsystems.com' }, 
    { 'name': 'WebDev Studio', 'description': 'Full-stack web development agency', 'logo_url': '', 'website': 'https://webdevstudio.com' } 
    ]
    
    # Sample jobs
    jobs = [


            # 1
            {'company_name':'Microsoft','title':'Software Engineer','description':'Design and maintain scalable software systems.','required_skills':['python','java','c++','data structures','algorithms','git'],'preferred_skills':['azure','docker','system design'],'experience_level':'Mid','location':'Redmond, WA','salary_range':'$110k - $140k'},

            # 2
            {'company_name':'Google','title':'Software Engineer II','description':'Build reliable large-scale distributed systems.','required_skills':['python','java','algorithms','system design','git'],'preferred_skills':['gcp','kubernetes','distributed systems'],'experience_level':'Mid','location':'Mountain View, CA','salary_range':'$130k - $160k'},

            # 3
            {'company_name':'Amazon','title':'Software Development Engineer','description':'Develop highly available backend services.','required_skills':['java','data structures','algorithms','sql','git'],'preferred_skills':['aws','microservices','docker'],'experience_level':'Mid','location':'Seattle, WA','salary_range':'$125k - $155k'},

            # 4
            {'company_name':'Meta','title':'Full Stack Engineer','description':'Build end-to-end web applications.','required_skills':['javascript','react','node.js','sql','rest api'],'preferred_skills':['graphql','typescript','docker'],'experience_level':'Mid','location':'Menlo Park, CA','salary_range':'$130k - $160k'},

            # 5
            {'company_name':'Netflix','title':'Backend Engineer','description':'Design backend services for streaming platforms.','required_skills':['java','spring boot','sql','rest api'],'preferred_skills':['microservices','aws','docker'],'experience_level':'Senior','location':'Los Gatos, CA','salary_range':'$150k - $190k'},

            # 6
            {'company_name':'Apple','title':'iOS Engineer','description':'Develop and maintain iOS applications.','required_skills':['swift','ios','xcode'],'preferred_skills':['performance optimization'],'experience_level':'Mid','location':'Cupertino, CA','salary_range':'$135k - $165k'},

            # 7
            {'company_name':'Uber','title':'Android Engineer','description':'Build scalable Android applications.','required_skills':['kotlin','android','rest api'],'preferred_skills':['firebase','graphql'],'experience_level':'Mid','location':'San Francisco, CA','salary_range':'$125k - $155k'},

            # 8
            {'company_name':'Spotify','title':'Frontend Developer','description':'Create responsive UI for music platforms.','required_skills':['react','javascript','html','css'],'preferred_skills':['redux','typescript'],'experience_level':'Mid','location':'Stockholm','salary_range':'$100k - $130k'},

            # 9
            {'company_name':'Adobe','title':'UI Engineer','description':'Build reusable UI components.','required_skills':['javascript','react','css'],'preferred_skills':['accessibility','design systems'],'experience_level':'Mid','location':'San Jose, CA','salary_range':'$115k - $145k'},

            # 10
            {'company_name':'Salesforce','title':'Software Engineer','description':'Develop CRM cloud features.','required_skills':['java','sql','oop','git'],'preferred_skills':['apex','microservices'],'experience_level':'Mid','location':'San Francisco, CA','salary_range':'$120k - $150k'},

            # 11
            {'company_name':'IBM','title':'Backend Developer','description':'Build enterprise backend systems.','required_skills':['java','sql','rest api','linux'],'preferred_skills':['microservices','docker'],'experience_level':'Mid','location':'Austin, TX','salary_range':'$110k - $140k'},

            # 12
            {'company_name':'Oracle','title':'Database Engineer','description':'Manage and optimize database systems.','required_skills':['sql','oracle','performance tuning'],'preferred_skills':['pl/sql','linux'],'experience_level':'Senior','location':'Redwood City, CA','salary_range':'$135k - $165k'},

            # 13
            {'company_name':'NVIDIA','title':'Machine Learning Engineer','description':'Develop ML models for AI platforms.','required_skills':['python','machine learning','deep learning','pytorch'],'preferred_skills':['cuda','computer vision'],'experience_level':'Senior','location':'Santa Clara, CA','salary_range':'$160k - $200k'},

            # 14
            {'company_name':'Tesla','title':'AI Engineer','description':'Build AI systems for autonomous vehicles.','required_skills':['python','deep learning','computer vision'],'preferred_skills':['pytorch','opencv'],'experience_level':'Mid','location':'Palo Alto, CA','salary_range':'$140k - $180k'},

            # 15
            {'company_name':'LinkedIn','title':'Backend Software Engineer','description':'Develop scalable networking services.','required_skills':['java','sql','rest api','data structures'],'preferred_skills':['kafka','microservices'],'experience_level':'Mid','location':'Sunnyvale, CA','salary_range':'$130k - $160k'},

            # 16
            {'company_name':'Stripe','title':'Backend API Engineer','description':'Develop secure payment APIs.','required_skills':['python','rest api','sql','security'],'preferred_skills':['oauth','distributed systems'],'experience_level':'Mid','location':'Remote','salary_range':'$135k - $165k'},

            # 17
            {'company_name':'PayPal','title':'Security Engineer','description':'Ensure security of payment systems.','required_skills':['web security','owasp','linux','networking'],'preferred_skills':['cloud security','aws'],'experience_level':'Senior','location':'San Jose, CA','salary_range':'$135k - $170k'},

            # 18
            {'company_name':'Snowflake','title':'Data Engineer','description':'Build scalable data pipelines.','required_skills':['sql','python','etl','data modeling'],'preferred_skills':['aws','cloud data'],'experience_level':'Mid','location':'San Mateo, CA','salary_range':'$135k - $165k'},

            # 19
            {'company_name':'Atlassian','title':'Full Stack Developer','description':'Build collaboration tools.','required_skills':['react','java','spring','sql'],'preferred_skills':['microservices','aws'],'experience_level':'Mid','location':'Remote','salary_range':'$120k - $150k'},

            # 20
            {'company_name':'SAP','title':'Enterprise Software Engineer','description':'Develop enterprise business software.','required_skills':['java','spring','sql'],'preferred_skills':['microservices'],'experience_level':'Mid','location':'Walldorf, Germany','salary_range':'$100k - $130k'},
            {'company_name':'Google','title':'Cloud Engineer','description':'Manage cloud infrastructure.','required_skills':['gcp','linux','networking','security'],'preferred_skills':['kubernetes','terraform'],'experience_level':'Mid','location':'Remote','salary_range':'$120k - $150k'},
            {'company_name':'Amazon','title':'DevOps Engineer','description':'Automate deployments and infrastructure.','required_skills':['aws','docker','kubernetes','ci/cd','linux'],'preferred_skills':['terraform','monitoring'],'experience_level':'Mid','location':'Austin, TX','salary_range':'$120k - $150k'},
            {'company_name':'Microsoft','title':'Data Engineer','description':'Build data pipelines and analytics systems.','required_skills':['python','sql','etl','data modeling'],'preferred_skills':['azure','spark'],'experience_level':'Mid','location':'Seattle, WA','salary_range':'$115k - $145k'},
            {'company_name':'Meta','title':'Data Scientist','description':'Analyze data and build predictive models.','required_skills':['python','sql','statistics','data analysis'],'preferred_skills':['machine learning','tensorflow'],'experience_level':'Senior','location':'New York, NY','salary_range':'$140k - $170k'},
            {'company_name':'Uber','title':'Site Reliability Engineer','description':'Ensure system reliability.','required_skills':['linux','monitoring','docker','networking'],'preferred_skills':['kubernetes','prometheus'],'experience_level':'Senior','location':'Seattle, WA','salary_range':'$130k - $165k'},
            {'company_name':'Netflix','title':'Platform Engineer','description':'Build internal developer platforms.','required_skills':['java','cloud','docker','kubernetes'],'preferred_skills':['aws','terraform'],'experience_level':'Senior','location':'Los Gatos, CA','salary_range':'$155k - $195k'},
            {'company_name':'Apple','title':'Backend Engineer','description':'Develop backend services for Apple platforms.','required_skills':['java','python','sql','rest api'],'preferred_skills':['microservices'],'experience_level':'Mid','location':'Cupertino, CA','salary_range':'$130k - $160k'},
            {'company_name':'Adobe','title':'Cloud Software Engineer','description':'Build cloud-native services.','required_skills':['java','python','cloud','rest api'],'preferred_skills':['aws','docker'],'experience_level':'Mid','location':'San Jose, CA','salary_range':'$120k - $150k'},
            {'company_name':'Salesforce','title':'Frontend Engineer','description':'Develop UI for CRM products.','required_skills':['javascript','react','html','css'],'preferred_skills':['typescript','redux'],'experience_level':'Mid','location':'San Francisco, CA','salary_range':'$115k - $145k'},
            {'company_name':'IBM','title':'Data Scientist','description':'Apply ML to enterprise problems.','required_skills':['python','machine learning','statistics'],'preferred_skills':['tensorflow','nlp'],'experience_level':'Senior','location':'Boston, MA','salary_range':'$135k - $165k'},


        {
            'company_name': 'TechCorp',
            'title': 'Python Developer',
            'description': 'Develop and maintain Python applications, work with APIs, and collaborate with cross-functional teams.',
            'required_skills': ['python', 'sql', 'git', 'rest api', 'flask', 'django'],
            'preferred_skills': ['docker', 'aws', 'react', 'postgresql', 'mongodb', 'kubernetes'],
            'experience_level': 'Mid',
            'location': 'San Francisco, CA',
            'salary_range': '$90k - $120k'
        },
        {
            'company_name': 'WebDev Studio',
            'title': 'Full Stack Developer',
            'description': 'Build end-to-end web applications using modern frameworks and technologies.',
            'required_skills': ['javascript', 'react', 'node.js', 'html', 'css', 'sql', 'git'],
            'preferred_skills': ['typescript', 'angular', 'vue', 'aws', 'docker', 'mongodb', 'express'],
            'experience_level': 'Mid',
            'location': 'New York, NY',
            'salary_range': '$85k - $115k'
        },
        {
            'company_name': 'DataFlow Inc',
            'title': 'Data Scientist',
            'description': 'Analyze complex data sets, build ML models, and provide data-driven insights.',
            'required_skills': ['python', 'machine learning', 'pandas', 'numpy', 'data analysis', 'sql'],
            'preferred_skills': ['tensorflow', 'pytorch', 'scikit-learn', 'jupyter', 'deep learning', 'nlp'],
            'experience_level': 'Senior',
            'location': 'Seattle, WA',
            'salary_range': '$120k - $150k'
        },
        {
            'company_name': 'CloudSystems',
            'title': 'DevOps Engineer',
            'description': 'Manage infrastructure, automate deployments, and ensure system reliability.',
            'required_skills': ['docker', 'kubernetes', 'aws', 'linux', 'git', 'ci/cd'],
            'preferred_skills': ['jenkins', 'terraform', 'ansible', 'azure', 'gcp', 'monitoring'],
            'experience_level': 'Mid',
            'location': 'Austin, TX',
            'salary_range': '$100k - $130k'
        },
        {
            'company_name': 'WebDev Studio',
            'title': 'Frontend Developer',
            'description': 'Create responsive and interactive user interfaces using modern web technologies.',
            'required_skills': ['javascript', 'react', 'html', 'css', 'git'],
            'preferred_skills': ['typescript', 'angular', 'vue', 'next.js', 'redux', 'webpack'],
            'experience_level': 'Junior',
            'location': 'Remote',
            'salary_range': '$60k - $80k'
        },
        {
            'company_name': 'TechCorp',
            'title': 'Backend Developer',
            'description': 'Design and implement server-side logic, APIs, and database solutions.',
            'required_skills': ['python', 'sql', 'rest api', 'git', 'linux'],
            'preferred_skills': ['java', 'node.js', 'docker', 'aws', 'postgresql', 'mongodb', 'microservices'],
            'experience_level': 'Mid',
            'location': 'Boston, MA',
            'salary_range': '$95k - $125k'
        },
        {
            'company_name': 'DataFlow Inc',
            'title': 'ML Engineer',
            'description': 'Build and deploy machine learning models at scale.',
            'required_skills': ['python', 'machine learning', 'tensorflow', 'pytorch', 'scikit-learn'],
            'preferred_skills': ['deep learning', 'nlp', 'computer vision', 'aws', 'docker', 'kubernetes'],
            'experience_level': 'Senior',
            'location': 'Palo Alto, CA',
            'salary_range': '$130k - $160k'
        },
        {
            'company_name': 'CloudSystems',
            'title': 'Software Engineer',
            'description': 'Design, develop, and maintain software applications.',
            'required_skills': ['python', 'java', 'git', 'sql', 'problem solving'],
            'preferred_skills': ['javascript', 'docker', 'aws', 'agile', 'microservices', 'rest api'],
            'experience_level': 'Mid',
            'location': 'Denver, CO',
            'salary_range': '$90k - $120k'
        }
    ]
    
    print("Initializing database with sample data...")
    
    # Create companies
    company_map = {}
    for company_data in companies:
        company_id = db.add_company(
            name=company_data['name'],
            description=company_data['description'],
            logo_url=company_data['logo_url'],
            website=company_data['website']
        )
        company_map[company_data['name']] = company_id
        print(f"Added company: {company_data['name']} (ID: {company_id})")
    
    # Create jobs
    for job_data in jobs:
        company_id = company_map.get(job_data['company_name'])
        if company_id:
            job_id = db.add_job_role(
                company_id=company_id,
                title=job_data['title'],
                description=job_data['description'],
                required_skills=job_data['required_skills'],
                preferred_skills=job_data['preferred_skills'],
                experience_level=job_data['experience_level'],
                location=job_data.get('location'),
                salary_range=job_data.get('salary_range')
            )
            print(f"Added job: {job_data['title']} at {job_data['company_name']} (ID: {job_id})")
    
    print(f"\nSuccessfully added {len(companies)} companies and {len(jobs)} job roles!")
    print("Database initialization complete.")

if __name__ == '__main__':
    init_sample_data()
