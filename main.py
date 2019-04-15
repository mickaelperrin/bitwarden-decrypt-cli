#!/usr/bin/env python3
import sys
from bitwarden_decrypt_simple_cli.CliSimple import CliSimple

if __name__ == '__main__':
    cli = CliSimple(*sys.argv)
    cli.run()
