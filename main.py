from flask import Flask, render_template,send_file
import requests

app = Flask('')
@app.route('/')
def main():
    return 'THE OSTRICH'
  
@app.route('/internal/<mailid>')
def mails(mailid):
    r = requests.get(f"https://mailable.me/secretm/{mailid}")
    return render_template('mail.html',foobar=r.content)

@app.route('/<mailid>')
def maili(mailid):
    r = requests.get(f"https://paste.theostrich.eu.org/raw/{mailid}")
    return render_template('mail.html',foobar=r.text)

@app.route('/mail.png')
def png():
   return send_file("mail.png")
  


def run():
    app.run(host='0.0.0.0', port=8080)
run()


		