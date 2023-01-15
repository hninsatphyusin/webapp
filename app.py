from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'XXXXXXXX'
app.config['MAIL_PASSWORD'] = 'XXXXX'
app.config['MAIL_USE_TLS'] = True

mail = Mail(app)


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

@app.route('/sendemail')
def sendemail():
    fname = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    msg = Message(subject + " - " + fname + " (" + email + ") ", sender="XXXXXXXX", recipients=["XXXXXXXX"])
    msg.body = message
    mail.send(msg)
    return "sent!"

                                                                
if __name__ == "__main__":
    app.run()
