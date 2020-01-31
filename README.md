# mh-test

test for MH

Meter -> broker -> PV Simulator -> output file

## Setup

No proper setup installation was done.
Enable python to find the location of the sources with

`export PYTHONPATH='/your/path/mh-test'`

Set the url to the broker

`export BROKER_URL='amqp://woabdkju:OYy-a8GI_1Clv2QIdeu26b92FYj2uTeO@hawk.rmq.cloudamqp.com/woabdkju'`

## Configuration

The PV simulator program reads the file named `PV_DAY_POWER.txt` from the current directory.
Such file contains the daily PV power profile signal.

The signal has been created from a bell-shaped distribution which approximates the shape provided in the description of the exercise:

![alt text](doc/Daily_PV_power_profile.png)

## Execution

Go to the root directory of the project

`cd /your/path/mh-test/`

### Meter

Run the meter (i.e. the publisher) with

`python mh/meter/cli.py -v --url $BROKER_URL`

### PV

Run the PV simulator (i.e. the subscriber) with

`python mh/pv/cli.py --outputfile myout.txt --url $BROKER_URL`

where `myout.txt` is the output file of choice.
