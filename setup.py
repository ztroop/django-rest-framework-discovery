from setuptools import find_packages, setup

version = "0.1.5"

setup(
    author='Zackary Troop',
    name='rest_framework_discovery',
    version=version,
    url='https://github.com/ztroop/djangorestframework-discovery',
    license='BSD',
    description='Automatically creates a queryable data source from an existing database.',
    packages=find_packages(exclude=['assets']),
    install_requires=['django>=2.0.0', 'djangorestframework>=3.8.0'],
)
