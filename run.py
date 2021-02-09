from flask_code import app

if __name__ == '__main__':
    from os import environ
    app.run (port = environ.get("PORT", 5050), debug = True)
