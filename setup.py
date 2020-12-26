from setuptools import find_packages, setup

setup(
    author='Zackary Troop',
    name='djangorestframework-discovery',
    version='0.1.8',
    url='https://github.com/ztroop/django-rest-framework-discovery',
    license='BSD',
    description='Create a queryable data source from an existing database.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['examples', 'tests']),
    install_requires=['django>=2.2.0', 'djangorestframework>=3.12.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
