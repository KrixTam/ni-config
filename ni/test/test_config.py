import os
import unittest
from ni.config import Config


class TestConfig(unittest.TestCase):

    def test_all(self):
        c = Config('config')
        self.assertTrue(c.validate())

    def test_set_error(self):
        c = Config('config')
        with self.assertRaises(KeyError):
            c['abc'] = 123

    def test_get_set(self):
        c = Config('config')
        d = {'name': 'base_filename', 'key': 'key_field'}
        self.assertEqual(c['base'], d)
        c['base'] = {'name': '123'}
        self.assertNotEqual(c['base'], d)
        self.assertTrue(c.validate())
        c['base']['name'] = 123
        self.assertFalse(c.validate())

    def test_dump(self):
        c = Config('config')
        c.dump()
        self.assertEqual(c.load(os.path.join(os.getcwd(), 'config.cfg')), c.load(os.path.join(os.getcwd(), 'config.default.cfg')))

    def test_is_default(self):
        c = Config('config')
        self.assertTrue(c.is_default())
        self.assertTrue(c.is_default(['base', 'key']))
        c['base']['name'] = '123'
        self.assertFalse(c.is_default('base'))
        self.assertFalse(c.is_default(['base', 'name']))


if __name__ == '__main__':
    unittest.main()
