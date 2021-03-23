from kamene.all import *


class QYTPING():
    def __init__(self, ip):
        self.dip = ip
        self.sip = None
        self.length = 100

    def one(self):
        ping_result = sr1(IP(dst=self.dip) / ICMP() / (b'v' * self.length), timeout=2, verbose=False)
        try:
            if ping_result.getlayer(IP).fields['src'] == self.dip and ping_result.getlayer(ICMP).fields['type'] == 0:
                print(str(self.dip) + ' 可达！')
            else:
                print(str(self.dip) + ' 不可达！')
        except Exception:
            print(str(self.dip) + ' 不可达！')

    def ping(self):
        for i in range(5):
            if self.sip:
                ping_result = sr1(IP(src=self.sip, dst=self.dip) / ICMP() / (b'v' * self.length), timeout=2,
                                  verbose=False)
            else:
                ping_result = sr1(IP(dst=self.dip) / ICMP() / (b'v' * self.length), timeout=2, verbose=False)
            try:
                if ping_result.getlayer(IP).fields['src'] == self.dip and ping_result.getlayer(ICMP).fields[
                    'type'] == 0:
                    print("!", end='', flush=True)
                else:
                    print(".", end='', flush=True)
            except Exception:
                print(".", end='', flush=True)
        print()

    def __str__(self):
        if self.sip:
            return '<%s => srcip: %s, dstip: %s, size: %d>' % (self.__class__.__name__, self.sip, self.dip, self.length)
        else:
            return '<%s => dstip: %s, size: %d>' % (self.__class__.__name__, self.dip, self.length)


class NewPing(QYTPING):
    def ping(self):
        for i in range(5):
            if self.sip:
                ping_result = sr1(IP(src=self.sip, dst=self.dip) / ICMP() / (b'v' * self.length), timeout=2,
                                  verbose=False)
            else:
                ping_result = sr1(IP(dst=self.dip) / ICMP() / (b'v' * self.length), timeout=2, verbose=False)
            try:
                if ping_result.getlayer(IP).fields['src'] == self.dip and ping_result.getlayer(ICMP).fields[
                    'type'] == 0:
                    print("+", end='', flush=True)
                else:
                    print("?", end='', flush=True)
            except Exception:
                print("?", end='', flush=True)
        print()


def print_new(word, s='-'):
    print('{0}{1}{2}'.format(s * int((70 - len(word)) / 2), word, s * int((70 - len(word)) / 2)))


if __name__ == '__main__':
    ping = QYTPING('192.168.0.1')
    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    ping.one()
    print_new('ping five')
    ping.ping()
    print_new('set playload lenth')
    ping.length = 200
    print(ping)
    ping.ping()
    print_new('set ping src ip address')
    ping.sip = '192.168.0.88'
    print(ping)
    ping.ping()
    print_new('new class NewPing', '=')
    new_ping = NewPing('192.168.0.1')
    new_ping.length = 300
    print(new_ping)
    new_ping.ping()
