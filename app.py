from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

                                                                
if __name__ == "__main__":
    app.run()
