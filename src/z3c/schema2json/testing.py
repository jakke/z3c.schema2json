import plone.testing
from plone.testing import z2
from plone.testing import security

from zope.configuration import xmlconfig

import z3c.schema2json

SCHEMA2JSON_FIXTURE = plone.testing.zca.ZCMLSandbox(
                            filename='testing.zcml',
                            package=z3c.schema2json,
                            name='SCHEMA2JSON_FIXTURE')


class BasicLayer(z2.Startup):

    def setUpZCML(self):
        super(BasicLayer, self).setUpZCML()
        context = self['configurationContext']
        xmlconfig.file("testing.zcml", z3c.schema2json,
                        context=context)


SCHEMA2JSON_BASE = BasicLayer(name='SCHEMA2JSON_BASE',
                        bases=(security.CHECKERS, z2.STARTUP))
