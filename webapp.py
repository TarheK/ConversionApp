from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template('home.html')

@app.route("/page1")
def render_page1():
    return render_template('page1.html')
def render_response1():
    feet = float(request.args['feet'])
    response=feet * (1/12)

@app.route("/page2")
def render_page2():
    return render_template('page2.html')

@app.route("/page3")
def render_page3():
    return render_template('page3.html')

    
if __name__=="__main__":
    app.run(debug=False, port=54321)
