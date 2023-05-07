from Data import Data_Base, Collector
from Data.Utils import utils

def main():
    list = Data_Base.addresses_list()
    print(list)
    for printer in list:
        print(f'Calculating Model: {printer[0]} on {printer[1]}...')
        if Collector.myping(printer[1]) is True:
            Data_Base.edit_count(printer[1], Collector.get_count(printer))
            print(f'Finished: {printer[0]} on {printer[1]}')
        else:
            print('false')




if __name__ == '__main__':
    main()