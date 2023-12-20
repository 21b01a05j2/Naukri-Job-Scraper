# Naukri-Job-Scraper
Job Data Extraction from Naukri website

This Selenium script is designed for web scraping job information from Naukri.com, a popular job search platform. The script performs the following tasks:

1)Job Search and Filtering:

Opens the Naukri.com website using the Chrome WebDriver.
Searches for jobs with the keyword "Jobs."
Filters jobs based on the following criteria:
Work from office preference.
Job category: Engineering - Software & QA.
Specialization: DBA / Data warehousing.
Education qualification: B.Tech/B.E.
Location: Bengaluru.
Salary ranges: 0-3 Lakhs, 3-6 Lakhs, 6-10 Lakhs, 10-15 Lakhs.

2)Data Extraction:

Extracts information such as job title, company name, experience required, salary, location, and skills from each job listing.
Skills are categorized into specific technologies or tools (Unix, Oracle, Linux, Debugging, XML, MySQL, RDBMS, Java, Python, Adobe), and their presence is marked with "Yes" or "No."

3)Pagination Handling:

Navigates through multiple pages of job listings for each salary range.

4)Data Storage:

Saves the extracted data into a Pandas DataFrame.
If a CSV file (transformed_jobs_data.csv) already exists, it loads the existing data and appends the new data to it.
The final DataFrame is then saved back to the CSV file.

5)Browser Closure:

Closes the Chrome WebDriver after the data extraction and storage processes.
