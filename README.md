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
        
* Create & update a file `.env` and then export the secrets to environment variables:

        cp .env.example .env
        source .env

* Run all tests or a certain one:

        pytest -v -s
        pytest -v -s -k test_one_times_one

## Running the Tests Remotely

* Go to [GitHub Actions](https://github.com/M3lania/demo/actions)
* Click on the `Run workflow` button
* The tests run automatically on staging every day at 11PM (UTC)
