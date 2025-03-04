from flask import Flask, render_template, request

app = Flask(__name__)

# Definere den Pfad für die Home Page
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)