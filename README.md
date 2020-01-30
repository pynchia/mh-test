# mh-test

test for MH

Meter -> broker -> PV Simulator -> output file

## Setup

No proper setup was done.
Enable python to find the location of the sources with

`export PYTHONPATH='/your/path/mh-test'`

## Execution

`cd /your/path/mh-test/`

Run the meter with

`python mh/meter/cli.py`

then run the PV simulator with

`python mh/pv/cli.py`

