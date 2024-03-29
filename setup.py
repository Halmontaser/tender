from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tender_management/__init__.py
from tender_management import __version__ as version

setup(
	name="tender_management",
	version=version,
	description="management",
	author="harby almontaser",
	author_email="almontaser@nfdhr.org",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
