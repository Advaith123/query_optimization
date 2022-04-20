from flask import Flask,request, render_template
import sqlite3
import process

app = Flask(__name__)

conn = sqlite3.connect('sqlqueries.sqlite',check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE if not exists QUERIES (id INTEGER PRIMARY KEY AUTOINCREMENT, query VARCHAR)''')
# @app.route("/")
# def hello():
#     return "Hello, World!"

cur.close()
@app.route('/', methods =["GET", "POST"])
def inp():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       cur = conn.cursor()
       query = request.form.get("fquery")
       #print(type(query))
       cur.execute('''INSERT INTO QUERIES (query) VALUES (?)''', (query,))
       #print('F')
       cur.execute('''SELECT * FROM QUERIES ''')
       #p = cur.fetchall()
       #print(p)
       cur.close()
       er1 = process.group(query)
       er2 = process.dates(query)
       er3 = process.like(query)
       er4 = process.star(query)
       er5 = process.dist(query)
       return render_template('result.html',er1 = er1,er2 = er2,er3 = er3,er4 = er4,er5 = er5)
    return render_template("home.html")


@app.route('/past')
def past():
    cur = conn.cursor()
    cur.execute(''' SELECT * FROM QUERIES WHERE ID > (SELECT COUNT(*) FROM QUERIES) - 5;''')
    p = cur.fetchall()
    #print(type(p))
    cur.close()
    try:
        p1=p[0][1]
        p2=p[1][1]
        p3=p[2][1]
        p4=p[3][1]
        p5=p[4][1]
        return render_template('past.html',p1=p1,p2=p2,p3=p3,p4=p4,p5=p5)
    except:
        m = 'error: 5 entries not there'
        return render_template('past.html',m=m)

@app.route('/guide')
def guide():
    return render_template('guide.html')

if __name__ == "__main__":
    app.run(debug=True)