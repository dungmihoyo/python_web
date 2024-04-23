from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage 
from PIL import Image, ImageTk

root = Tk()
root.geometry("1200x800")

# Create background website 
head = Image.open('bg.png')
hand = Image.open('login.png')
login_hand = Image.open('photo.png')
# hand_menu = Image.open('menu.png')
# head.paste(hand, (5,5)) 
login_photo = ImageTk.PhotoImage(hand)
bg_photo = ImageTk.PhotoImage(head) 
login_photo = ImageTk.PhotoImage(login_hand)
# menu_photo = ImageTk.PhotoImage(hand_menu) 

back_g = Label(root, image=bg_photo)
back_g.place(x = 0,y = 0 ) 

def Check_User( ) : 
    button1 = Button( frame, image = login_photo) 
    button1.pack_forget()
    frame.place(x = 900, y = 50)

# Create Login Window 
def Login_Window( ) : 
    #Create new window out website 
    newWindow = Toplevel( ) 
    newWindow.geometry("400x400") 
    newWindow.title("Login Acount")
    
    #initial value for login information
    name_var = StringVar( )
    pass_var = StringVar( )

    label_user_name = Label(newWindow, text = "User Name:") 
    label_pass_word = Label(newWindow, text = "Pass Word:") 

    # Set grid for label 
    label_user_name.place(x = 60, y = 60)
    label_pass_word.place(x = 60, y = 100)

    # Create Text login account 
    text_user_name = Entry(newWindow, textvariable= name_var) 
    text_pass_word = Entry(newWindow, textvariable= pass_var) 
    
    # Set grid for entry account 
    text_user_name.place(x = 150, y = 60)
    text_pass_word.place(x = 150, y = 100)

    # Create login button 
    login_button = Button(newWindow, text = 'Login', command=Check_User) 
    # Set grid for login button 
    login_button.place(x = 200, y =150 )

    # Create Acount Window ( ) 
    new_label = Label(newWindow, text = 'Create new account' ) 
    new_label.place(x = 80 , y = 300) 

    # Create new account button
    new_button = Button(newWindow, text = 'Sign Up' ) 
    new_button.place(x = 200, y = 300) 

def Menu ( ) : 
    layer_menu_1 = Button(frame_menu, text = 'Introduction' )
    layer_menu_2 = Button(frame_menu, text = 'Lecture_1' )
    layer_menu_3 = Button(frame_menu, text = 'Lecture_2' )

    layer_menu_1.pack()
    layer_menu_2.pack()  
    layer_menu_3.pack() 

#Create frame for button 
frame = Frame(root) 
frame.pack()
frame.place(x = 900, y = 50) 

#Create Login Side 
button1 = Button( frame, image = login_photo, command=Login_Window) 
button1.pack()
frame.place(x = 900, y = 50)

# Create Menu Button 
frame_menu = Frame(root, bg ='#88cffa') 
frame_menu.pack()

# Create hidden layer 

button_menu = Button(frame_menu, text = 'Menu' , command=Menu) 
button_menu.pack( )


root.mainloop()

