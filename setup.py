# FIXME: Update the setup.py file with our package information
from setuptools import setup, find_packages

setup(
    name='DEMO_PACKAGE',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    author='Trevor Carter',
    author_email='trevok12@byu.edu',
    description='A package built for the sake of confirming that I can build a package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/thetkc312/demo_package.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)