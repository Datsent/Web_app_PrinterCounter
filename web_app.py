import Data.Data_Base

from flask import Flask, render_template, request, redirect, url_for, send_file


app = Flask(__name__, template_folder='Data/html/templates', static_folder='Data/html/static')

@app.route('/', methods=['POST', 'GET'])
def data_web():
    if request.method == 'POST':
        table = request.form.get('table')
        tables = Data.Data_Base.get_tables_name()
        print(table)
        file = Data.Data_Base.load_db_into_list(table)
        return render_template('home.html', SCORES=file, TABLES=tables)
    else:

        file = Data.Data_Base.load_db_into_list('Printers')
        tables = Data.Data_Base.get_tables_name()
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
        tables = Data.Data_Base.get_tables_name()
        file = Data.Data_Base.load_db_into_list('Printers')
        return render_template('home.html', SCORES=file, TABLES=tables)
    else:
        return render_template('add.html')

@app.route('/download')
def download_file():
    #Data.Data_Base.export_to_csv('Printers')
    path = Data.Data_Base.export_to_csv('Printers')

    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)
