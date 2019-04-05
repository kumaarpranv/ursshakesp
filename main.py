import warnings
warnings.filterwarnings("ignore")
from shakespeare_utils import *

from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    #generate_output()

@app.route("/post", methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        start=request.form['linestart']
        poem=generate_output(text=start)
        poemlis=poem.split('\n')
        return render_template('post.html', poemlis=poemlis)
    else:
        return render_template('index.html')
if __name__ == '__main__':
   app.run(debug = True)