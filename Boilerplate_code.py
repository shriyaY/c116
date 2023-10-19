#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/program")

#‘/’ URL is bound with first_flask function.
def my_program():
    return "Today I'm learning about PYTHON FLASK"


@app.route("/about_me")
def shriya():
    return("i like ice skating")

@app.route("/python") 
def skate():
    grade = "9"
    return render_template("index.html",grade_number=grade)

@app.route("/code")
def picture():
    return render_template("index.html", grade_number='9')

#run the application on local server
app.run(debug=True)
