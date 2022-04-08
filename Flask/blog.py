from flask import Flask,render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    sayi = 10
    sayi2=list([1,2,3,4,5,6,7,8,9])
    soz={"alper":35,"Desa":1350}
    return render_template("index.html",nomber=sayi,namber=sayi2,deva=soz)


@app.route("/about")
def about():
    return "<h1>Abouta geldin lan</h1>"



if __name__ == "__main__":
    app.run(debug=True)