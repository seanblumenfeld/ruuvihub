#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys

import environ
from django.core.management import execute_from_command_line

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_ENV_COMMANDS = ['test', 'check']


def load_env(env_name):
    env_file = os.path.join(BASE_DIR, f'.{env_name}.env')
    environ.Env.read_env(env_file=env_file)
    os.environ['DJANGO_SETTINGS_MODULE'] = f'web.settings.{env_name}'


def get_env_name():
    env = os.getenv('ENV')

    if env:
        return env

    if sys.argv[1] in TEST_ENV_COMMANDS:
        logging.disable(logging.CRITICAL)

        if env != 'test':
            logger.info("Running tests in non test ENV. Setting test ENV to continue.")
        if os.getenv('DOCKER'):
            return 'test'
        else:
            return 'local'

    logger.info('ENV not set, using local')
    return 'local'


def main():
    env_name = get_env_name()
    load_env(env_name)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
