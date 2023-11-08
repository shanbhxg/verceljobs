// JavaScript for formatting the job description

document.addEventListener('DOMContentLoaded', function() {
    // Get the job description element
    const jobDescription = document.getElementById('jobDescription');

    // Split the description into sections based on keywords
    const sections = jobDescription.textContent.split('Skills Required:');

    // Check if the description contains 'Skills Required' and split accordingly
    if (sections.length > 1) {
        const skillsRequiredSection = sections[1].trim();
        const additionalInfoSection = sections[0].trim();

        // Create HTML elements for each section
        const skillsRequiredDiv = document.createElement('div');
        skillsRequiredDiv.innerHTML = `<h3>Skills Required:</h3>${skillsRequiredSection}`;

        const additionalInfoDiv = document.createElement('div');
        additionalInfoDiv.innerHTML = `<h3>Additional Information:</h3>${additionalInfoSection}`;

        // Replace the original description with the formatted sections
        jobDescription.innerHTML = '';
        jobDescription.appendChild(additionalInfoDiv);
        jobDescription.appendChild(skillsRequiredDiv);
    }
});
