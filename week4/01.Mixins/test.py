from mixins import JsonableMixin, SetAttributesMixin, EqualAttributesMixin, XMLableMixin


class Panda(JsonableMixin, SetAttributesMixin, EqualAttributesMixin, XMLableMixin):
    pass


def main():
    p = Panda(name="Ivan", age=30)
    print(p.to_xml())


if __name__ == '__main__':
    main()
