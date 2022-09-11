from flask import Flask, render_template, redirect, url_for
#from views import views

app = Flask(__name__)

#app.register_blueprint(views, url_prefix="/home")

@app.route("/Home")
def home():
    return render_template("home.html")

@app.route("/MoviePicker")
def movie_picker():
   return render_template("moviepicker.html")

@app.route("/")
def home2():
    return render_template("home.html")

if __name__== '__main__':
    app.run(debug=True, port=8000)