import Data.Data_Base
import Data.Collector
from flask import Flask, render_template, request, redirect, url_for, send_file
from Data.Utils.utils import MASSAGE


app = Flask(__name__, template_folder='Data/html/templates', static_folder='Data/html/static')

@app.route('/', methods=['POST', 'GET'])
def data_web():
    if request.method == 'POST':
        table = request.form.get('table')
        tables = Data.Data_Base.get_tables_name()
        print(table)
        file = Data.Data_Base.load_db_into_list(table)
        massage = Data.Data_Base.get_time_modify()
        return render_template('home.html', SCORES=file, TABLES=tables, LER=massage)
    else:

        file = Data.Data_Base.load_db_into_list('Printers')
        tables = Data.Data_Base.get_tables_name()
        massage = Data.Data_Base.get_time_modify()
        return render_template('home.html', SCORES=file, TABLES=tables, LER=massage)
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
        Data.Data_Base.edit_count(new_printer[2], Data.Collector.get_count([new_printer[1], new_printer[2]]))
        tables = Data.Data_Base.get_tables_name()
        file = Data.Data_Base.load_db_into_list('Printers')
        return render_template('home.html', SCORES=file, TABLES=tables)
    else:
        return render_template('add.html')

@app.route('/download')
def download_file():
    path = Data.Data_Base.export_to_csv('Printers')

    return send_file(path, as_attachment=True)
@app.route('/drivers', methods=['POST'])
def download_file1():
    if request.method == 'POST':
        button_value = request.form['driver']
        if '5330' in button_value:
            path = 'Data\\Drivers\\Brother J5330DW Driver.EXE'
            return send_file(path, as_attachment=True)
        elif '2710' in button_value:
            path = 'Data\\Drivers\\Brother L2710DN Driver.EXE'
            return send_file(path, as_attachment=True)
        elif 'Samsung' in button_value:
            path = 'Data\\Drivers\\Samsung Diagnostic.exe'
            return send_file(path, as_attachment=True)
        elif '8950' in button_value:
            path = 'Data\\Drivers\\Brother-MFC-8950DW.EXE'
            return send_file(path, as_attachment=True)
        elif '5799' in button_value:
            path = 'Data\\Drivers\\EPSON WF-M5799.exe'
            return send_file(path, as_attachment=True)
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)
