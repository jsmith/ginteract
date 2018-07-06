#!/usr/bin/env python3
import os
import sys

import git
import inquirer


def main():
    git_repo = git.Repo(os.getcwd(), search_parent_directories=True)

    # noinspection PyTypeChecker
    branches = sorted(git_repo.branches, key=lambda branch: branch.commit.committed_date, reverse=True)
    branch_lookup = {str(branch): branch for branch in branches}

    question = [
        inquirer.List(
            'branch',
            message='Which branch',
            choices=[str(branch) for branch in branches],
        ),
    ]

    choice = inquirer.prompt(question)

    if choice is None:
        return

    choice = choice['branch']
    branch_lookup[choice].checkout()
    print('Checked out {}!'.format(choice))


if __name__ == '__main__':
    sys.exit(main())
