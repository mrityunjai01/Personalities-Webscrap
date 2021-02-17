from flask import Flask, render_template, request, send_from_directory, redirect, jsonify
from personality_check import check
import os
import multiprocessing
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/get_answers', methods = ["POST"])
def get_ans():
    personality_input = request.form.get("personality_input")
    res = pool.apply_async(check, (personality_input,))
    try:
        return res.get(timeout=8), 200
    except TimeoutError:
        return jsonify({
            "msg": "Timeout, your request took just too much time"
        }), 500
    # print("1")
    # queue = Queue()
    # print("2")
    # p = Process(target=check, args=(personality_input,))
    # print("3")
    # p.start()
    # print("4")
    # p.join() # this blocks until the process terminates
    # print("5")
    # outfile = queue.get()
    # print("6")
    # print("the outfile is "+outfile)
@app.route('/download_page/<outfile>')
def download_page(outfile):
    return render_template('download.html', outfile_d = "po"+outfile, outfile_l = "link_"+outfile)
@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    download_folder = os.path.join(app.root_path, 'data')
    return send_from_directory(directory=download_folder, filename=filename)
# @app.route('/download_page', methods=['GET', 'POST'])
# def download(filename):
#     return render_template('download.html', )

from os import environ
pool = multiprocessing.Pool(processes = 5)
app.run (port = environ.get("PORT", 5050), debug = True)
