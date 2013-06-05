from unittest import TestCase
from unittest import TestSuite, makeSuite

from zope.app.testing.functional import FunctionalDocFileSuite
from z3c.schema2json.testing import SCHEMA2JSON_BASE


class TestMySetup(TestCase):
    """blub"""
    layer = SCHEMA2JSON_BASE

    def test_my_setup(self):
        self.assertEqual(1, 1)


def test_suite():

    readme = FunctionalDocFileSuite(
        'usage.txt')

    suite = TestSuite()
    suite.addTest(makeSuite(TestMySetup))

    return suite

    # return unittest.TestSuite([readme])
