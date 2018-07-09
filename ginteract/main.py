import functools
import os
import sys

import click
import git

from ginteract import interact


@click.group()
def main():
    pass


def command(*args, **kwargs):
    def decorator(func):
        # noinspection PyTypeChecker
        @click.command(*args, **kwargs)
        @functools.wraps(func)
        def wrapper(*a, **kw):
            repo = git.Repo(os.getcwd(), search_parent_directories=True)
            branches = sorted(repo.branches, key=lambda branch: branch.commit.committed_date, reverse=True)
            branches = [str(branch) for branch in branches]
            current = str(repo.active_branch)
            branches = list(filter(lambda branch: branch != current, branches))
            cmd = func(repo, branches, current, *a, **kw)
            try:
                cmd()
            except git.exc.GitCommandError as e:
                click.echo(e)

        main.add_command(wrapper)
        return wrapper

    return decorator


@command('checkout')
def checkout(repo, branches, _):
    choice = interact.prompt(branches)
    return lambda: repo.git.checkout(choice)


@command('merge')
def merge(repo, branches, current):
    choice = interact.prompt(branches, '{} <- '.format(current))
    return lambda: repo.git.merge(choice)


@command('delete')
def delete(repo, branches, _):
    choices = interact.prompt(branches, multiple=True)
    if choices and not click.confirm('Delete {}?'.format(', '.join(choices))):
        raise click.Abort

    def delete_branches():
        for branch in choices:
            repo.git.branch('-d', branch)

    return delete_branches


if __name__ == '__main__':
    sys.exit(main())
