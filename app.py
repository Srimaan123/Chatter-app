from flask import Flask,render_template,request,url_for
from 
app = Flask(__name__)

@app.route("/")
def hello():
  return "hi welcome to flask"

if __name__ == "__main__":
  app.run(debug=True)
