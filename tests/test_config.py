# coding: utf-8

import unittest
from config import config
import hashlib
import os


def set_error():
    c = config('config')
    c['abc'] = 123


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
        self.assertEqual(c.load(os.path.join(os.getcwd(), 'config.cfg')), c.load(os.path.join(os.getcwd(), 'config.default.cfg')))

    def test_is_default(self):
        c = config('config')
        self.assertTrue(c.is_default())
        c['base']['name'] = '123'
        self.assertFalse(c.is_default('base'))


if __name__ == '__main__':
    unittest.main()
