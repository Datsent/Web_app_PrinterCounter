from Data import Data_Base, Report

def main():
    Data_Base.set_offline_printer('10.1.2.180')
    Report.send_mail()
    Data_Base.copy_table()
    Data_Base.reset_counter()
if __name__ == '__main__':
    main()