# geospatial_examples
Just some scripts/examples in python for geospatial data. Also a repo for testing some news features at Python 3.10



## Installing python3.10 at Ubuntu Focal (20.04.3)

Just update the system/packages:
```bash
sudo apt update && sudo apt upgrade -y
```
Add the ppa of deadsnakes to get last versions
```bash
sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update
```

Install the last version available of python3.10
```bash
sudo apt install python3.10
```

Update/reinstall pip 
```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
```

Install `distutils` (is deprecated with removal planned for Python 3.12), but it still seems necessary for `pip` use.
```bash
sudo apt install python3.10-distutils
```

Just checking/updating if necessary to the last version of `pip`
```bash
python3.10 -m pip install --upgrade pip
```

## Creating the environment with `virtualenv`

Install `virtualenv` with pip
```bash
python3.10 -m pip install virtualenv
```

Create the environment with virtual env
```bash
python3.10 -m virtualenv ./env/
```

Active the environment and test the python version
```bash
source env/bin/activate
which python
# Will show the path to the python, something like <your base path>/env/bin/python
python --version
# Will show the python version, in my case: Python 3.10.2
```

I kept having problems with pip version, so i fix it updating to the last version at my environment with:
```bash
# Download a install pip script
curl -O https://bootstrap.pypa.io/get-pip.py
# Run the script
python get-pip.py
# Deletes the script
rm get-pip.py
# Checks/update the pip with the pip
pip install --upgrade pip
```

To install the packages utilized at this repo, just use:
```bash
pip freeze > requirements.txt
```


## Repo organization

* At [example_module]('./example_module/') has a package to test something as a package.
* At [examples]('./examples') has scripts to test different things using the example_module and also some scripts tests.
* At [annotations]('./annotations/') has annotations (why and how it was done) for different scripts and modules at the package.