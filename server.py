from flask import Flask, render_template, url_for, request, send_from_directory, redirect
import os
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('Database.txt', mode='a') as Database:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        Database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('Database.csv', mode='a') as Database2:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        csv.writer(Database2, delimiter=',', quotechar='"',
                   quoting=csv.QUOTE_MINIMAL).writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/ThankYou.html')
    else:
        return redirect('/Message_not_sent.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
