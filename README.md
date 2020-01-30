# mh-test

test for MH

Meter -> broker -> PV Simulator -> output file

## Setup

No proper setup was done.
Enable python to find the location of the sources with

`export PYTHONPATH='/your/path/mh-test'`

Set the url to the broker

`export BROKER_URL='amqp://woabdkju:OYy-a8GI_1Clv2QIdeu26b92FYj2uTeO@hawk.rmq.cloudamqp.com/woabdkju'`

## Execution

`cd /your/path/mh-test/`

Run the meter with

`python mh/meter/cli.py --url $BROKER_URL`

then run the PV simulator with

`python mh/pv/cli.py --url $BROKER_URL`
