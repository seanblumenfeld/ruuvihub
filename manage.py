#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys

import environ
from django.core.management import execute_from_command_line


def load_env(env):
    if env == 'test':
        logging.disable(logging.CRITICAL)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_file = os.path.join(base_dir, f'.{env}.env')
    environ.Env.read_env(env_file=env_file)
    os.environ['DJANGO_SETTINGS_MODULE'] = f'web.settings.{env}'


def get_env():
    if sys.argv[1] == 'test':
        if os.getenv('ENV', 'test') != 'test':
            raise RuntimeError('Tests must run using test ENV.')
        return 'test'
    return os.getenv('ENV', 'dev')


def main():
    env = get_env()
    load_env(env)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
