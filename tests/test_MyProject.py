"""
Example unit tests for MyProject package
"""
import unittest
import desc.myproject

class MyProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.message = 'Hello, world'
        
    def tearDown(self):
        pass

    def test_run(self):
        foo = desc.myproject.MyProject(self.message)
        self.assertEquals(foo.run(), self.message)

    def test_failure(self):
        self.assertRaises(TypeError, desc.myproject.MyProject)
        foo = desc.myproject.MyProject(self.message)
        self.assertRaises(RuntimeError, foo.run, True)

if __name__ == '__main__':
    unittest.main()
