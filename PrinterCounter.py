from Data import Data_Base, Collector, Report

from Data.Utils import utils

def main():
    list = Data_Base.addresses_list()
    print(list)
    for printer in list:
        print(f'Calculating Model: {printer[0]} on {printer[1]}...')
        if printer[1] != '10.1.2.180':
            if Collector.myping(printer[1]) is True:
                try:
                    Data_Base.edit_count(printer[1], Collector.get_count(printer))
                    Data_Base.status(printer[1], 'V')
                    print(f'Finished: {printer[0]} on {printer[1]}')
                except:
                    Data_Base.status(printer[1], '!')
                    print(f'Problem with {printer[1]}')
            else:
                Data_Base.status(printer[1], '/')
                Report.send_err_mail(printer[1], printer[0])
        else:
            print(f'Printer {printer[1]} is offline. Add automatically 350 pages')
            Data_Base.status(printer[1], '!')


if __name__ == '__main__':
    main()
