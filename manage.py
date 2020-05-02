#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys

import environ
from django.core.management import execute_from_command_line

ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')


def main():
    environ.Env.read_env(env_file=ENV_FILE)

    if sys.argv[1] == 'test':
        logging.disable(logging.CRITICAL)
        os.environ['DJANGO_SETTINGS_MODULE'] = 'web.settings.test'
    else:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'web.settings.dev'

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
