from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if not task:
        flash("Please enter a task")
        return redirect(url_for("index"))
    tasks.append(task)
    flash("Task added successfully")
    return redirect(url_for("index"))

@app.route("/remove", methods=["POST"])
def remove():
    task = request.form.get("task")
    tasks.remove(task)
    flash("Task removed successfully")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
