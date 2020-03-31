import unittest
from mixins import JsonableMixin, SetAttributesMixin, EqualAttributesMixin, XMLableMixin


class Panda(JsonableMixin, SetAttributesMixin, EqualAttributesMixin, XMLableMixin):
    pass


class Person(JsonableMixin, SetAttributesMixin, EqualAttributesMixin, XMLableMixin):
    pass


class TestXMLableMixin(unittest.TestCase):
    def test_if_to_xml_works_correctly_for_object_without_data_structures(self):
        panda = Panda(
            name='Marto',
            age=20,
            weight=100.10,
        )
        expected = '<Panda><name>Marto</name><age>20</age><weight>100.1</weight></Panda>'

        self.assertEqual(expected, panda.to_xml())

    def test_if_to_xml_works_correctly_for_object_with_data_structures(self):
        panda = Panda(
            name='Marto',
            age=20,
            weight=100.10,
            skills={'eat': 100, 'fight': 200}
        )
        expected = '<Panda><name>Marto</name><age>20</age><weight>100.1</weight><skills><eat>100</eat><fight>200' \
                   '</fight></skills></Panda>'

        self.assertEqual(expected, panda.to_xml())

    def test_if_to_xml_works_correctly_for_empty_object(self):
        panda = Panda()
        expected = '<Panda></Panda>'

        self.assertEqual(expected, panda.to_xml())

    def test_if_from_xml_works_correctly_for_empty_object(self):
        panda_xml = '<Panda></Panda>'
        expected = Panda().__dict__

        self.assertEqual(expected, Panda.from_xml(panda_xml).__dict__)

    def test_if_from_xml_works_correctly_for_object_with_data_structures(self):
        panda_xml = '<Panda><name>Marto</name><age>20</age><weight>100.1</weight><skills><eat>100</eat><fight>200' \
                    '</fight></skills></Panda>'

        expected = Panda(name='Marto',
                         age=20,
                         weight=100.10,
                         skills={'eat': 100, 'fight': 200}
                         ).__dict__

        self.assertEqual(expected, Panda.from_xml(panda_xml).__dict__)

    def test_if_from_xml_works_correctly_for_object_without_data_structures(self):
        panda_xml = '<Panda><name>Marto</name><age>20</age><weight>100.1</weight></Panda>'

        expected = Panda(name='Marto',
                         age=20,
                         weight=100.10,
                         ).__dict__

        self.assertEqual(expected, Panda.from_xml(panda_xml).__dict__)

    def test_if_from_xml_raises_Exception(self):
        panda_xml = '<Panda><name>Marto</name><age>20</age><weight>100.1</weight></Panda>'

        res = None
        exp = 'Wrong type'
        try:
            Person.from_xml(panda_xml)
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)


if __name__ == '__main__':
    unittest.main()
