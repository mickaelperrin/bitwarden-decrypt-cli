#!/usr/bin/env python3
import sys
from bitwarden_simple_cli.CliSimple import CliSimple


def start():
    cli = CliSimple(*sys.argv)
    cli.run()


if __name__ == '__main__':
    start()
