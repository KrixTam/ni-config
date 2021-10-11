# coding: utf-8

import unittest
from ni.config import EncryptionConfig, EasyCodec, Config
import os


def set_error():
    c = EncryptionConfig('cr-config', EasyCodec('key.dat'))
    c['abc'] = 123


class TestEncryptionConfig(unittest.TestCase):

    def test_all(self):
        c = EncryptionConfig('cr-config', EasyCodec('key.dat'))
        self.assertTrue(c.validate())

    def test_set_error(self):
        with self.assertRaises(Exception) as context:
            set_error()
        self.assertTrue(isinstance(context.exception, KeyError))

    def test_get_set(self):
        c = EncryptionConfig('cr-config', EasyCodec('key.dat'))
        d = {'name': 'base_filename', 'key': 'key_field'}
        self.assertEqual(c['base'], d)
        c['base'] = {'name': '123'}
        self.assertNotEqual(c['base'], d)
        self.assertTrue(c.validate())
        c['base']['name'] = 123
        self.assertFalse(c.validate())

    def test_dump(self):
        ec = EncryptionConfig('cr-config', EasyCodec('key.dat'))
        ec.dump()
        c = Config('config')
        self.assertEqual(ec._load(os.path.join(os.getcwd(), 'cr-config.cfg')), c._load(os.path.join(os.getcwd(),
                                                                                                    'config.default.cfg')))

    def test_is_default(self):
        c = EncryptionConfig('cr-config', EasyCodec('key.dat'))
        self.assertTrue(c.is_default())
        self.assertTrue(c.is_default(['base', 'key']))
        c['base']['name'] = '123'
        self.assertFalse(c.is_default('base'))
        self.assertFalse(c.is_default(['base', 'name']))


if __name__ == '__main__':
    unittest.main()
