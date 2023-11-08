import pandas as pd
import os

# Read the CSV file into a DataFrame
jobs_data = pd.read_csv('job.csv')

# Create a directory to store HTML files if it doesn't exist
if not os.path.exists('job_pages'):
    os.makedirs('job_pages')

# Iterate through each row in the DataFrame and generate HTML
for index, job in jobs_data.iterrows():
    job_id = job['job_ID'] 
    job_title = job.get('designation', 'No Designation')  # Use get() to handle missing 'designation' column
    company = job['name']
    location = job['City'] + ', ' + job['State'] 
    job_description = job['job_details']  # Replace 'job_description' with the column name for the job description

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
            <h2>{location}</h2>
        </header>
        <main>
            <p id="jobDescription">{job_description}</p>
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
