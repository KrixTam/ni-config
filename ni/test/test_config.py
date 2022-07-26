import os
import unittest
from ni.config import Config
from ni.config.config import replace

cwd = os.path.abspath(os.path.dirname(__file__))
test_config_filename = os.path.join(cwd, 'sources', 'config')


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
        self.assertEqual(c.load('config.cfg'), c.load(os.path.join(cwd, 'sources', 'config.default.cfg')))
        dump_filename = 'config_dump.cfg'
        c.dump(dump_filename)
        self.assertEqual(c.load('config.cfg'), c.load(dump_filename))

    def test_error_dump(self):
        c = Config(test_config_filename)
        c._value['output'] = 123
        with self.assertRaises(AssertionError):
            c.dump()

    def test_is_default(self):
        c = Config(test_config_filename)
        self.assertTrue(c.is_default())
        self.assertTrue(c.is_default(['base', 'key']))
        c['base']['name'] = '123'
        self.assertFalse(c.is_default('base'))
        self.assertFalse(c.is_default(['base', 'name']))

    def test_error_is_default_01(self):
        c = Config(test_config_filename)
        with self.assertRaises(ValueError):
            c.is_default([])

    def test_error_is_default_02(self):
        c = Config(test_config_filename)
        with self.assertRaises(TypeError):
            c.is_default({})

    def test_error_replace(self):
        a = 123
        b = []
        with self.assertRaises(TypeError):
            replace(a, b)

    def test_error_init(self):
        with self.assertRaises(TypeError):
            Config(['123'])

    def test_error_load(self):
        self.assertEqual(None, Config.load('abcdefg.123'))

    def test_error_get(self):
        c = Config(test_config_filename)
        with self.assertRaises(KeyError):
            c['123']

    def test_error_set(self):
        c = Config(test_config_filename)
        with self.assertRaises(ValueError):
            c['output'] = 123

    def test_contain(self):
        c = Config(test_config_filename)
        self.assertTrue('output' in c)

    def test_repr(self):
        c = Config(test_config_filename)
        self.assertEqual(c.__repr__(), "{'base': {'name': 'base_filename', 'key': 'key_field'}, 'output': 'output_filename', 'tags': [{'name': 'base_filename', 'key': 'key_field', 'fields': [{'field': 'A', 'default': 'default value of field A'}, {'field': 'B', 'default': 'default value of field B'}]}]}")

    def test_init(self):
        config_filename = os.path.join(cwd, 'sources', 'config.desc')
        cfg = Config.load(config_filename)
        c = Config(cfg)
        self.assertEqual(c.__repr__(), "{'base': {'name': 'base_filename', 'key': 'key_field'}, 'output': 'output_filename', 'tags': [{'name': 'base_filename', 'key': 'key_field', 'fields': [{'field': 'A', 'default': 'default value of field A'}, {'field': 'B', 'default': 'default value of field B'}]}]}")

    def test_load_config_01(self):
        c = Config(test_config_filename)
        self.assertTrue(c.is_default())
        config_filename = os.path.join(cwd, 'sources', 'config.cfg')
        c.load_config(config_filename)
        self.assertFalse(c.is_default())
        self.assertEqual(c['tags'][0]['name'], 'config.abc')

    def test_load_config_02(self):
        c = Config(test_config_filename)
        self.assertTrue(c.is_default())
        c.load_config('config_filename_1231232121')
        self.assertTrue(c.is_default())

    def test_error_set_02(self):
        c = Config(test_config_filename)
        self.assertTrue(c.is_default())
        config_filename = os.path.join(cwd, 'sources', 'config_err.cfg')
        with self.assertRaises(ValueError):
            c.load_config(config_filename)

    def test_empty_dict(self):
        c = Config({
            'name': 'CSVFileElf',
            'default': {
                'add': {
                    'base': {
                        'name': 'base_filename',
                        'key': 'key_field',
                        'drop_duplicates': False,
                    },
                    'output': {
                        'name': 'output_filename',
                        'BOM': False,
                        'non-numeric': []
                    },
                    'tags': [
                        {
                            'name': 'tags_filename',
                            'key': 'key_field',
                            'fields': ['field A', 'field B'],
                            'defaults': ['default value of field A', 'default value of field B']
                        }
                    ]
                },
                'merge': {
                    'input': ['input_filename_01', 'input_filename_02'],
                    'output': {
                        'name': 'output_filename',
                        'BOM': False,
                        'non-numeric': []
                    },
                    'on': ['field_name'],
                    'mappings': {}
                }
            },
            'schema': {
                'type': 'object',
                'properties': {
                    'add': {
                        'type': 'object',
                        'properties': {
                            'base': {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string'},
                                    'key': {'type': 'string'},
                                    'drop_duplicates': {'type': 'boolean'}
                                }
                            },
                            'output': {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string'},
                                    'BOM': {'type': 'boolean'},
                                    'non-numeric': {
                                        'type': 'array',
                                        'items': {'type': 'string'}
                                    }
                                }
                            },
                            'tags': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'name': {'type': 'string'},
                                        'key': {'type': 'string'},
                                        'fields': {
                                            'type': 'array',
                                            'items': {'type': 'string'}
                                        },
                                        'defaults': {
                                            'type': 'array',
                                            'items': {'type': 'string'}
                                        }
                                    }
                                },
                                'minItems': 1
                            }
                        }
                    },
                    'merge': {
                        'type': 'object',
                        'properties': {
                            'input': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'minItems': 2
                            },
                            'output': {
                                'type': 'object',
                                'properties': {
                                    'prefix': {'type': 'string'},
                                    'BOM': {'type': 'boolean'},
                                    'non-numeric': {
                                        'type': 'array',
                                        'items': {'type': 'string'}
                                    }
                                }
                            },
                            'on': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'minItems': 1
                            },
                            'mappings': {'type': 'object'}
                        }
                    }
                }
            }
        })
        config = {
            'output': {
                'name': 'merge_01.csv',
                'BOM': False,
                'non-numeric': []
            },
            'on': ['生效日期', '基金代码'],
            'mappings': {'权益登记日': '生效日期', '拆分折算日': '生效日期'}
        }
        c['merge'] = config
        self.assertEqual(c['merge']['mappings'], config['mappings'])


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
