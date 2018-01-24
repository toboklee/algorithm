import unittest
import random


ENCODABLES = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
DOMAIN = 'http://tinyurl.com/'


class Codec:
    def __init__(self):
        # Each Dict used for encoding and decoding respectively
        self.urls, self.codes = {}, {}

    def encode(self, long_url):
        if long_url not in self.urls:

            # 6 letter encoding
            code = self.code_generator()

            if code not in self.codes:
                # Set in both dict in order to keep record and decode later.
                self.codes[code] = long_url
                self.urls[long_url] = code

            return ''.join([DOMAIN, self.urls[long_url]])

    def decode(self, short_url):
        # Only last 6 characters should be a code.
        code = short_url[-6:]

        try:
            return self.codes[code]
        except KeyError:
            raise KeyError("Code is not available")

    @staticmethod
    def code_generator():
        return ''.join([random.choice(ENCODABLES) for _ in xrange(6)])


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def runTest(self):
        url = "http://www.google.com"
        self.assertEqual(self.codec.decode(self.codec.encode(url)), url)


if __name__ == '__main__':
    unittest.main()
