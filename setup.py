from setuptools import setup, find_packages

setup(
    name="X-pyAPI",
    version="0.4",
    description="A simple Python library for posting tweets on X.com using new X API v2.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Redian Marku",
    author_email="redian@topnotch-programmer.com",
    url="https://github.com/redianmarku/X-PyAPI.git",
    packages=find_packages(),
    install_requires=[
        'requests-oauthlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
