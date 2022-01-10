import os
import unittest
from ni.config import Config

cwd = os.path.abspath(os.path.dirname(__file__))
test_config_filename = os.path.join(cwd, 'config')


class TestConfig(unittest.TestCase):

    def test_all(self):
        c = Config(test_config_filename)
        self.assertTrue(c.validate())

    def test_set_error(self):
        c = Config(test_config_filename)
        with self.assertRaises(KeyError):
            c['abc'] = 123

    def test_get_set(self):
        c = Config(test_config_filename)
        d = {'name': 'base_filename', 'key': 'key_field'}
        self.assertEqual(c['base'], d)
        c['base'] = {'name': '123'}
        self.assertNotEqual(c['base'], d)
        self.assertTrue(c.validate())
        c['base']['name'] = 123
        self.assertFalse(c.validate())

    def test_dump(self):
        c = Config(test_config_filename)
        c.dump()
        self.assertEqual(c.load('config.cfg'), c.load(os.path.join(cwd, 'config.default.cfg')))

    def test_is_default(self):
        c = Config(test_config_filename)
        self.assertTrue(c.is_default())
        self.assertTrue(c.is_default(['base', 'key']))
        c['base']['name'] = '123'
        self.assertFalse(c.is_default('base'))
        self.assertFalse(c.is_default(['base', 'name']))


if __name__ == '__main__':
    unittest.main()
