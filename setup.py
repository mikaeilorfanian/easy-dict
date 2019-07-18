import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "easy-dict",
    version = "0.1",
    author = "Mikaeil Orfanian",
    author_email = "mokt@outlook.com",
    description = ("Thin wrapper around Pytchon dicts to make them easy to work with!"),
    license = "BSD",
    keywords = "dict dict-json productivity",
    url = "https://github.com/mikaeilorfanian/easy-dict",
    py_modules =["easy_dict"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
