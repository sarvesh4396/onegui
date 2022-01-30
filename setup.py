#!/usr/bin/env python3

# flake8: noqa
from setuptools import find_packages, setup

# Get the version from onegui/config/version.py without importing the package
exec(
    compile(open("onegui/config/version.py").read(), "onegui/config/version.py", "exec")
)


# Get the packages from onegui/config/requirements.py without importing the package
exec(
    compile(
        open("onegui/config/requirements.py").read(),
        "onegui/config/requirements.py",
        "exec",
    )
)


# Package meta-data.
NAME = "onegui"
package = "onegui"
DESCRIPTION = "Only python gui tool you need for all your tools"
AUTHOR = "Sarvesh Kumar Dwivedi"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = __version__
CLI_NAME = "onegui"
EMAIL = ""

setup(
    name=NAME,
    packages=find_packages(include=[package, f"{package}.*"]),
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    install_requires=INSTALL_REQUIRES,
    setup_requires=SETUP_REQUIRES,
    include_package_data=True,
    extras_require={"all": ["matplotlib>=2.2.0", "jupyter"]},
    entry_points={
        "console_scripts": [f"{CLI_NAME.lower()} = {package}.{package}:main"]
    },
    package_data={package: [f"{package}/assets/*"]},
)
