from flask import Flask, render_template, url_for, redirect, request
from mydb import DataBase
from datetime import datetime
from gen import StudentGen

app = Flask(__name__)

database = DataBase("demo")
#database.create_table()
#obj = StudentGen(20)
#for stud in obj.students:
#    database.insert(stud)

def time(date):
    date_1 = datetime.strptime(date,"%Y-%m-%d" )
    return  date_1.strftime("%d.%m.%Y")

app.jinja_env.globals.update(time = time)

@app.route("/")
def index():
    
    news = database.select_all()
    return render_template("index.html", news = news)
 
@app.route("/news/<slug>") 
def news(slug):
    try:
        news = database.select_by_col({"slug": slug})[0]
        author_name = f"{news.pop('fname')} {news.pop('sname')}"
        news_header= f"{news.pop('news_head')}"
        news.pop("id")
        slug = news.pop("slug")
        result = []
        for key, value in news.items():
            if key =="date":
               
                result.append({key:time(value)})
            else:
                result.append({key:value})
    except Exception as e:
        return e
    
   
    return render_template("info.html", data = result, name = author_name, news_header=news_header,slug =slug)


@app.errorhandler(500)
def internal_error(error):
    return redirect(url_for("index"))

@app.errorhandler(404)
def not_found_error(error):
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()

