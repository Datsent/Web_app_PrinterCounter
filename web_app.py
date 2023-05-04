from Data.Utils import utils
from flask import Flask, render_template

app = Flask(__name__, template_folder='Data/html/templates', static_folder='Data/html/static')

@app.route('/')
def data_web():
    file = [("1", "2", "3"),]
    return render_template('home.html')



if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)
