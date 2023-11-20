import pandas as pd
import os
import re

def preprocess_text(description):
    description = re.sub(r'About the job', '', description)
    
    pattern = re.compile(r'([a-z])([A-Z])')
    description = pattern.sub(r'\1 \2', description)
    description = re.sub(r'(?<=[a-zA-Z])\.(?=[a-zA-Z])', '. ', description)
    description = re.sub(r'(\d+)-(\d+) years', r'\1 \2 years', description)
    description = re.sub('\s+', ' ', description).strip()
    
    responsibilities_start = description.find('Responsibilities')
    qualifications_start = description.find('Qualifications')
    
    responsibilities = description[responsibilities_start:qualifications_start].replace('Responsibilities', '').strip()
    qualifications = description[qualifications_start:].replace('Qualifications', '').strip()
    
    responsibilities_list = responsibilities.split('.')
    qualifications_list = qualifications.split('.')
    
    responsibilities_list = [item.strip() for item in responsibilities_list if item.strip()]
    qualifications_list = [item.strip() for item in qualifications_list if item.strip()]

    additional_info = description[:responsibilities_start].strip()

    result = f"<br>Additional Information:<br>{additional_info}<br>Responsibilities:" + "\u2022 " + ('<br>\u2022 '.join(responsibilities_list) if responsibilities_list else '') + "<br>Qualifications:" + "\u2022 " + ('<br>\u2022 '.join(qualifications_list) if qualifications_list else '')

    return result

# Read the CSV file into a DataFrame
jobs_data = pd.read_csv('job.csv')

# Create a directory to store HTML files if it doesn't exist
if not os.path.exists('job_pages'):
    os.makedirs('job_pages')

# Iterate through each row in the DataFrame and generate HTML
for index, job in jobs_data.iterrows():
    job_id = job['job_ID'] 
    job_title = job.get('designation', 'you!')
    company = job['name']
    work_type = job['work_type']
    involvement = job['involvement']
    employees_count = job['employees_count']
    total_applicants = job['total_applicants']
    level = job['level']
    location = job['City'] + ', ' + job['State'] 
    job_description = job['job_details']

    # Preprocess the job description using spaCy
    preprocessed_description = preprocess_text(job_description)

    # Generate the HTML content for the job page
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{job_title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>{company} is looking for {job_title}!</h1>
            <h2>{work_type} | {involvement} | {total_applicants} applicants | {level}</h2>
            <h2>{location}</h2>
        </header>
        <main>
            <p id="jobDescription">{preprocessed_description}</p>
        </main>
    </div>
    <script src="script.js"></script>
</body>
</html>
    """

    # Save the HTML content to a file
    file_name = f"job_{job_id}.html"
    with open(f"job_pages/{file_name}", "w", encoding='utf-8') as file:
        file.write(html_content)