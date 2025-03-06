from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

# Definere den Pfad für die Home Page
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        
        diaryInput = request.form["diaryInput"]
        
        saveDiaryInputToFile(diaryInput)
        
        LookForActivity = request.form["lookForActivity"]
        
        findTheActivity(lookForActivity)
        
    return render_template('index.html')

def saveDiaryInputToFile(text_):
    folder_path = "diary_sites/"
    
    #get today datetime
    today = datetime.today().date()

    #create the file name
    file_name = folder_path + f"{today}" + ".txt"

    # Open a file in write mode
    with open(f"{file_name}", 'a') as file:         
        # Write some text to the file
        file.write(text_ + "\n")

def findTheActivity(activity):
    
    directory = "/diarysites"
    
    # All the files
    file_list = os.listdir(directory)

    for f in file_list:
        
        with open(f, 'r') as file:
            activities = ""
            lines = file.readline()
            
            for line in lines:
                activities += line
            
            if activity in activities:
                return f
                                   

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    print("Success!")