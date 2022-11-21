GitHub Actions - Demo
=====================

## Running the Tests Locally

* System requirements:
  * python 3
  * pip

* Clone this repo

* Next, install `virtualenv` and then create & activate a virtual environment:

        pip install virtualenv 
        virtualenv ve-demo -p python3
        source ve-demo/bin/activate

* Install packages and project dependencies:

        cd demo
        pip install -r requirements.txt

* Run all tests or a certain one:

        pytest -v -s
        pytest -v -s -k test_one_times_one
