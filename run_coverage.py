import os
import coverage
import unittest


def run_all_tests(test_modules):
    suite = unittest.TestSuite()
    for t in test_modules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suite_fn = getattr(mod, 'suite')
            suite.addTest(suite_fn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
    unittest.TextTestRunner().run(suite)


# 删除测试文件
test_files = ['config.cfg', 'cr-config.cfg', 'config_dump.cfg']
for filename in test_files:
    if os.path.exists(filename):
        os.remove(filename)

test_modules = [
    'ni.test.test_codec',
    'ni.test.test_config',
    'ni.test.test_encryption',
    'ni.test.test_validator'
]

# 执行测试用例
cov = coverage.Coverage()
cov.start()

run_all_tests(test_modules)

cov.stop()
cov.save()

cov.html_report(directory='htmlcov')