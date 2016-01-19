import unittest
import subprocess

class CheckHello(unittest.TestCase):
    def test_output(self):
        p1 = subprocess.check_output(["./hello"])
        # print p1
        self.assertEqual(p1, "Helloworld !\n")
    def test_output2(self):
        p1 = subprocess.check_output(["./hello"])
        # print p1
        self.assertEqual(p1, "Helloworld !\n")

if __name__ == '__main__':
    unittest.main()
