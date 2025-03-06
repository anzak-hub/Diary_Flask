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
    
    # Find all the files
    file_list = os.listdir(directory)
    
    #List of activities that have been done
    foundActivities = []
    
    #for each file a string of activities that has to be searched trough
    for f in file_list:
        
        activities = ""
        
        with open(f, 'r') as file:
            lines = file.readline()
            
            for line in lines:
                activities += line
                
            if activity in activities:
                foundActivities.append(activity, "datum:" f"{f}".strip(".txt"))
    
    return foundActivities       
                                   

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    print("Success!")