from zope.interface import Interface


class IJSONGenerator(Interface):

    def output(value):
        """Output value as JSON item according to field.
        """

    def input(item):
        """Input JSON item according to field and return value.
        """
