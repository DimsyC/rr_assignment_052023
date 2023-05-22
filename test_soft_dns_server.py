import unittest
import tldextract
from soft_dns_server import SoftDnsServer
from validators import url, ipv4

class SoftDnsServerTestCase(unittest.TestCase):
    def setUp(self):
        self.test_cache = {
            "google.com": "172.217.1.110",
            "yahoo.com": "74.6.231.21",
            "nhl.com": "104.18.17.236",
            "python.org": "151.101.193.168"
        }

        self.server = SoftDnsServer(self.test_cache)

    def test_register(self):
        url = 'amazon.com'
        ip = '176.32.103.205'
        self.server.register(url, ip)

        # Check the url is registered in the cache
        result = self.server.cache[url]
        self.assertEqual(result, ip)

    def test_resolve_exists_in_cache(self):
        for url, ipv4 in self.test_cache.items():

            # test for URL to IPv4 resolution
            result = self.server.resolve(url)
            self.assertEqual(result, ipv4)

            # test for IPv4 to URL resolution
            result = self.server.resolve(ipv4)
            self.assertEqual(result, url)

    def test_resolve_not_in_cache(self):
        # https://youtube.com is not in test_cache
        url_not_in_cache = 'https://youtube.com'

        # 31.13.72.36 is not in cache and belongs to Facebook
        ip_not_in_cache = '31.13.72.36'

        # test for URL to IPv4 resolution
        result = self.server.resolve(url_not_in_cache)
        self.assertTrue(ipv4(result))

        # test for IPv4 to URL resolution
        url = self.server.resolve(ip_not_in_cache)
        result = tldextract.extract(url).registered_domain
        self.assertEqual(result, 'facebook.com')


if __name__ == '__main__':
    unittest.main()
