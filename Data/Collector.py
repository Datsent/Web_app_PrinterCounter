import os
from Data.Models import Brother, Epson, Samsung

def myping(host):
    response = os.system("ping -n 1 " + host)
    if response == 0:
        return True
    else:
        return False
def get_count(printer):
    '''
    Call specific function to get data.
    '''
    if check_printer(printer[0]) == 'Brother':
        return Brother.brother(printer[1])
    elif check_printer(printer[0]) == 'Epson':
        return Epson.epson(printer[1])
    elif check_printer(printer[0]) == 'Samsung':
        return Samsung.samsung(printer[1])
    else:
        pass

def check_printer(model):
    '''
    Check kind\model of printer.
    '''
    if 'brother' in model.lower():
        return 'Brother'
    elif 'epson' in model.lower():
        return 'Epson'
    elif 'samsung' in model.lower():
        return 'Samsung'
    else:
        pass