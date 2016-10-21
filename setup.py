"""
A plugin for Therapist to handle basic linting operations.
"""
import os

from setuptools import find_packages, setup


DEPENDENCIES = ['therapist']
ROOT = os.path.abspath(os.path.dirname(__file__))

version = __import__('therapist_basic_linter').__version__


setup(
    name='therapist-basic-linter',
    version=version,
    url='https://github.com/rehandalal/therapist-basic-linter',
    license='Mozilla Public License Version 2.0',
    author='Rehan Dalal',
    author_email='rehan@meet-rehan.com',
    description='A plugin for Therapist to handle basic linting operations.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=DEPENDENCIES,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    py_modules=['therapist'],
    entry_points={
        'therapist.plugin': [
            'end_of_file_newline = therapist_basic_linter.plugins:EndOfFileNewline',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ]
)
