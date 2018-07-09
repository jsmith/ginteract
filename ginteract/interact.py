import io
import termios

import click
import inquirer


class Choices(click.Choice):
    """The choice type allows a value to be checked against a fixed set of
    supported values.  All of these values have to be strings.

    See :ref:`choice-opts` for an example.
    """
    name = 'choices'

    def convert(self, value: str, param, ctx):
        for choice in value.split():
            choice = choice.strip()
            if choice not in self.choices:
                self.fail('invalid choice: %s. (choose from %s)' % (value, ', '.join(self.choices)), param, ctx)
        else:
            return value

    def __repr__(self):
        return 'Choices(%r)' % list(self.choices)


def prompt(choices, message='Choice', multiple=False):
    cls = inquirer.Checkbox if multiple else inquirer.List
    question = [cls('key', message=message, choices=choices)]
    try:
        choice = inquirer.prompt(question)
        if choice is None:
            raise click.Abort
        choice = choice['key']
    except (termios.error, io.UnsupportedOperation):
        text = '{} ({})'.format(message, ', '.join(choices))
        if multiple:
            choice = click.prompt(text, default=choices[0], type=Choices(choices))
            choice = choice.split()
        else:
            choice = click.prompt(text, default=choices[0], type=click.Choice(choices))

    return choice
