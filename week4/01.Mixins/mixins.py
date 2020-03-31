import json
from dicttoxml import dicttoxml
import xmltodict
import jxmlease


class JsonableMixin:
    def to_json(self, indent=4):
        name = self.__class__.__name__
        attributes = self.__dict__
        return json.dumps({'type': name, 'dict': attributes}, indent=indent)

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        class_name = data['type']

        if class_name != cls.__name__:
            raise ValueError('Wrong type.')

        attributes = data['dict']

        return cls(**attributes)


class SetAttributesMixin:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)


class EqualAttributesMixin:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


# from_xml can return object which field values are strings


class XMLableMixin:
    def to_xml(self):
        name = self.__class__.__name__
        return dicttoxml(self.__dict__, custom_root=name, attr_type=False).decode("utf-8")[39:]

    @classmethod
    def from_xml(cls, xml_data):
        parsed = jxmlease.parse(xml_data)
        dictionary = json.loads(json.dumps(parsed))
        class_name = cls.__name__
        if class_name not in dictionary:
            raise ValueError('Wrong type')
        attributes = dictionary[class_name]
        if attributes == '':
            return cls()
        simplify_attributes(attributes)
        return cls(**attributes)


def simplify_attributes(attributes):
    for key, val in attributes.items():
        if type(val) is list or type(val) is tuple:
            continue

        if type(val) is dict:
            simplify_dict(attributes, key)
            continue

        if is_float(val):
            attributes[key] = float(val)
            continue
        if val.isdigit():
            attributes[key] = int(val)
            continue


def simplify_dict(attributes, key):
    for k, v in attributes[key].items():

        if is_float(v):
            attributes[key][k] = float(v)
            continue
        if v.isdigit():
            attributes[key][k] = int(v)
            continue


def is_float(string):
    if '.' not in string:
        return False
    return string.replace('.', '', 1).isdigit()
