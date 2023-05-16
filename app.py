from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods={"GET", "POST"})
def bmi_endpoint():
    if request.method == "POST":
        weight = int(request.form.get('weight', False))
        height = int(request.form.get('height', False))
        # if weight and height:
        #     bmi = weight / (height / 100) ** 2
        # else:
        #     bmi = ''
        bmi = weight / (height / 100) ** 2
        return render_template("bmi.html", bmi=bmi)


@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
