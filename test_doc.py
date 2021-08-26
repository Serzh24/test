import unittest
from doc import data_person, data_shelf

class TestDoc(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_data_person(self):
        self.assertEqual("Василий Гупкин", data_person("2207 876234"))

    def test_data_shelf(self):
        self.assertEqual("1", data_shelf("2207 876234"))


if __name__ == '__main__':
    unittest.main()