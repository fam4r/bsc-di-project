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

- Original source: [UCI](https://archive.ics.uci.edu/ml/datasets/phishing+websites)
- Described dataset on [OpenML](https://www.openml.org/d/4534)

### Fix arff dataset

```bash
$ wget https://archive.ics.uci.edu/ml/machine-learning-databases/00327/Training%20Dataset.arff
$ mv Training\ Dataset.arff PhishingWebsites.arff
$ sed -i "s/{ /{/g" PhishingWebsites.arff
$ sed -i "s/ }/}/g" PhishingWebsites.arff
```

### Convert arff dataset to csv

```bash
$ ./arff2csv.py
```
