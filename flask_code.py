from flask import Flask, render_template, request, send_from_directory, redirect
from personality_check import check
from multiprocessing import Queue, Process
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/get_answers', methods = ["POST"])
def get_ans():
    personality_input = request.form.get("personality_input")
    queue = Queue()
    p = Process(target=check, args=(personality_input,))
    p.start()
    p.join() # this blocks until the process terminates
    outfile = queue.get()
    return redirect(url_for(download_page)+"/"+outfile)
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
