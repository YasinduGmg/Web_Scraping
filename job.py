from bs4 import BeautifulSoup
import requests
import time


def print_job_details(job):
    posted_date = job.find('span',class_='sim-posted').span.text
    if 'few' in posted_date:
        company_name = job.find('h3').text.strip()
        skills_div = job.find('div',class_='more-skills-sections')
        skills = [skill.text.strip() for skill in  skills_div.find_all('span')]
        more_info = job.header.h2.a['href']
        
        print(f"""
        Company Name: {company_name}
        Skills: {", ".join(skills)}
        More Info: {more_info}
        Posted Date: {posted_date}
    """)
        
def get_job_details():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
    soup = BeautifulSoup(html_text.text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        print_job_details(job)

    
if __name__ == '__main__':
    while True:
        get_job_details()
        time_wait = 60
        print(f"Waiting {time_wait} Minutes ")
        time.sleep(time_wait * 60)
