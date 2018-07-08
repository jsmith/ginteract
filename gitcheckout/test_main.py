import os
import tempfile
import traceback
import unittest.mock

import click.testing
import git

from gitcheckout import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        os.chdir(self.tmpdir.name)

        self.repo = git.Repo.init(self.tmpdir.name)

        path = os.path.join(self.tmpdir.name, 'test.txt')
        with open(path, 'w') as fp:
            fp.write('test text')

        self.repo.index.add([path])
        self.repo.git.commit('-m', 'test commit')

        self.repo.create_head('branch0')
        self.repo.create_head('branch1')

    @staticmethod
    def format_traceback(result):
        etype, value, tb = result.exc_info
        return ''.join(traceback.format_exception(etype, value, tb))

    @unittest.mock.patch('click.prompt', return_value='branch0')
    def test_checkout(self, _):
        runner = click.testing.CliRunner()
        result = runner.invoke(main.checkout)
        assert result.exit_code == 0
        assert str(self.repo.active_branch) == 'branch0'

    def tearDown(self):
        self.tmpdir.cleanup()
