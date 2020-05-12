#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys

import environ
from django.core.management import execute_from_command_line

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COMMANDS_TO_DEFAULT_TO_DEV_ENV = ['makemigrations', 'migrate']
COMMANDS_TO_DEFAULT_TO_TEST_ENV = ['test', 'check']


def load_env(env_name):
    env_file = os.path.join(BASE_DIR, 'environments', f'.{env_name}.env')
    environ.Env.read_env(env_file=env_file)
    os.environ['DJANGO_SETTINGS_MODULE'] = f'web.settings.{env_name}'
    return env_file, os.environ['DJANGO_SETTINGS_MODULE']


def get_env_name():
    env = os.getenv('ENV')

    if env:
        return env

    if sys.argv[1] in COMMANDS_TO_DEFAULT_TO_TEST_ENV:
        if env != 'test':
            logger.warning("Running tests in non test ENV. Setting ENV to test to continue.")
        logger.warning('Disabling all logging.')
        logging.disable(logging.CRITICAL)
        return 'test'
    else:
        if env != 'dev':
            logger.warning(f"Running '{sys.argv[1]}' in non dev ENV. Setting ENV to dev to "
                           f"continue.")
        return 'dev'


def main():
    env_name = get_env_name()
    env_file, settings_module = load_env(env_name)
    logger.info(f'Using env file: {env_file}')
    logger.info(f'Using settings module: {settings_module}')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
