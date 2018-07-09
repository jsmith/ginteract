import os
import tempfile
import traceback
import unittest
import uuid

import click.testing
import git

from ginteract import main


def click_runner(func):
    def wrapper(instance, *args, **kwargs):
        runner = click.testing.CliRunner()
        result = func(instance, runner, *args, **kwargs)

        if result.exit_code != 0:
            etype, value, tb = result.exc_info
            print(''.join(traceback.format_exception(etype, value, tb)))
            raise Exception('Exit code is {}'.format(result.exit_code))

    return wrapper


class TestMain(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        os.chdir(self.tmpdir.name)

        self.repo = git.Repo.init(self.tmpdir.name)
        self.make_commit()

        self.repo.create_head('branch0')
        self.make_commit()

        self.repo.create_head('branch1')
        self.make_commit()

    def make_commit(self):
        filename = str(uuid.uuid4())
        path = os.path.join(self.tmpdir.name, filename)
        with open(path, 'w') as fp:
            fp.write(filename)  # write filename to file
        self.repo.index.add([path])
        self.repo.git.commit('-m', filename)

    @click_runner
    def test_checkout(self, runner):
        result = runner.invoke(main.checkout, input='branch0')
        assert str(self.repo.active_branch) == 'branch0'
        return result

    @click_runner
    def test_merge(self, runner):
        self.repo.git.checkout('master')
        result = runner.invoke(main.merge, input='branch1')
        assert 3 == len(list(self.repo.iter_commits('master')))
        return result

    @click_runner
    def test_delete(self, runner):
        result = runner.invoke(main.delete, input='branch0 branch1\ny')
        assert 1 == len(self.repo.branches)
        return result

    def tearDown(self):
        self.tmpdir.cleanup()
