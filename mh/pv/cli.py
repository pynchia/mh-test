"""
The command line interface to the PV application
"""

import click
import logging
from mh.pv.main import main


DEFAULT_QUEUE = 'meter'

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.ERROR)

@click.command()
@click.option(
    "--outputfile", "-o", default=None, help="The file where the output data must be appended"
)
@click.option(
    "--url", "-u", required=True, help="Full address and credentials to the broker"
)
@click.option(
    "--queue", "-q", default=DEFAULT_QUEUE, help="Name of the queue"
)
@click.option(
    "--verbose", "-v", is_flag=True, default=False, help="Log at info level"
)
def cli(outputfile, url, queue, verbose):
    if verbose:
        log.setLevel(logging.INFO)
    main(outputfile, url, queue)


if __name__ == '__main__':
    cli()
