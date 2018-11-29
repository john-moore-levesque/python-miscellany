import socket
import json


class SocketTester():
    def __init__(self, domain):
        self.domain = domain

    def getPorts(self):
        portfile = "ports.json"
        ports = {}
        jports = {}
        with open(portfile, 'r') as pfile:
            jports = json.load(pfile, encoding='utf-8')['ports']
        for port in jports:
            if 0 < int(port) < 1023:
                ports[port] = jports[port]
            else:
                pass
        return ports

    def checkPort(self, port, time=0.25):
        try:
            return socket.create_connection((self.domain, port), time)
        except socket.timeout:
            return False
        except OSError:
            print(self.domain)
            print(port)

    def portscan(self, portfile="ports.json"):
        ports = self.getPorts()
        validports = {}
        for port in ports:
            if self.checkPort(int(port), time=0.25):
                validports[port] = ports[port]
            else:
                pass
        return validports


def test():
    tester = SocketTester("www.example.com")
    ports = tester.portscan()
    return ports


if __name__ == '__main__':
    print("Testing www.example.com")
    ports = test()
    print("Valid ports:")
    for port in ports.keys():
        print("port: %s" %(port))
