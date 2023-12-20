from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import time
import pandas as pd
import os

# Set up the WebDriver
driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")
time.sleep(5)

search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@class='suggestor-input']"))
)

search_bar.send_keys("Jobs")
search_bar.send_keys(Keys.RETURN)

# Adjust wait time if needed
work_from_office = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@title='Work from office']"))
)
work_from_office.click()
time.sleep(4)

software_qa_option = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@title='Engineering - Software & QA']"))
)
software_qa_option.click()
time.sleep(4)

DBA = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@title='DBA / Data warehousing']"))
)
DBA.click()
time.sleep(4)

# List of salary ranges to iterate over
salary_ranges = ['0-3 Lakhs', '3-6 Lakhs', '6-10 Lakhs', '10-15 Lakhs']

# Initialize lists to store data
titles = []
companies = []
experiences = []
salaries = []
locations = []
Unix = []
Oracle = []
Linux = []
Debugging = []
XML = []
MySQL = []
RDBMS = []
Java = []
Python = []
Adobe = []



education = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@title='B.Tech/B.E.']"))
)
education.click()
time.sleep(4)

try:
    company_jobs_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@title='Company Jobs']"))
    )
    company_jobs_option.click()
except:
    pass

time.sleep(4)

try:
    bengaluru_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@title='Bengaluru']"))
    )
    bengaluru_option.click()
except:
    pass

time.sleep(4)

# Iterate through salary ranges
for salary_range in salary_ranges:
    # Add Salary filter
    salary_filter = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[@title='{salary_range}']"))
    )
    salary_filter.click()
    time.sleep(4)

    # Loop through all pages
    while True:
        # Wait for job roles to load
        job_roles = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='srp-jobtuple-wrapper']"))
        )

        # Iterate through job roles and extract data
        for job_role in job_roles:
            # Extracting common information
            title = job_role.find_element(By.XPATH, ".//div[@class=' row1']/a").text

            # Use try-except block to handle NoSuchElementException
            try:
                company = job_role.find_element(By.XPATH, ".//span[@class=' comp-dtls-wrap']/a").text
            except NoSuchElementException:
                company = "Not specified"  # Set a default value or handle it as needed

            experience = job_role.find_element(By.XPATH, ".//span[@class='expwdth']").text

            salary_element = job_role.find_element(By.XPATH, ".//span[@class='ni-job-tuple-icon ni-job-tuple-icon-srp-rupee sal']/span")
            salary_text = salary_element.text.strip() if salary_element else "Not disclosed"
            salary = salary_text if salary_text.lower() != "not disclosed" else f"{salary_range} PA"

            location = job_role.find_element(By.XPATH, ".//span[@class='locWdth']").text

            # Extracting skills
            skills_path = ".//div[@class=' row5']//li[@class='dot-gt tag-li ']"
            skills = job_role.find_elements(By.XPATH, skills_path)

            # Extract skill details and fill with "No" if the skill is not present
            Unix.append("Yes" if any("Unix" in skill.text for skill in skills) else "No")
            Oracle.append("Yes" if any("Data analysis" in skill.text for skill in skills) else "No")
            Linux.append("Yes" if any("Linux" in skill.text for skill in skills) else "No")
            Debugging.append("Yes" if any("Application development" in skill.text for skill in skills) else "No")
            XML.append("Yes" if any("MongoDB" in skill.text for skill in skills) else "No")
            MySQL.append("Yes" if any("Asset management" in skill.text for skill in skills) else "No")
            RDBMS.append("Yes" if any("RDBMS" in skill.text for skill in skills) else "No")
            Java.append("Yes" if any("Java" in skill.text for skill in skills) else "No")
            Python.append("Yes" if any("Python" in skill.text for skill in skills) else "No")
            Adobe.append("Yes" if any("Adobe" in skill.text for skill in skills) else "No")

            # Add data to respective lists
            titles.append(title)
            companies.append(company)
            experiences.append(experience)
            salaries.append(salary)
            locations.append(location)

        try:
            # Go to the next page
            next_page = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='styles_selected__j3uvq']/following-sibling::a"))
            )
            next_page.click()
            time.sleep(5)  # Adjust wait time if needed
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
            print(f"No more pages available for {salary_range}. Moving to the next salary range.")
            break

    # After extracting data for the current salary range, unselect it for the next iteration
    salary_filter = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[@title='{salary_range}']"))
    )
    salary_filter.click()
    time.sleep(4)

# Create a DataFrame after the loop
data = {
    'Title': titles,
    'Company': companies,
    'Experience': experiences,
    'Salary': salaries,
    'Location': locations,
    'Unix': Unix,
    'Oracle': Oracle,
    'Linux': Linux,
    'Debugging': Debugging,
    'XML': XML,
    'MySQL': MySQL,
    'RDBMS': RDBMS,
    'Java': Java,
    'Python': Python,
    'Adobe': Adobe
}

# Load existing data from CSV if it exists
existing_df = pd.read_csv("C:\\Users\\SAI PAVAN\\Desktop\\sal\\transformed_jobs_data.csv") if os.path.exists("C:\\Users\\SAI PAVAN\\Desktop\\sal\\transformed_jobs_data.csv") else pd.DataFrame()

# Concatenate existing data with new data
df = pd.concat([existing_df, pd.DataFrame(data)])

# Save the DataFrame to a CSV file
csv_path = "C:\\Users\\SAI PAVAN\\Desktop\\sal\\transformed_jobs_data.csv"
df.to_csv(csv_path, index=False)

print(f"Data saved to {csv_path}")

# Close the browser
driver.quit()
