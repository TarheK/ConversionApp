from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/home.html")
def render_home():
    return render_template('home.html')

@app.route("/page1.html")
def render_page1():
    return render_template('page1.html')

@app.route("/page2.html")
def render_page2():
    return render_template('page2.html')

@app.route("/page3.html")
def render_page3():
    return render_template('page3.html')

    
if __name__=="__main__":
    app.run(debug=False, port=54321)
