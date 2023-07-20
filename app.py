from flask import Flask, render_template, request, redirect
import requests
import json
from python.job import get_jobs
from python.location import get_location
from forms import JobInput
app = Flask(__name__,)
app.config['SECRET_KEY'] = '7e129e3b3bcf778f16fe0d0b5ab7593a'
from flask_bootstrap import Bootstrap
Bootstrap(app)

@app.route("/", methods = ['GET','POST'])
def home():
    data = get_location()
    print(data)
    city = data['city']
    posts = get_jobs("anything",city)
    if request.method == "POST":
       # getting input with name = title in HTML form
       first = request.form.get("title")
       # getting input with name = location in HTML form
       last = request.form.get("location")
       return jobs(first, last)
    return render_template('home.html', posts=posts )
    #return render_template('home.html', title='home')

@app.route("/jobs", methods = ['GET','POST'])
def jobs(title, location):
    posts = get_jobs(title,location)
    return render_template('jobs.html', posts=posts)

@app.route("/about", methods = ['GET','POST'])
def about():
    return render_template('about.html')

@app.route("/redirect", methods=["GET"])
def direct():
    simple = request.get("url")
    return redirect(simple, code=302)

if __name__ == '__main__':
    app.run(debug=True)



