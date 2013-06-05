# -*- coding: utf-8 -*-
"""
kuleuven.wiwo.app

Licensed under the GPL license, see LICENCE.txt for more details.
"""
import os
import glob
import unittest

from Globals import package_home
import doctest

from plone.testing import layered
from z3c.schema2json.testing import SCHEMA2JSON_BASE


UNITTESTS = []

OPTIONFLAGS = (doctest.ELLIPSIS |
               doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.NORMALIZE_WHITESPACE |
               doctest.REPORT_NDIFF)


def list_doctests():
    home = package_home(globals())
    return [filename for filename in
            glob.glob(os.path.sep.join([home, '*.txt']))
            if os.path.basename(filename) not in UNITTESTS]


def test_suite():
    filenames = list_doctests()
    suites = []
    for filename in filenames:
        suite = layered(
            doctest.DocFileSuite(
                os.path.basename(filename),
                optionflags=OPTIONFLAGS,
                package='z3c.schema2json.tests',),
            layer=SCHEMA2JSON_BASE)
        suites.append(suite)

    return unittest.TestSuite(suites)
