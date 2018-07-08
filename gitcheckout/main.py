import functools
import os
import sys

import click
import git

from gitcheckout import interact


@click.group()
def main():
    pass


def command(*args, **kwargs):
    def decorator(func):
        @click.command(*args, **kwargs)
        @functools.wraps(func)
        def wrapper(*a, **kw):
            repo = git.Repo(os.getcwd(), search_parent_directories=True)
            cmd = func(repo, *a, **kw)
            try:
                cmd()
            except git.exc.GitCommandError as e:
                click.echo(e)

        main.add_command(wrapper)
        return wrapper

    return decorator


@command('checkout')
def checkout(repo: git.Repo):
    # noinspection PyTypeChecker
    branches = sorted(repo.branches, key=lambda branch: branch.commit.committed_date, reverse=True)
    branch_lookup = {str(branch): branch for branch in branches}
    branches = [str(branch) for branch in branches]
    choice = interact.prompt('Choice', branches)
    return branch_lookup[choice].checkout


@command('merge')
@click.option('--remote', '-r')
def merge(repo: git.Repo, remote):
    pass


if __name__ == '__main__':
    sys.exit(main())
