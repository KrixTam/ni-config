import unittest
from ni.config import ParameterValidator

schema = {
    'a': {"type": "string"},
    'b': {"type": ["number", "string"]},
    'c': {"type": "boolean"}
}
validator = ParameterValidator(schema)


class TestParameterValidator(unittest.TestCase):
    def test_default(self):
        self.assertTrue(validator.validates({'a': '123', 'b': 231, 'c': False}))
        self.assertTrue(validator.validates({'b': '231'}))

    def test_error(self):
        self.assertFalse(validator.validate('d', 123))
        self.assertFalse(validator.validate('a', 123))


if __name__ == '__main__':
    unittest.main()
