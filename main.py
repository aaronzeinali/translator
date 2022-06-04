import googletrans
from tkinter import *
from tkinter import ttk

##### MAIN FUNCTION
translator = googletrans.Translator()
###################

window = Tk()
window.geometry("450x120")
window.title("Bookingo Translator")

def display_text():
    global entry
    string = entry.get()
    text = translator.translate(string)
    if text.src == "en":
        text2 = translator.translate(string, dest='fa')
        label.configure(text=text2.text, )
    else:
        label.configure(text=text.text)
    

    
    
label = Label(window, text="", font=("cambria"))    
label.pack()

entry = Entry(window, width=60)
entry.focus_set()
entry.pack()

ttk.Button(window, text="Translate", width=50, command= display_text).pack(pady=20)
window.mainloop()