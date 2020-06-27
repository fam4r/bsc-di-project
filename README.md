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
$ pipenv run ipython kernel install --user --name=diproj --display-name "Py3 DIA - Project"
```

## Run

Execute

```bash
$ pipenv run jupyter notebook
```

Then a tab should have been opened in your browser.

If you used the virtual environment installation, choose the kernel `diproj` (or
the chosen name).

## Project description

### References

- [Malicious and Benign Websites: Classify by application and network features](https://www.kaggle.com/xwolf12/malicious-and-benign-websites)

### Fix arff dataset

```bash
$ wget <ds_url.arff> -O <ds_name>.arff
$ sed -i "s/{ /{/g" <ds_name>.arff
$ sed -i "s/ }/}/g" <ds_name>.arff
```

### Convert arff dataset to csv

```bash
$ pipenv run ./arff2csv.py
```
