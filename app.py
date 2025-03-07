from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

# Definere den Pfad für die Home Page
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        
        diaryInput = request.form["diaryInput"]
        
        lookForActivity = request.form["lookForActivity"]
        
        if diaryInput:
            saveDiaryInputToFile(diaryInput)  
            
        if lookForActivity:
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
    
    directory = "diary_sites/"
    
    # Find all the files
    file_list = os.listdir(directory)
    
    activities = []
    
    #for each file a string of activities that has to be searched trough
    for f in file_list:
 
        with open(directory + f, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line != " ":
                    activities.append((f.strip(".txt"), line.strip()))
    return activities
    # for a in activities:
    #     if activity in a[1]:
    #         print(a[0])
              
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)