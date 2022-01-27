import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="nasaapi",
    version="1.0.0b",
    description="Wrapper for nasa api",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Artem Nikolaev",
    author_email="anikolaev82@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.9"
    ],
    packages=["nasaapi", "nasaapi/entity", "nasaapi/entity/abclass", "nasaapi/utils", "nasaapi/rovers"],
    include_package_data=True,
    install_requires=["requests", "sqlalchemy", "psycopg2"]
)
