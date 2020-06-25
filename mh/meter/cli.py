"""
The command line interface to the Meter application
"""

import click
import logging
from mh.meter.main import main


DEFAULT_QUEUE = 'meter'

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.ERROR)

@click.command()
@click.option(
    "--url", "-u", required=True, help="Full address and credentials to the broker"
)
@click.option(
    "--queue", "-q", default=DEFAULT_QUEUE, help="Name of the queue"
)
@click.option(
    "--verbose", "-v", is_flag=True, default=False, help="Log at debug level"
)
def cli(url, queue, verbose):
    if verbose:
        log.setLevel(logging.INFO)
    main(url, queue)


if __name__ == '__main__':
    cli()
