import pg8000
from flask import request,redirect 
from flask import Blueprint 
from flask import render_template

authentication_bp=Blueprint(
"auth",__name__
)

@authentication_bp.route(
"/user_statement",
methods=["GET","POST"]
)

def user_statement():
    if request.method == "POST":                            

        answer = request.form["answer"]
        
        

        if answer == "Yes":
            

            return redirect("/old_user_login")

        elif answer == "No":

            return redirect ("/new_user_login")
            
    return render_template(
    "user_statement.html"
    )
    
    
@authentication_bp.route("/old_user_login",methods=["GET","POST"])
def old_user_login():
    
    if request.method=="POST":
        profile_name = request.form["profile_name"]
        profile_pass = request.form["profile_pass"]

        # search Neon database here
        conn = pg8000.connect(
    host="YOUR_HOST",
    database="neondb",
    user="neondb_owner",
    password="YOUR_PASSWORD",
    ssl_context=True
)

        cursor = conn.cursor()

        cursor.execute(
        """
        SELECT *
        FROM users
        WHERE profile_name=%s
        AND profile_pass=%s
        """,
        (profile_name, profile_pass))

        user = cursor.fetchone()

        conn.close()
        

    if user:

        return redirect("/user_account")

    else:

        return redirect("/new_user_login")
    return render_template("old_user_login.html")
    
    
@authentication_bp.route("/new_user_login",methods=["GET","POST"])
def new_user_login():
    
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]                    

        return redirect(
            "/create_profile"
        )
    return render_template("new_user_login.html")
    
    
@authentication_bp.route(
    "/create_profile",
    methods=["GET","POST"]
)
def create_profile():

    if request.method == "POST":

        profile_name = request.form["profile_name"]
        profile_pass = request.form["profile_pass"]

        conn = pg8000.connect(
            host="ep-calm-boat-atwdggmw-pooler.c-9.us-east-1.aws.neon.tech",
            database="neondb",
            user="neondb_owner",
            password="npg_FXjK9qn7owLN",
            ssl_context=True
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (profile_name, profile_pass)
            VALUES (%s, %s)
            """,
            (profile_name, profile_pass)
        )

        conn.commit()
        conn.close()

        return redirect("/final_page")

    return render_template(
        "create_profile.html"
    )
    
@authentication_bp.route("/final_page")
def final_page():

    return "Account Created Successfully"

    
    
    
