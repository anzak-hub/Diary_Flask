from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "you are underweight - eat more!", "too-thin"
    elif bmi < 25:
        return "you have normal weight - keep on going!", "normal"
    else:
        return "you are overweight - eat less and move more!", "too-fat"

# Definere den Pfad für die Home Page
@app.route('/', methods=["GET", "POST"])
def index():
    bmi = None
    cat = None
    classy = None
    if request.method == 'POST':
        diaryInput = request.form["diaryInput"]
        
        saveDiaryInputToFile(diaryInput)
    
    return render_template('index.html', bmi=bmi, category=cat, classy=classy)

def saveDiaryInputToFile(text_):
    folder_path = "diary_sites/"
    #get current datetime
    now = datetime.now()
    # Format date and time as string
    date_time_str = now.strftime("%Y-%m-%d %H-%M")
    date_time_str = date_time_str.replace(" ", "-")

    #create the file name
    file_name = folder_path + date_time_str + ".txt"

    # Open a file in write mode
    with open(file_name, 'a') as file:          

        # Write some text to the file
        file.write(text_ + "\n")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    print("Success!")