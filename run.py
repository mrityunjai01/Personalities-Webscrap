from flask_code import app
import multiprocessing
if __name__ == '__main__':
    from os import environ
    pool = multiprocessing.Pool(processes = 5)
    app.run (port = environ.get("PORT", 5050), debug = True)
