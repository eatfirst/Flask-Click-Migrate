"""Flask-Click-Migrate."""

from setuptools import setup

setup(
    name='Flask-Click-Migrate',
    version='0.1.0',
    author='EatFirst.com',
    author_email='opensource@eatfirst.com',
    description='A library to glue flask + alembic + click',
    url='https://github.com/eatfirst/Flask-Click-Migrate',
    packages=['flask_click_migrate'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'six',
        'Flask',
        'click',
        'alembic',
    ]
)
