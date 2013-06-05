from setuptools import setup, find_packages

version = '1.0.0dev'

setup(name='z3c.schema2json',
      version=version,
      description="Convert zope.schema defined object to dictionary structure",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Paul Wilson',
      author_email='',
      url='http://github.com/jakke/z3c.schema2json',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['z3c', 'z3c.schema2json'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.component',
          'zope.container',
          'zope.schema',
          'zope.datetime',
          'martian',
          'five.grok',
          'grokcore.component',
          'z3c.autoinclude',
          'z3c.schema2json',
      ],
      extras_require=dict(
            test=['plone.testing',
                  'zc.sourcefactory',
                  'zope.app.testing', ]),
      )
