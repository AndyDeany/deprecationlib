from setuptools import setup

import deprecationlib


setup(
    name=deprecationlib.__name__,
    version=deprecationlib.__version__,
    description=deprecationlib.__doc__,
    url=deprecationlib.__url__,
    author=deprecationlib.__author__,
    author_email=deprecationlib.__author_email__,
    packages=[deprecationlib.__name__],
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    )
)
