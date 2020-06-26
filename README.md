# Data Intensive Applications: Project

## Requirements

This repo provides a virtual environment support, no other installation
providers are supported, if you want to directly install packages in your
system, please search yourself their names (`pipenv graph | grep -v '-'`) and
how to do.

Install [Pipenv](https://github.com/pypa/pipenv).

### Pipenv

```bash
$ pipenv install
$ pipenv shell
(venv) $ ipython kernel install --user --name=diproj --display-name "Py3 DIA - Project"
```

## Run

Execute

```bash
$ pipenv shell
(venv) $ jupyter notebook
```

Then a tab should have been opened in your browser.

If you used the virtual environment installation, choose the kernel `diproj` (or
the chosen name).
