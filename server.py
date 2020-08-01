from flask import Flask, render_template, request, url_for , redirect
import csv
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

def record_to_database(data):
    with open("database.csv", "a+") as database:
        email = data.get("email")
        subject = data.get("subject")
        text = data.get("text")
        csv_writer = csv.writer(database, delimiter= ",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,text])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        record_to_database(data)
        return redirect("/thanks")
    else:
        return "not epic"

