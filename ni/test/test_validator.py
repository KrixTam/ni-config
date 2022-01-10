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

    def test_error_01(self):
        self.assertFalse(validator.validate('d', 123))

    def test_error_02(self):
        self.assertFalse(validator.validate('a', 123))

    def test_error_03(self):
        self.assertFalse(validator.validates({'a': '123', 'd': 231, 'c': False}))

    def test_error_04(self):
        self.assertFalse(validator.validates({'a': 123, 'c': False}))


if __name__ == '__main__':
    unittest.main()
