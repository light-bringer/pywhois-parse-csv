import ipwhois
import datetime
from warnings import filterwarnings
filterwarnings(action="ignore")
import csv, os

def getwhoisdict(IPAddr):
    '''
    getting whois Dict
    '''
    obj = ipwhois.IPWhois(IPAddr)
    res = obj.lookup_rdap(asn_methods=["whois"])
    return res


def writetocsv(mydictlist, headers):
    ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    csvdir = "output"
    csvfile = "output_ipaddr" + str(ts) + ".csv"
    csvpath = os.path.join(csvdir, csvfile)

    with open(csvpath, "wb") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for mydict in mydictlist:
            print mydict
            writer.writerow(mydict)


# print getwhoisdict('1.210.22.66')
mynewdictlist = [{'a':1, 'b':"mystring"}, {'a':7, 'b':"mynewstring"}, {'a':7667, 'b':"mystring12344"}]
headers = ['a', 'b']
print writetocsv(mynewdictlist, headers)

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(getwhoisdict('1.1.1.1'))
