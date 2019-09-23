
import os
import re
from setuptools import setup, find_packages

NAME = 'caspo_control'

META = {}
META_FILE = "{}/__init__.py".format(NAME)
with open(META_FILE) as f:
    __data = f.read()
for key in ["version"]:
    match = re.search(r"^__{0}__ = ['\"]([^'\"]*)['\"]".format(key), __data, re.M)
    if not match:
        raise RuntimeError("Unable to find __{meta}__ string.".format(meta=key))
    META[key] = match.group(1)

setup(name=NAME,
    description = "Python 3 interface to caspo control",
    install_requires = [
        "colomoto_jupyter",
    ],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords="computational systems biology",

    include_package_data = True,
    packages = find_packages(),
    **META
)

