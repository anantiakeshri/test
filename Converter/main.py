from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=300)

# adding padding
window.config(padx=70, pady=70)

def convert():
    pass
    
    

#Text
text = Text(height=1, width=10)
text.focus()                        #Puts cursor in textbox.
text.insert(END, " ")
print(text.get("1.0", END))         #Get's current value in textbox at line 1, character 0
text.grid(column=3, row=0)

# Label 0
label_0 = Label(text="Miles", font=("Ariel", 20))
label_0.config(padx=10, pady=10)
label_0.grid(column=4, row=0)

# Label 1
label_1 = Label(text="is", font=("Ariel", 20))
label_1.config(padx=10, pady=10)
label_1.grid(column=0, row=1)

# Label 2
label_2 = Label(text="equal", font=("Ariel", 20))
label_2.config(padx=10, pady=10)
label_2.grid(column=1, row=1)

# Label 3
label_3 = Label(text="to", font=("Ariel", 20))
label_3.config(padx=10, pady=10)
label_3.grid(column=2, row=1)

# Entry 
entry = Entry(width=5)
entry.grid(column=3, row=1)

# Label 4
label_4 = Label(text="Km", font=("Ariel", 20))
label_4.config(padx=10, pady=10)
label_4.grid(column=4, row=1)

# Buttons
button = Button(text="Calculate")
button.grid(column=3, row=2)

window.mainloop()