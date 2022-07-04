import os
import unittest
from ni.config import EncryptionConfig, EasyCodec, Config

cwd = os.path.abspath(os.path.dirname(__file__))
test_filename = os.path.join(cwd, 'sources', 'key.dat')
test_config_filename = os.path.join(cwd, 'sources', 'config')
test_cr_config_filename = os.path.join(cwd, 'sources', 'cr-config')


class TestEncryptionConfig(unittest.TestCase):

    def test_all(self):
        c = EncryptionConfig(test_cr_config_filename, EasyCodec(test_filename))
        self.assertTrue(c.validate())

    def test_set_error(self):
        c = EncryptionConfig(test_cr_config_filename, EasyCodec(test_filename))
        with self.assertRaises(KeyError):
            c['abc'] = 123

    def test_get_set(self):
        c = EncryptionConfig(test_cr_config_filename, EasyCodec(test_filename))
        d = {'name': 'base_filename', 'key': 'key_field'}
        self.assertEqual(c['base'], d)
        c['base'] = {'name': '123'}
        self.assertNotEqual(c['base'], d)
        self.assertTrue(c.validate())
        c['base']['name'] = 123
        self.assertFalse(c.validate())

    def test_dump(self):
        ec = EncryptionConfig(test_cr_config_filename, EasyCodec(test_filename))
        ec.dump()
        c = Config(test_config_filename)
        self.assertEqual(ec._load(os.path.join(os.getcwd(), 'cr-config.cfg')), c._load(os.path.join(cwd, 'sources', 'config.default.cfg')))

    def test_is_default(self):
        c = EncryptionConfig(test_cr_config_filename, EasyCodec(test_filename))
        self.assertTrue(c.is_default())
        self.assertTrue(c.is_default(['base', 'key']))
        c['base']['name'] = '123'
        self.assertFalse(c.is_default('base'))
        self.assertFalse(c.is_default(['base', 'name']))

    def test_load_config(self):
        c = EncryptionConfig(test_cr_config_filename, EasyCodec(test_filename))
        self.assertTrue(c.is_default())
        c.load_config('config_filename_1231232121')
        self.assertTrue(c.is_default())


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
