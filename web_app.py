from Data.Data_Base import load_db_into_list
from flask import Flask, render_template


app = Flask(__name__, template_folder='Data/html/templates', static_folder='Data/html/static')

@app.route('/')
def data_web():
    file = load_db_into_list()
    return render_template('home.html', SCORES=file)



if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)
