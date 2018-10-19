from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template('home.html')
@app.route("/responseh")
def render_responseh():
    millimeters = float(request.args['millimeters'])
    response=millimeters * (1/10)
    return render_template('response.html', response = response)

@app.route("/page1")
def render_page1():
    return render_template('page1.html')
@app.route("/response1")
def render_response1():
    feet = float(request.args['feet'])
    response=feet * 12
    return render_template('response.html', response = response)
    
@app.route("/page2")
def render_page2():
    return render_template('page2.html')
@app.route("/response2")
def render_response2():
    killometers = float(request.args['killometers'])
    response=killometers * 1000
    return render_template('response.html', response = response)                       

@app.route("/page3")
def render_page3():
    return render_template('page3.html')
@app.route("/response3")
def render_response3():
    miles = float(request.args['miles'])
    response=mile * 5280
    return render_template('response.html', response = response)

    
if __name__=="__main__":
    app.run(debug=False, port=54321)
