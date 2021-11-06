from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cardion/__init__.py
from cardion import __version__ as version

setup(
	name="cardion",
	version=version,
	description="Healthcare",
	author="Cardion",
	author_email="hrishikesh.k@cardion.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
