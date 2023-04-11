import requests
from bs4 import BeautifulSoup

URL = 'https://weworkremotely.com'

def get_jobs(word):
  url = f'{URL}/remote-jobs/search?term={word}'
  jobs = extract_all_wwr(url)
  return jobs

def extract_all_wwr(url):
  jobs = []
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  job_block = soup.find_all('section', {'class':'jobs'})
  for job_record in job_block:
    job_field = job_record.find_all('li')
    for job in job_field[:-1]:
      job = extract_wwr(job)
      jobs.append(job)
  return jobs

def extract_wwr(html):
  job = html.find_all('a')[1]
  title = job.find('span', {'class': 'title'}).string
  company = job.find('span', {'class': 'company'}).string
  location = job.find('span', {'class': 'region company'})
  if location is not None:
    location = location.string
  else:
    location = 'N/A'
  link = f'{URL}{job["href"]}'
  return {
    'title': title,
    'company': company,
    'location': location,
    'link': link
  }