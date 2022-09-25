import unittest
from main import Person


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_set_name(self):
        person = Person()
        person.set_name('Abbas')
        self.assertEqual(person.name[0], 'Abbas')
        

    

if __name__ == '__main__':
    unittest.main()