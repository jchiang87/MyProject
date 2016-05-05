#!/usr/bin/env python
"""
Run all of the test scripts with filename pattern test_*.py.
"""
import os
import unittest
runner = unittest.TextTestRunner()
loader = unittest.TestLoader()
testsuite = loader.discover(os.path.join(os.environ['MYPROJECT_DIR'], 'tests'),
                            pattern='test_*.py')
runner.run(testsuite)
