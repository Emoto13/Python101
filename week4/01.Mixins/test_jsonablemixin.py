import unittest
import json
from mixins import JsonableMixin, SetAttributesMixin, EqualAttributesMixin, XMLableMixin


class Panda(JsonableMixin, SetAttributesMixin, EqualAttributesMixin, XMLableMixin):
    pass


class Car(JsonableMixin, SetAttributesMixin, EqualAttributesMixin, XMLableMixin):
    pass


class TestJsonableMixin(unittest.TestCase):
    def test_to_json_returns_empty_json_for_objects_with_no_arguments(self):
        panda = Panda()

        result = panda.to_json(indent=4)
        expected = {
            'type': Panda.__name__,
            'dict': {}
        }

        self.assertEqual(result, json.dumps(expected, indent=4))

    def test_to_json_returns_correct_json_with_arguments(self):
        panda = Panda(
            name='Marto',
            age=20,
            weight=100.10,
            food=['bamboo', 'grass'],
            skills={'eat': 100, 'sleep': 200}
        )

        panda_result = panda.to_json(indent=4)
        panda_expected = {
            'type': Panda.__name__,
            'dict': {
                'name': 'Marto',
                'age': 20,
                'weight': 100.10,
                'food': ['bamboo', 'grass'],
                'skills': {'eat': 100, 'sleep': 200}
            }
        }

        self.assertEqual(panda_result, json.dumps(panda_expected, indent=4))

    #    def test_to_json_returns_correct_json_with_arguments_of_jsonable_type(self):
    #        panda = Panda(name='Marto', friend=Panda(name='Ivo'))

    #        panda_result = panda.to_json(indent=4)
    #       panda_expected = {
    #            'type': Panda.__name__,
    #            'dict': {
    #               'name': 'Marto',
    #               'friend': {
    #                   'type': Panda.__name__,
    #                   'dict': {
    #                       'name': 'Ivo'
    #                  }
    #              }
    #          }
    #      }

    #      self.assertEqual(panda_result, json.dumps(panda_expected, indent=4))

    def test_from_json_with_wrong_class_type(self):
        car = Car()
        car_json = car.to_json()

        with self.assertRaises(ValueError):
            Panda.from_json(car_json)

    def test_from_json_with_no_arguments(self):
        car = Car()
        car_json = car.to_json()

        result = Car.from_json(car_json)

        self.assertEqual(car, result)

    def test_from_json_with_arguments(self):
        panda = Panda(
            name='Marto',
            age=20,
            weight=100.10,
            food=['bamboo', 'grass'],
            skills={'eat': 100, 'sleep': 200}
        )
        panda_json = panda.to_json()

        result = Panda.from_json(panda_json)

        self.assertEqual(panda, result)

    def test_if_from_json_raises_Exception(self):
        panda_dict = {
            'type': Panda.__name__,
            'dict': {
                'name': 'Marto',
                'age': 20,
                'weight': 100.10,
                'food': ['bamboo', 'grass'],
                'skills': {'eat': 100, 'sleep': 200}
            }
        }

        res = None
        exp = 'Wrong type'
        try:
            Car.from_json(json.dumps(panda_dict, indent=4))
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
