from flask import Flask, render_template

app = Flask(__name__)


# plik home.html musi byc umieszczony w katalogu templates w głównym katalogu projektu
@app.route("/")
def home():
    # return "Hello World"
    return render_template('home.html')


@app.route("/salvador")
def salvador():
    return "Hello Salvador"


if __name__ == '__main__':
    app.run(debug=True, port=8080)
