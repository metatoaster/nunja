from setuptools import setup
from setuptools import find_packages

version = '0.0'

classifiers = """
Development Status :: 4 - Beta
Environment :: Console
Framework :: Setuptools Plugin
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)
Operating System :: OS Independent
Programming Language :: JavaScript
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
""".strip().splitlines()

package_json = {
    "dependencies": {
        "requirejs-text": "~2.0.12",
    },
}

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='nunja',
    version=version,
    description="The unified templating framework for Python x JavaScript",
    long_description=long_description,
    classifiers=classifiers,
    keywords='',
    author='Tommy Yu',
    author_email='tommy.yu@auckland.ac.nz',
    url='https://github.com/calmjs/nunja',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=[],
    zip_safe=True,
    package_json=package_json,
    install_requires=[
        'Jinja2>=2.4',
        'calmjs.rjs',
    ],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*',
    entry_points={
        'calmjs.registry': [
            'nunja.mold = nunja.registry:MoldRegistry',
        ],
    },
    test_suite="nunja.tests.make_suite",
)