from flask import Flask 

from home_page import home_bp

from auth_page import authentication_bp


server = Flask(__name__)

server.register_blueprint(home_bp)

server.register_blueprint(authentication_bp)


if __name__ == "__main__":

    server.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
