import pandas as pd 
import sqlite3 


conn = sqlite3.connect("user.db")
cursor = conn.cursor( ) 
query = """SELECT * FROM USER_INFOR"""
query_insert =  """INSERT INTO USER_INFOR VALUES (?, ?, ?, ?, ?)"""
cursor.execute(query) 
data = cursor.fetchall( )
print (data)


class User_Infor() : 
    def __init__(self) -> None:
        self.first_name = None 
        self.last_name = None 
        self.email = None 
        self.user_name = None 
        self.pass_word = None 
        
    def set_name(self, name  ) : 
        new = str ()
        result={"a": ["á", "ã", "à", "ạ", "ă", "ắ", "ằ", "ẵ", "ặ", "â", "ầ", "ấ", "ẫ", "ấ" ], 
                "o": ["ó", "ọ", "ò", "ó", "ơ", "ớ", "ợ", "ờ", "ỡ", "ô", "ồ", "ố", "ộ", "ỗ" ],
                "e": ["é", "è", "ẹ", "ẽ", "ê", "ế", "ề", "ễ", "ệ"], 
                "u": ["ú", "ù", "ũ", "ụ", "ư", "ứ", "ừ", "ự", "ữ"], 
                "i": ["í", "ì", "ị", "ĩ"],
                "y": ["ý", "ỵ", "ỳ", "ỹ"],
                "d": ["đ"]
               }
        # Chuyen doi chu cai co dau -> chu cai khong dau 
        name.lower( )
        for i in range (len(name)) : 
            flag = False 
            for j in result : 
                if ( name[i] == j ) : 
                    new+= name[i]
                    flag = True 
                    break 
                if (name[i] in result[j]): 
                    new+=j 
                    flag = True 
                    break 
            if flag == False : 
                new+= name[i]
        return new.lower()
    
    def exception_name(self, name ) :
        for i in name : 
            if(ord(i) not in range (65, 90)): 
                print ( i)
                return False 
        return True 
    
    
    def set_firtname (self, first_name) :
        new = self.set_name(first_name) 
        if (self.exception_name(new)) : 
            return first_name 
        else : 
            raise ValueError("error")
        
    
    def Check_Infor (self, first_name, last_name, email, user_name, pass_word ) : 
        
        self.first_name = self.set_firtname(first_name)
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.pass_word = pass_word 
        
        flag = False 
        for infor in data : 
                if(self.email == infor[2] or self.user_name == infor[3]) : 
                    flag = True 
                    print ("THis account is exsits")
                    break 
        if (flag == False ) : 
            data_tuple = (self.first_name, self.last_name, self.email, self.user_name, self.pass_word)
            cursor.execute(query_insert, data_tuple )
            conn.commit( )
        

user = User_Infor() 
# user.Check_Infor('Dung', 'Tran', 'dung@gmail.com', 'dung1', '12345')
# print (user.set_name("Dũng"))
print (user.exception_name(user.set_name("Dũng")))
            
# cursor.execute(query) 
# data = cursor.fetchall( )
# print (data)
       
        

conn.close()
        
        

