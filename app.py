from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

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
    if request.method == 'POST':

        save_button_pressed = request.form.get("save") #if the save button was pressed
        search_button_pressed = request.form.get("search") #if the save button was pressed
        
        if save_button_pressed is not None:
            diaryInput = request.form["diaryInput"]
            
            saveDiaryInputToFile(diaryInput)

        elif search_button_pressed is not None:
            wordToSearch = request.form["wordToSearch"]
            print("\n Serach button pressed", wordToSearch)
            searchFilesForWord(wordToSearch)

        

    files_list = get_all_tagebuch_inputs()
    return render_template('index.html', files=files_list, message = "Enter what happend today")

@app.route('/selected-item', methods=["GET", 'POST'])
def selected_item():
    print(request.method)
    data = request.get_json()
    selected_item = data.get('selectedItem')
    print(f'Selected item: {selected_item}')
    return render_template('index.html', message = "After selected")
    return jsonify({'status': 'success', 'selectedItem': selected_item})

@app.route('/doubleclick/<int:item_id>', methods=["GET", "POST"])
def handle_doubleclick(item_id):
    data = request.get_json()
    print(data)
    # Process the double-click event here
    #item = items.get(item_id)
    print(f"Item {data['id']}  {data['selectedItem']}was double-clicked!")
    
    message_ = readFile(data["selectedItem"].replace("\"",""))
    print("THE message is", message_)
    
    return render_template('index.html', message = message_)
    return jsonify({"message": f"Item {data['id']} was double-clicked!"})

def searchFilesForWord(wordToSearch):
    folder_path = "diary_sites/"
    
    files_with_text = []

    files = get_all_tagebuch_inputs()
    for file_name in files:
        file_name = folder_path + file_name
        with open(file_name, 'r') as file:          

            for line in file:
                print("line", line, line.find(wordToSearch))
                if line.find(wordToSearch) != -1:
                    #the word is in the file
                    files_with_text.append(file_name)
                    break
    for file in files_with_text:
        print("\n\n", file)

def readFile(file_name):
    folder_path = "diary_sites/"
    file_name = folder_path + file_name

    file_text = ""
    with open(file_name, 'r') as file:          

            for line in file:
                file_text += line
    return file_text

def get_all_tagebuch_inputs():
        folder_path = "diary_sites/"
        # List all files in the specified folder
        files = os.listdir(folder_path)

        for file_name in files:
            print(file_name)
        
        return files

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
    