import ipwhois
from warnings import filterwarnings
filterwarnings(action="ignore")


def getwhoisdict(IPAddr):
    '''
    getting whois Dict
    '''
    obj = ipwhois.IPWhois(IPAddr)
    res = obj.lookup_rdap(asn_methods=["whois"])
    return res



print getwhoisdict('1.210.22.66')
