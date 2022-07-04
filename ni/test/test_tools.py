import unittest
from ni.config.tools import logger


class TestLogger(unittest.TestCase):
    def test_debug(self):
        msg = logger.debug([2001, '我'])
        self.assertEqual('[2001] 找不到"我"。', msg)

    def test_info(self):
        msg = logger.info([2001, '我'])
        self.assertEqual('[2001] 找不到"我"。', msg)

    def test_log(self):
        msg = logger.log([2001, '我'])
        self.assertEqual("[####] 临时打印信息：\n[2001, '我']", msg)

    def test_warning(self):
        msg = logger.warning([2001, '我'])
        self.assertEqual('[2001] 找不到"我"。', msg)

    def test_error(self):
        msg = logger.error([2001, '我'])
        self.assertEqual('[2001] 找不到"我"。', msg)

    def test_critical(self):
        msg = logger.critical([2001, '我'])
        self.assertEqual('[2001] 找不到"我"。', msg)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
