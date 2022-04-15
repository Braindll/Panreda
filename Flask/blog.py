from flask import Flask,render_template, request
from flaskext.mysql import MySQL


app = Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Desa6672"
app.config["MYSQL_DB"]="flask"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql = MySQL(app)



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