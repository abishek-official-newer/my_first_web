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
        hello this is official home page our developer (abishek)will make it too intresting and useful within 1 month 
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
        <h2>You can use this for your "About Our Website" section:


---

About Our Website

Welcome to our website!

This website was created with the goal of providing users with a simple, reliable, and user-friendly experience. We are committed to delivering quality content, useful information, and continuous improvements to meet the needs of our visitors.

The owner and developer of this website is Abishek, who is passionate about technology, learning, and web development. This platform reflects his dedication to creating helpful digital solutions and enhancing user experiences.

We believe in professionalism, honesty, and innovation. Our mission is to make information easily accessible while maintaining a secure, efficient, and well-organized environment for all users.

Thank you for visiting our website and being a part of our journey. Your support and feedback help us grow and improve every day.

Owner: Abishek
Website Founder & Developer


---

This version looks professional, disciplined, and suitable for a personal or project website. </h2>
<br><br>
<h2YOURS TRUELY; ABISHEK</h2>
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

        
