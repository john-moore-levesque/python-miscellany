import json
import urllib.request
import socket


class Whois():
    def __init__(self, configpath="config.json"):
        self.apikey = self._getApiKey(configpath)

    def _getApiKey(self, configpath="config.json"):
        jsondata = {}
        with open(configpath, 'r') as jfile:
            jsondata = json.load(jfile, encoding='utf-8')
        try:
            return jsondata["whois"]["apikey"]
        except KeyError:
            return False

    def whoisLookup(self, domain, format="JSON"):
        api = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=%s&domainName=%s&outputFormat=%s" %(self.apikey, domain, format)
        data = urllib.request.urlopen(api).read().decode('utf-8')
        return json.loads(data)['WhoisRecord']

    def dnsLookup(self, ip):
        api = "https://reverse-ip-api.whoisxmlapi.com/api/v1?apiKey=%s&ip=%s" %(self.apikey, ip)
        data = urllib.request.urlopen(api).read().decode('utf-8')
        return json.loads(data)

    def getIP(self, domain):
        return socket.getaddrinfo("%s" %(domain), 0)[0][-1][0]

    def basicInfo(self, domain):
        ip = self.getIP(domain)
        who = self.whoisLookup(domain)
        created = who['createdDate']
        updated = who['updatedDate']
        expires = who['expiresDate']
        return (domain, ip), {"created": created, "updated": updated, "expires": expires}

    def outputInfo(self, domain):
        header, info = self.basicInfo(domain)
        print("Information for %s (%s)" %(header[0], header[1]))
        print("{")
        for k, v in info.items():
            print("\t%s: %s" %(k, v))
        print("}")

def test():
    testWhois = Whois()
    testWhois.outputInfo("google.com")


if __name__ == '__main__':
    test()
