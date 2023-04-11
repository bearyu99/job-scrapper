from flask import Flask, render_template, request, redirect, send_file
from scrapper import wwr, remote, saramin
from exporter import save_to_file

app = Flask('JobScrapper')

db = {}

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/report')
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = (
        saramin.get_jobs(word) +
        remote.get_jobs(word) +
        wwr.get_jobs(word)
      )
      db[word] = jobs
  else:
    return redirect('/')
  return render_template(
    'report.html', 
    searchingBy=word,
    resultNumber=len(jobs),
    jobs=jobs
  )

@app.route('/export')
def export():
  word = request.args.get('word')
  if word:
    word = word.lower()
    jobs = db.get(word)
    if jobs:
      save_to_file(jobs, word)
      return send_file(f'csv/{word}.csv', download_name=f'{word}.csv', as_attachment=True)
  return redirect('/')
    

app.run(host='localhost')

#saramin.get_jobs('golang')