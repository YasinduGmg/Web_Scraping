from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
soup = BeautifulSoup(html_text.text,'lxml')
jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

def print_job_details(job):
    company_name = job.find('h3').text.strip()
    skills_div = job.find('div',class_='more-skills-sections')
    skills = [skill.text.strip() for skill in  skills_div.find_all('span')]
    posted_date = job.find('span',class_='sim-posted').span.text
    
    print(f"""
    Company Name: {company_name}
    Skills: {", ".join(skills)}
    Posted Date: {posted_date}
""")
for job in jobs:
    print_job_details(job)

    

