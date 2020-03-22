import unittest
from python_sort import python_sort, change_order_based_on_ascending

class TestPythonSort(unittest.TestCase):
    def test_python_sort_for_empty_array(self):
        arr = []
        python_sort(arr = arr)
        res = []
        self.assertEqual(arr,res)

    def test_python_sort_for_empty_tuple(self):
        tupl = ()
        python_sort(arr = tupl)
        res = ()
        self.assertEqual(tupl,res)
    

    def test_if_python_sort_works_for_tuple(self):
        tupl = (2, 2, 1, 3, 5)
        tupl = python_sort(arr = tupl)
        res = (1, 2, 2, 3, 5)

        self.assertEqual(tupl, res)

    def test_if_python_sort_works_for_array_of_dictionaries(self):
        arr = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
        key = 'age'
        res = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

        arr = python_sort(arr = arr, key= key)

        self.assertEqual(arr, res)


    def test_if_python_sort_works_for_tuple_of_dictionaries(self):
        tupl = ({'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25})
        key='age'
        res = ({'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27})

        tupl = python_sort(arr = tupl, key = key)

        self.assertEqual(tupl, res)                                

    def test_if_change_order_based_on_ascending_works_for_descending(self):
        arr = [8, 9, 10, 10, 100]
        res = [100, 10, 10, 9, 8]
        asc = False
        arr = change_order_based_on_ascending(arr, asc)

        self.assertEqual(arr, res)

    def test_if_change_order_based_on_ascending_works_for_acscending(self):
        arr = [8, 9, 10, 10, 100]
        res = [8, 9, 10, 10, 100]
        asc = True

        arr = change_order_based_on_ascending(arr, asc)

        self.assertEqual(arr, res)

    def test_if_python_sort_raises_exception_when_key_is_given_but_array_is_not_of_dictionaries(self):
        arr = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}, 1, 'Ivan', 'Pesho']
        key = 'age'

        res = None 
        try:
            python_sort(arr = arr, key = key)
        except ValueError as exc:
            res = str(exc)

        self.assertEqual(res, 'Cannot sort array which contains different types of elements')      


    def test_if_python_sort_raises_exception_when_key_is_not_given_but_array_is_of_dictionaries(self):
        arr = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]

        res = None 
        try:
            python_sort(arr = arr)
        except ValueError as exc:
            res = str(exc)

        self.assertEqual(res, 'Cannot sort array of dictionaries without a given key') 



if __name__ == '__main__':
    unittest.main()
