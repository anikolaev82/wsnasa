import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
#README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="nasaapi",
    version="1.0.0",
    description="Wrapper for nasa api",
#    long_description=README,
#    long_description_content_type="text/markdown",
#    url="https://github.com/realpython/reader",
    author="Artem Nikolaev",
    author_email="anikolaev82@gmail.com",
#    license="MIT",
#    classifiers=[
#        "License :: OSI Approved :: MIT License",
#        "Programming Language :: Python :: 3",
#        "Programming Language :: Python :: 3.7",
#    ],
    packages=["nasaapi", "nasaapi/entity", "nasaapi/utils", "nasaapi/rovers"],
    include_package_data=True,
    install_requires=["requests"],
#    entry_points={
#        "console_scripts": [
#            "realpython=reader.__main__:main",
#       ]
#    },
)