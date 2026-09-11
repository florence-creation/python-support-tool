from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        name = request.form.get("name", "")
        number = request.form.get("number", "")
        reason = request.form.get("reason", "")

        if not name or not number or not reason:
            result = "Tanpri ranpli tout chan yo."
        else:
            result = "Rapò a prepare avèk siksè."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
