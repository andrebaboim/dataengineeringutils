from setuptools import setup, find_packages

setup(
    name='dataengineeringutils',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A python package containing functions that help manage our data management processes on AWS',
    long_description=open('README.md').read(),
    install_requires=[],
    include_package_data=True,
    url='https://github.com/moj-analytical-services/dataengineeringutils',
    author='Karik Isichei',
    author_email=''
)