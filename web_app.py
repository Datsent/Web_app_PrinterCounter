import Data.Data_Base
from Data.Data_Base import load_db_into_list
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, template_folder='Data/html/templates', static_folder='Data/html/static')

@app.route('/', methods=['POST', 'GET'])
def data_web():
    if request.method == 'POST':
        tables = request.form.get('table')
        print(tables)
        file = load_db_into_list()
        tables = ['Printer']
        return render_template('home.html', SCORES=file, TABLES=tables)
    else:
        file = load_db_into_list()
        tables = ['Printer']
        return render_template('home.html', SCORES=file, TABLES=tables)
@app.route('/redirect')
def redirect_page():
    return redirect(url_for('data_web_post'))

@app.route('/add', methods=['POST', 'GET'])
def data_web_post():
    if request.method == 'POST':
        new_printer = [request.form.get('name'), request.form.get('model'), request.form.get('address'),
                       request.form.get('sup_date'), request.form.get('start_count'), request.form.get('last_count'),
                       request.form.get('count')]
        print(new_printer)
        Data.Data_Base.add_list_to_db(new_printer)
        file = load_db_into_list()
        return render_template('home.html', SCORES=file)
    else:
        return render_template('add.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)
