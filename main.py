import ipwhois
import datetime
import ipaddress
import csv
import os

from warnings import filterwarnings
filterwarnings(action="ignore")



def validateIPAddr(IPAddr):
    retval = -1
    try:
        IP = ipaddress.ip_address(unicode(IPAddr))
        if IP:
            retval = 0
    except:
        print "Not a valid IP Address"

    return retval



def readIPAddr():
    inputdir = "input"
    inputfile = "IPADDR"
    inputfilepath = os.path.join(inputdir, inputfile)
    print inputfilepath
    with open(inputfilepath) as f:
        content = f.read().splitlines()
    IPArray = []
    for value in content:
        if validateIPAddr(value) == 0:
            IPArray.append(value)
    print IPArray
    return IPArray




def getwhoisdict(IPAddr):
    '''
    getting whois Dict
    '''
    print type(IPAddr)
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
    csv_file.close()


# print getwhoisdict('1.210.22.66')
mynewdictlist = [{'a':1, 'b':"mystring"}, {'a':7, 'b':"mynewstring"}, {'a':7667, 'b':"mystring12344"}]
#headers = ['a', 'b']
#print writetocsv(mynewdictlist, headers)

import pprint
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(getwhoisdict('1.1.1.1'))


def main():
    IPAddrList = readIPAddr()
    IPAddrDictList = []
    for IPAddr in IPAddrList:
        print IPAddr
        whoisinfodict = getwhoisdict(IPAddr)
        IPAddrDictList.append(whoisinfodict)

    headers = IPAddrDictList[0].keys()
    writetocsv(IPAddrDictList, headers)






