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

    def test_get_name(self):
        person = Person()
        person.set_name('Abbas')
        self.assertEqual(person.get_name(0),'Abbas')

    def test_get_name_empty_object(self):
        person1 = Person()
        # person.set_name('Abbas')
        self.assertEqual(person1.get_name(1),'There is no such user')
        

    

if __name__ == '__main__':
    unittest.main()