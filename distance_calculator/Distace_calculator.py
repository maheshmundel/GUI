from tkinter import * 

def result(source, destination, mode):

    api_key = 'Your_api_key'
    base = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    if mode_field == 'train':
        compelete_url = base + 'origins='+source+\
            '&destinations' + destination + \
            '&mode = transit&transit_mode = train' + \
            '&key =' + api_key
     #   r = requests.get(compelete_url)
    else:
        distance_field.delete(0, END)
        duration_field.delete(0, END)
        distance_field.insert(10,'100km')
        duration_field.insert(10,'1 hour')

# Function for getting values from respective text entry box and calling result funcion
def find():
    # get method returns current text as a string from entry box
    source = source_field.get()
    destination = destination_field.get()
    travel_modes = mode_field.get()
    # Calling result()
    result(source, destination, travel_modes)
    
# Function for inserting train string in mode_field entry box
def train():
    mode_field.delete(0, END)
    mode_field.insert(10,"train")

# Funstion for inserting driving string in mode_field entry box
def driving():
    mode_field.delete(0, END)
    mode_field.insert(10, "driving")

# Function for inserting walking string in mode_field entry box
def walking():
    mode_field.delete(0, END)
    mode_field.insert(10, "walking")

# Function for clearing the content
def del_source():
    source_field.delete(0, END)
    distance_field.delete(0, END)
    duration_field.delete(0, END)

# Function for clearing the content
def del_destination():
    destination_field.delete(0, END)
    distance_field.delete(0, END)
    duration_field.delete(0, END)

# Function for clearing the content
def del_modes():
    mode_field.delete(0, END)
    distance_field.delete(0, END)
    duration_field.delete(0, END)

# Function for clearing the content
def delete_all():
    source_field.delete(0, END)
    destination_field.delete(0, END)
    mode_field.delete(0, END)
    distance_field.delete(0, END)
    duration_field.delete(0, END)


#def del_source():
#    source_field.delete(0,END)

if __name__ == "__main__":
    #create a GUI Window
    master = Tk()

    master.config(bg='light green')

    #Set the configuration of GUI window
    master.geometry("500x300")

    #Create lebals
    Label1 = Label(master, text='Welcome').grid(row=0, column=1, sticky="E")
    Label2 = Label(master, text='Source').grid(row=1, column=0, sticky="E")
    Label3 = Label(master, text='Destination').grid(row=2, column=0)
    Label4 = Label(master, text='Choose travelling mode').grid(row=3, column=1)
    Label5 = Label(master, text='Distance').grid(row=7, column=0,sticky="E")
    Label6 = Label(master, text='Duration').grid(row=8, column=0,sticky="E")


    #Create entry box
    #ipadx keyword argument set width of entry space
    source_field = Entry(master)
    source_field.grid(row=1,column=1,ipadx="100")
    destination_field = Entry(master)
    destination_field.grid(row=2,column=1,ipadx="100")
    mode_field = Entry(master)
    mode_field.grid(row=5,column=1,ipadx="50")
    distance_field = Entry(master)
    distance_field.grid(row=7,column=1,ipadx="100")
    duration_field = Entry(master)
    duration_field.grid(row=8,column=1,ipadx="100")

    #create buttons
    #clear button attached to del_source function
    button1 = Button(master, text='CLEAR', command=del_source).grid(row=1,column=2)
    #clear button attached to del_destination function
    button2 = Button(master, text='CLEAR', command=del_destination).grid(row=2,column=2)
    #clear button attached to delete_all function
    button3 = Button(master, text='CLEAR ALL', command=delete_all).grid(row=9,column=1)
    #clear button attached to train function
    button4 = Button(master, text='Train',command=train).grid(row=4,column=0)
    #clear button attached to driving function
    button4 = Button(master, text='Driving', command=driving).grid(row=4, column=1)
    #clear button attached to walking function
    button5 = Button(master, text='Walking', command=walking).grid(row=4, column=2)
    #clear button attached to del_source function
    button6 = Button(master, text='RESULT', command=find).grid(row=6,column=1)
    #clear button attached to del_modes function
    button7 = Button(master, text='Clear', command=del_modes).grid(row=5,column=2)
    # Close button
    button8 = Button(master, text='Close', command=master.destroy).grid(row=10,column=1)

    #Start GUI
    master.mainloop()