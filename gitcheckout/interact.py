import io
import termios

import click
import inquirer


def prompt(message, choices):
    question = [inquirer.List('key', message=message, choices=choices)]
    try:
        choice = inquirer.prompt(question)
        if choice is None:
            raise click.Abort
        choice = choice['key']
    except (termios.error, io.UnsupportedOperation):
        text = '{} ({})'.format(message, ', '.join(choices))
        choice = click.prompt(text, default=choices[0], type=click.Choice(choices))
    return choice
