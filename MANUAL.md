# PythonPackage

## Definition

### Sources

* Set modules to `PythonPackage` directory.
* Set resource files to `MyResources` directory.
* Rename these directories to expected names.
* Edit `main` method in `__main__.py` module to expected package runtime behavior.

### Resource files

* Resource file access example:

```python
import pkg_resources
file = pkg_resources.resource_filename("PythonPackage", "MyResources/MyFile.txt")
data = open(file, "r", encoding="utf-8").readlines()
```

### Information

* Edit `README.md`, `PythonPackage.doxygen`, `PythonPackage.spec` and `setup.py` files to expected information.
* Rename `PythonPackage.doxygen` and `PythonPackage.spec` files to expected names.

## Installation

### Legacy

* Execute `python setup.py install --user` command to install package.

### Modern

* Execute `pip install build --user` command to install `build` package.
* Execute `python -m build` command to generate `dist/PythonPackage-1.0.0.tar.gz` package.
* Execute `pip install dist/PythonPackage.tar.gz --user` command to install package.

## Use

### Executable

* Execute `python -m PythonPackage` command to execute package.

_Note: The command executes local package if `PythonPackage` exists in current directory._

### Package

* Use in another Python project example:

```python
from PythonPackage.MyModule import MyClass
x = MyClass(1)
print(x)
```

## Deployment

### Standalone executable

* Execute `pip install PyInstaller --user` command to install `PyInstaller` package.
* Execute `python -O -m PyInstaller PythonPackage.spec` command to generate `dist/PythonPackage-1.0.0.exe` standalone executable.

### Mirror

* Set `dist/PythonPackage-1.0.0.tar.gz` package to Python packages mirror.
