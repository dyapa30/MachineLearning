from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course.This will be an amazing course"

@app.route("/index")
def index():
    return "Welcome to index page"


if __name__=="__main__":
    app.run(debug=True)