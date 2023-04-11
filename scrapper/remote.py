import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

URL = 'https://remoteok.com'

def get_jobs(word):
  url = f'{URL}/remote-{word}-jobs?hide_closed=true'
  jobs = extract_all_rmt(url)
  return jobs
  
  
def extract_all_rmt(url):
  jobs = []
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, 'html.parser')
  job_field = soup.find('div', {'class':'container'}).find_all('tr', {'class':'job'})
  for job in job_field:
    job = extract_rmt(job)
    jobs.append(job)
  return jobs

def extract_rmt(html):
  job = html.find('td', {'class':'company'})
  title = job.find('a').find('h2').string
  company = job.find('span').find('h3').string
  location = job.find('div', {'class':'location'}).string
  if '$' in location:
    location = 'N/A'
  href = job.find('a')['href']
  link = URL + href
  return {
    'title': remove_emoji(title),
    'company': remove_emoji(company),
    'location': remove_emoji(location),
    'link': link
  }

def remove_emoji(string):
    return string.encode('ascii', 'ignore').decode('ascii').strip()
  