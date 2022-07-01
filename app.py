
from flask import Flask, render_template, request
import model as m


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/submit', methods = ["POST"])
def show():
    result = []
    if request.method == "POST":
        result.append(int(request.form["industrial_risk"]))
        result.append(int(request.form["management_risk"]))
        result.append(int(request.form["financial_flexibility"]))
        result.append(int(request.form["credibility"]))
        result.append(int(request.form["competitiveness"]))
        result.append(int(request.form["operating_risk"]))
        res = m.train(result)
    return render_template('result.html', res = res )

        

if __name__ == "__main__":
    app.run(debug=True)    