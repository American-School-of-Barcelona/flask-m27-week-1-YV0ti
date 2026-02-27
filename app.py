from flask import Flask , render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))

#render_template renders the template into HTML that my browser understands
#


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

if __name__ == "__main__":
    app.run(debug=True)
