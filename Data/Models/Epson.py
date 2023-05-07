import urllib.request, ssl

def epson(ip_adress):
    '''
    Get Data from Epson printers by selenium.
    '''
    context = ssl._create_unverified_context()
    res = urllib.request.urlopen("https://%s/PRESENTATION/ADVANCED/INFO_MENTINFO/TOP" %ip_adress,
                  context=context)
    my_HTML = res.read().decode()
    x = my_HTML.find("Total Number of Pages&nbsp")
    y = my_HTML[x:].find("</div>")
    count = my_HTML[x:x + y].split('">')[2]
    return count

if __name__ == "__main__":
    print(epson('10.1.1.122'))


