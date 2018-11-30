import json
import urllib.request
import socket


class Whois():
    def __init__(self, configpath="config.json"):
        self.apikey = self._getApiKey(configpath)

    def _getApiKey(self, configpath="config.json"):
        '''
        read configpath (default config.json) to get API key
        '''
        jsondata = {}
        with open(configpath, 'r') as jfile:
            jsondata = json.load(jfile, encoding='utf-8')
        try:
            return jsondata["whois"]["apikey"]
        except KeyError:
            return False

    def whoisLookup(self, domain, format="JSON"):
        '''
        Uses www.whoisxmlapi.com - register at https://whoisapi.whoisxmlapi.com/
           for a free API key
        '''
        api = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=%s&domainName=%s&outputFormat=%s" %(self.apikey, domain, format)
        data = urllib.request.urlopen(api).read().decode('utf-8')
        return json.loads(data)['WhoisRecord']

    def dnsLookup(self, ip):
        '''
        reverse nslookup
        '''
        api = "https://reverse-ip-api.whoisxmlapi.com/api/v1?apiKey=%s&ip=%s" %(self.apikey, ip)
        data = urllib.request.urlopen(api).read().decode('utf-8')
        return json.loads(data)

    def getIP(self, domain):
        '''
        get IP address for dnsLookup()
        '''
        return socket.getaddrinfo("%s" %(domain), 0)[0][-1][0]

    def geoLookup(self, ip):
        '''
        geolookup on ip address
        '''
        api = "https://geoipify.whoisxmlapi.com/api/v1?apiKey=%s&ipAddress=%s" %(self.apikey, ip)
        data = urllib.request.urlopen(api).read().decode('utf-8')
        return json.loads(data)

    def getReputation(self, domain):
        '''
        get reputation score for domain
        '''
        api = "https://domain-reputation-api.whoisxmlapi.com/api/v1?apiKey=%s&domainName=%s" %(self.apikey, domain)
        data = urllib.request.urlopen(api).read().decode('utf-8')
        return json.loads(data)

    def basicInfo(self, domain):
        '''
        return basic info about site
        '''
        ip = self.getIP(domain)
        who = self.whoisLookup(domain)
        geo = self.geoLookup(ip)
        reputation = self.getReputation(domain)
        info = {}
        try:
            info['created'] = who['createdDate']
        except KeyError:
            pass
        try:
            info['updated'] = who['updatedDate']
        except KeyError:
            pass
        try:
            info['expires'] = who['expiresDate']
        except KeyError:
            pass
        try:
            info['reputation'] = reputation['reputationScore']
        except KeyError:
            pass
        return (domain, ip), info, geo['location']

    def outputInfo(self, domain):
        '''
        nicely format basicInfo()
        '''
        header, info, geo = self.basicInfo(domain)
        print("Information for %s (%s)" %(header[0], header[1]))
        print("{")
        for k, v in info.items():
            print("\t%s: %s" %(k, v))
        print("\tlocation:")
        print("\t{")
        for k, v in geo.items():
            print("\t\t%s: %s" %(k, v))
        print("\t}")
        print("}")


def test(domain="example.com"):
    '''
    test with google.com
    '''
    testWhois = Whois()
    testWhois.outputInfo(domain)


if __name__ == '__main__':
    print("example.com")
    test()
    print("")
    print("")
    print("google.com")
    test("google.com")
