import unittest

from zope.app.testing.functional import FunctionalDocFileSuite
from z3c.schema2json.testing import FunctionalLayer

def test_suite():

    readme = FunctionalDocFileSuite(
        'README.txt')

    readme.layer = FunctionalLayer

    return unittest.TestSuite([readme])
