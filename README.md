# Example: Python E-commerce

Demo tests to serve as a starting point for the State Model Based Testing with Selenium workshop at SeleniumConf 2023 in Chicago. 

The site under test is available on GitHub pages [here](https://altwalker.github.io/jekyll-ecommerce/).

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
