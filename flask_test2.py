from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/submit", methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # return f"Name: {name}, email: {email}"
    dictionary = {"name": name, "email": email}
    # zapisz_plik(f"Name: {name}, email: {email}")
    zapisz_plik(dictionary)
    return render_template('submitted.html', name=name, email=email)


@app.route("/users")
def users():
    dane = odczytaj_plik()
    print(dane)
    return dane
    # return render_template('submitted.html', name=dane['name'], email=dane['email'])


@app.route("/userwww")
def user_www():
    dane = odczytaj_plik()
    dict2 = json.loads(dane)  # zamienia json na dict
    # return dane
    return render_template('submitted.html', name=dict2['name'], email=dict2['email'])


def zapisz_plik(dane):
    with open("flask_dane.json", "w") as f:
        json.dump(dane, f, indent=4)


def odczytaj_plik():
    with open('flask_dane.json', 'r') as fh:
        data = json.load(fh)
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
# 15:10
