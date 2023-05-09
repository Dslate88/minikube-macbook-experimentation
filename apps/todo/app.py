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
    priority = request.form.get("priority")  # Get the priority from the form
    if not task:
        flash("Please enter a task")
        return redirect(url_for("index"))
    tasks.append({"task": task, "priority": priority})  # Store the task and priority as a dictionary
    flash("Task added successfully")
    return redirect(url_for("index"))

@app.route("/remove", methods=["POST"])
def remove():
    task = request.form.get("task")
    task_to_remove = next(t for t in tasks if t["task"] == task)  # Find the task dictionary with the matching task
    tasks.remove(task_to_remove)
    flash("Task removed successfully")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
