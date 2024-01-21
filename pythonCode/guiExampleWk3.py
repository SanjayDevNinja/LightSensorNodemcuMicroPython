

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk() #similar to a windows form
root.title("Narendra's Masterpiece") #title of the window
frame = ttk.Frame( #create a Frame (container in this case)
root, #parent of this widgetprogram
width=360, #width
height=240) #height
frame.grid() #row=0, column=0
frame['padding'] = (5,10) #padding
frame['borderwidth'] = 10 #border
frame['relief'] = 'sunken' #style: panel or gropubox

def read_form(*args):
    messagebox.showinfo( #from tkinter import messagebox
    title='Form Information',message=f'Username: {username.get()} \nResidency: {residency.get()}\nCourses:{comp100.get()} {comp120.get()} {comp213.get()}\nProgram: ')

#row 0
lbl_feather = ttk.Label(frame) #the parent of this widget
image = PhotoImage(file='feather.png') #create a PhotoImage
lbl_feather['image'] = image #put the above image on label
lbl_feather.grid( #positionsing the label
column=1, #column=1
row=0, #row=0
sticky=(W, E)) #where to anchor in the cell

#row 1
lbl_full_name = ttk.Label( #creates a Label
frame, #parent
text='Full name:').grid( #sets the text
column=0, #column=0
row=1, #row=1
sticky=(W, E)) #align center
username = StringVar() #variable that will be used to communicate
name = ttk.Entry( #creates an Entry
frame, #parent
textvariable=username).grid( #the variable to bind to
column=1, #column=1
row=1, #row=1
sticky=(W)) #align left
#row 2
ttk.Label( frame, text='Residency:').grid( column=0, row=2, sticky=(W, E))
panel = ttk.Frame(frame) #this will be the container for the widget below
panel.grid(column=1, row=2, sticky=(W, E))
panel['borderwidth'] = 3
panel['relief'] = 'ridge'
residency = StringVar()
ttk.Radiobutton(panel, text='Domestic', variable=residency, value='dom').grid(
column=0, row=0, sticky=(W)) #grid coordinate is for its immediate parent
ttk.Radiobutton(panel, text='International', variable=residency,
value='intl').grid(
column=0, row=1, sticky=(W))
#row 4
ttk.Label( frame, text='Courses:').grid( column=0, row=4, sticky=(W, E))
panel = ttk.Frame(frame)
panel.grid( column=1, row=4, columnspan=4, sticky=(W, E))
panel['borderwidth'] = 3
panel['relief'] = 'ridge'
comp100 = StringVar()
comp213 = StringVar()
comp120 = StringVar()
#row 4 continued
check = ttk.Checkbutton( panel,
text='Programming I',
variable=comp100,
# offvalue='imperial',
onvalue='comp100')
check.grid(column=0, row=0, sticky=(W))
ttk.Checkbutton( panel, text='Web Page Design',
variable=comp213, onvalue='comp213').grid(
column=0, row=1, sticky=(W))
ttk.Checkbutton( panel, text='Software Engineering Fundamentals',
variable=comp120, onvalue='comp129').grid(
column=0, row=2, sticky=(W))
#row 5
button = ttk.Button(frame, text='Reset') #buttons can also have images
button.grid(column=0, row=5, sticky=(W, E))
ttk.Button(frame, text='Ok',
command=read_form).grid( #the function that will be called
column=1, row=5, sticky=(W, E))
ttk.Button(frame, text='Exit',
command=root.quit).grid( #the delegate that will be called
column=2, row=5, sticky=(W, E))
root.mainloop() #starts the main event loop
