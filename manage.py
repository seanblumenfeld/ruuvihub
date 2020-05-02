#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys

import environ
from django.core.management import execute_from_command_line


def load_env(env_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_file = os.path.join(base_dir, f'.{env_name}.env')
    environ.Env.read_env(env_file=env_file)
    os.environ['DJANGO_SETTINGS_MODULE'] = f'web.settings.{env_name}'


def main():
    if sys.argv[1] == 'test':
        logging.disable(logging.CRITICAL)
        load_env(env_name='test')
    else:
        load_env(env_name='dev')

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
