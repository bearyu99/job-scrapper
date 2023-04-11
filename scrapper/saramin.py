import requests, re
from math import ceil
from bs4 import BeautifulSoup

page_count = 40
URL = 'https://www.saramin.co.kr'

def get_jobs(word):
  url = f'{URL}/zf_user/search/recruit?searchword={word}'
  last_page = get_last_page(url)
  jobs = extract_all_srm(url, last_page)
  return jobs

def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  job_block = soup.find('section', {'class':'section_search'})
  total_count = job_block.find('span').string
  result_count = int(re.sub('총|,|건| ', '', total_count)) / page_count
  return ceil(result_count)

def extract_all_srm(url, last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f'{url}&recruitPage={page+1}&recruitPageCount={page_count}')
    soup = BeautifulSoup(result.text, 'html.parser')
    job_field = soup.find('section', {'class':'section_search'}).find_all('div', {'class':'item_recruit'})
    for job in job_field:
      job = extract_srm(job)
      jobs.append(job)
  return jobs

def extract_srm(html):
  title = html.find('h2', {'class':'job_tit'}).find('a')['title']
  company = html.find('strong', {'class':'corp_name'}).find('a').string.strip()
  location = html.find('div', {'class':'job_condition'}).find('span').find('a')
  if location is None:
    location = 'N/A'
  else:
    location = location.string
  link = html.find('h2', {'class':'job_tit'}).find('a')['href']
  return {
    'title': title,
    'company': company,
    'location': location,
    'link': URL + link
  }