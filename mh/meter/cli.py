"""
The command line interface to the user
"""

import click
import logging

from mh.meter.main import main


log = logging.getLogger(__name__)


DEFAULT_QUEUE = 'meter'

@click.command()
@click.option(
    "--url", help="Full address and credentials to the broker"
)
@click.option(
    "--queue", default=DEFAULT_QUEUE, help="Name of the queue"
)
def cli(url, queue):
    main(url, queue)

# 'amqp://woabdkju:OYy-a8GI_1Clv2QIdeu26b92FYj2uTeO@hawk.rmq.cloudamqp.com/woabdkju'

if __name__ == '__main__':
    cli()
