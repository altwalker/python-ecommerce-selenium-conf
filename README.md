# Example: Python E-commerce

Demo tests to serve as a starting point for the State Model Based Testing with Selenium workshop at SeleniumConf 2023 in Chicago. 

The site under test is available on GitHub pages [here](https://altwalker.github.io/jekyll-ecommerce/).

## Prerequisites

You will need to have Python3 installed for this workshop. More info on that here: https://www.python.org/


## Setup

Linux/MacOS:

```bash
$ cd python-ecommerce-selenium-conf
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Windows:

```bash
$ cd python-ecommerce-selenium-conf
$ python3 -m venv .venv
$ .venv/Scripts/activate.bat
$ pip install -r requirements.txt
```

Read more about venv [here](https://docs.python.org/3/library/venv.html).

#### Geckodriver

Download [geckodriver](https://github.com/mozilla/geckodriver/releases).

After you download and extract the executable, make sure you set the path to the geckodriver executable in the Path variable to make other programs aware of its location.

On Windows:

```
$ set PATH=%PATH%;C:\bin\geckodriver
```

On Linux/MacOS:

```
$ ln -s /path/to/geckodriver /usr/local/bin/geckodriver
```
### Run Tests

To run the tests use:

```
pytest -s 
```

## Prepare Setup for State Model Based Tools

We will be using AltWalker and GraphWalker to implement and run models that we create during the State Model Based Workshop. 


For this you will need to:

- Install [Java11](https://openjdk.java.net/)
- Install and configure GraphWalker CLI - instructions are available [here](https://github.com/altwalker/graphwalker-installer)

To check that you GraphWalker correctly configured, run the following command and check that you get the same version:

```
$ gw --version
org.graphwalker version: 4.3.2-408d9b4

org.graphwalker is open source software licensed under MIT license
The software (and it's source) can be downloaded from http://graphwalker.org
For a complete list of this package software dependencies, see http://graphwalker.org/archive/site/graphwalker-cli/dependencies.html
```