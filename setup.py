# coding: utf-8

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PythonPackage",
    version="1.0.0",
    author="Alexis Foerster",
    author_email="alexis.foerster@gmail.com",
    description="Python package including base elements.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lovehina13/PythonPackage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent",
    ],
    install_requires=["pip>=23.0.1"],
    python_requires=">=3.11.2",
    include_package_data=True,
    package_data={"PythonPackage": ["MyResources/*"]}
)
