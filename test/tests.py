import unittest
from ethplorer.address import Address

class TestAddressRequest(unittest.TestCase):

    ADDRESS = '0x48c80f1f4d53d5951e5d5438b54cba84f29f32a5'
    proxy = {'http': 'http://195.62.53.223:27194'}

    def test_get_address_info(self):
        r = Address(address=self.ADDRESS)
        self.assertEqual(r.get_address_info()['address'], self.ADDRESS)
        
    def test_get_address_info_proxy(self):
        r = Address(address=self.ADDRESS, proxies=self.proxy)
        self.assertEqual(r.get_address_info()['address'], self.ADDRESS)

if __name__ == '__main__':
    unittest.main()
