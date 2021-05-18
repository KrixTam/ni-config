# coding: utf-8

import unittest
from config import config
import hashlib
import os


def set_error():
    c = config('config')
    c['abc'] = 123


def checksum(filename):
    # https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
    # Note: hash_md5.hexdigest() will return the hex string representation for the digest, if you just need the packed bytes use return hash_md5.digest(), so you don't have to convert back.
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class TestConfig(unittest.TestCase):

    def test_all(self):
        c = config('config')
        self.assertTrue(c.validate())

    def test_set_error(self):
        with self.assertRaises(Exception) as context:
            set_error()
        self.assertTrue(isinstance(context.exception, KeyError))

    def test_get_set(self):
        c = config('config')
        d = {'name': 'base_filename', 'key': 'key_field'}
        self.assertEqual(c['base'], d)
        c['base']['name'] = '123'
        self.assertNotEqual(c['base'], d)
        self.assertTrue(c.validate())
        c['base']['name'] = 123
        self.assertFalse(c.validate())

    def test_dump(self):
        c = config('config')
        c.dump()
        self.assertEqual(checksum(os.path.join(os.getcwd(), 'config.cfg')), checksum(os.path.join(os.getcwd(), 'config.default.cfg')))


if __name__ == '__main__':
    unittest.main()
