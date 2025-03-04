from flask import Flask, render_template, request

app = Flask(__name__)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "you are underweight - eat more!"
    elif bmi < 25:
        return "you have normal weight - keep on going!"
    else:
        return "you are overweight - eat less and move more!"

# Definere den Pfad für die Home Page
@app.route('/', methods=["GET", "POST"])
def index():
    bmi = None
    cat = None
    if request.method == 'POST':
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        bmi = round(weight / (height/100)**2, 2)
        cat = categorize_bmi(bmi)
    
    return render_template('index.html', bmi=bmi, category=cat)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)