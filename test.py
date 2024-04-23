import tkinter as tk 

# Khoi tao cua so dang nhap 
window_login = tk.Tk()
window_login.geometry("350x500")

# khoi tao giao dien dang nhap  
window_login.title("Login") 


# khoi tao cac bien nhan gia tri khi duoc chuyen vao 
user_name = tk.StringVar( )
pass_word  = tk.StringVar( )
# khoi tao cac bien cho nguoi dung nhap ten moi vao 
new_user = tk.StringVar() 
new_pass = tk.StringVar()
dict = {"dung123":"12345", 
        "dung234":"23456"}

# khoi tao nhan cua ten nguoi dang nhap va mat khau 
user_name_task = tk.Label(window_login, text = "User Name: " ) 
pass_word_task = tk.Label(window_login, text = "Pass Word: " ) 

# khoi tao thanh text giup nguoi dung nhap du lieu 
text_user_name = tk.Entry(window_login, textvariable=user_name)
text_pass_word = tk.Entry(window_login, textvariable=pass_word )
# Set vi tri cho label 

user_name_task.place(x = 60, y = 60) 
pass_word_task.place(x = 60, y = 100) 
# set vi tri cho text bar 

text_user_name.place(x = 150, y = 60) 
text_pass_word.place(x = 150, y = 100) 

# ham duoc goi sau khi na nut login 
def Check_PassWord( ) : 
    text = tk.StringVar()

    for i in dict : 
        if(user_name.get() == i): 
            if( pass_word.get() == dict[i]): 
                text = tk.StringVar(window_login, "Sucessfully !!! ")
            else : 
                text = tk.StringVar(window_login, "Wrong pass or user_name !!! ")
        
    message = tk.Label(window_login, textvariable= text)
    message.pack()
   
# neu nguoi dung chua co tai khoan, tao ham giup nguoi dung nhap vao thong tin ca nhan 
def Add_Dict( ) : 
    dict[new_user.get()] = new_pass.get()
    for i in dict : 
        print (f"user name: {i} | pass word: {dict[i]}")
    

def Add_infor ( ) : 
    # Dung cua so cu va tao cua so moi 
    add = tk.Toplevel() 
    add.geometry("350x500")
    add.title("New account") 
    
    #Tao label cho nguoi dung nhap vao ten 
    new_user_name = tk.Label(add, text = "New User Name :")
    new_pass_word = tk.Label(add, text = "New Pass Word :")

    # Tao text bar cho nguoi dung nhap thong tin ca nhan 
    new_user_name_text = tk.Entry(add, textvariable=new_user)
    new_pass_word_text = tk.Entry(add, textvariable=new_pass) 

    # Set vi tri cho tung thanh cong cu 
    new_user_name.place(x = 60, y = 60) 
    new_pass_word.place(x = 60, y = 100) 
    
    new_user_name_text.place(x = 150, y = 60) 
    new_pass_word_text.place(x = 150, y = 100) 
    
    add_new_button = tk.Button(add, text="Create new", command=Add_Dict)
    add_new_button.place(x = 150, y = 150 )
    
    
# tao ra nut giup nguoi dung dang nhap 
login_button = tk.Button(window_login, text = "login", command= Check_PassWord) 
login_button.place(x = 200, y = 150) 

# Tao ra thanh cong cu giup nguoi dung moi tao tai khoan 
signup_label = tk.Label(window_login, text="Create new account !!")
signup_button = tk.Button(window_login, text = "click here" , command= Add_infor) 

signup_label.place(x = 100, y = 200) 
signup_button.place(x = 220, y = 200) 
# vong lap trang web 
window_login.mainloop( )
