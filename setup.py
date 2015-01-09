from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()  # TODO convert rst

version = '0.3.0'

install_requires = []

setup(name='provtool',
    version=version,
    description="Utility for working with iOS Provisioning Profiles",
    long_description=README,
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 2.7',
    ],
    keywords='ios provisioning',
    author='Andy Mroczkowski',
    author_email='andy@mrox.net',
    url='http://github.com/amrox/provtool',
    license='BSD',
    packages=find_packages('', exclude=['ez_setup', 'examples', 'tests']),
    package_dir={'provtool': 'provtool'}, include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
            'console_scripts':
                ['provtool = provtool.cli:main'],
    }
)
