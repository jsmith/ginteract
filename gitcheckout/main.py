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
        # noinspection PyTypeChecker
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
    branches = filter(lambda branch: branches)
    branches = [str(branch) for branch in branches]
    choice = interact.prompt('Choice', branches)
    return lambda: repo.git.checkout(choice)


@command('merge')
def merge(repo: git.Repo):
    # noinspection PyTypeChecker
    branches = sorted(repo.branches, key=lambda branch: branch.commit.committed_date, reverse=True)
    branches = [str(branch) for branch in branches]
    choice = interact.prompt('Choice', branches)
    return lambda: repo.git.merge(choice)


@command('delete')
def delete(repo: git.Repo):
    # noinspection PyTypeChecker
    branches = sorted(repo.branches, key=lambda branch: branch.commit.committed_date, reverse=True)
    branches = [str(branch) for branch in branches]
    choices = interact.prompt('Choice', branches, multiple=True)

    def delete_branches():
        for branch in choices:
            repo.git.branch('-d', branch)

    return delete_branches


if __name__ == '__main__':
    sys.exit(main())
