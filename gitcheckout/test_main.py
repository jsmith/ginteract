import unittest

from gitcheckout.main import parse_git_branches, BranchesInfo, branches_menu, DETACHED_HEAD_BRANCH_NAME


class TestParseGitBranches(unittest.TestCase):
    def test_normal_output(self):
        output = 'master\n  test\n* new-features\n'
        b = parse_git_branches(output)
        self.assertEqual(b.current_branch, 'new-features')
        self.assertEqual(b.current_index, 2)
        self.assertEqual(b.all_branches[0], 'master')
        self.assertEqual(b.all_branches[1], 'test')
        self.assertEqual(b.all_branches[2], 'new-features')

    def test_detached_head(self):
        output = '* (no branch)\n  master\n'
        b = parse_git_branches(output)
        self.assertEqual(b.current_branch, DETACHED_HEAD_BRANCH_NAME)
        self.assertEqual(b.current_index, 0)
        self.assertEqual(b.all_branches[0], DETACHED_HEAD_BRANCH_NAME )
        self.assertEqual(b.all_branches[1], 'master')


class TestBranchesMenu(unittest.TestCase):
    def test_menu(self):
        all_branches = ['master', 'docs', 'test']
        b = BranchesInfo(all_branches, 'docs', 1)
        self.assertEqual(branches_menu(b), '''
Current branch: docs
0  master
1  docs
2  test
''')
