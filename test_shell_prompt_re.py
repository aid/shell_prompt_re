#!/usr/bin/env python3

import unittest
import re
from dataclasses import dataclass

SHELL_RE = re.compile(r'^\[?(\w+)@([\w\d-]+)[:\s]([\w~/ ]*[\w~/]+)\]?(?:\s%|\s#|\$|#)\s')

@dataclass
class TestData:
    prompt: str
    username: str
    hostname: str
    directory: str

# Prompt obtained on MacOS 12 using the default ZSH shell
ZSH_DATA = {
    'zsh_home':                 TestData('aid@mac ~ % ',                'aid',  'mac',         '~'),
    'zsh_tmp':                  TestData('aid@mac tmp % ',              'aid',  'mac',         'tmp'),
    'zsh_space':                TestData('aid@mac GOOGLE CLOUD % ',     'aid',  'mac',         'GOOGLE CLOUD'),
    'zsh_root_dir':             TestData('aid@mac / % ',                'aid',  'mac',         '/'),
    'zsh_root_user_home':       TestData('root@mac ~ # ',               'root', 'mac',         '~'),
    'zsh_host_hash_home':       TestData('aid@mac-test ~ % ',           'aid',  'mac-test',    '~'),
}

# Prompts obtained on an Ubuntu Linux 18 system using the default BASH shell
BASH_DATA = {
    'bash_home':                TestData('aid@linux:~$ ',               'aid',  'linux',         '~'),
    'bash_tmp':                 TestData('aid@linux:~/tmp$ ',           'aid',  'linux',         '~/tmp'),
    'bash_root':                TestData('aid@linux:/$ ',               'aid',  'linux',         '/'),
    'bash_space':               TestData('aid@linux:~/GOOGLE DRIVE$ ',  'aid',  'linux',         '~/GOOGLE DRIVE'),
    'hash_host_hash_home':      TestData('aid@linux-test:~$ ',          'aid',  'linux-test',    '~'),
    'bash_root_user_home':      TestData('root@linux:~# ',              'root', 'linux',         '~'),
}

# Prompts obtained/fabricated for a Linux system running on Google Cloud Compute with the ZSH shell
GCP_DATA = {
    'test_gcp_home':            TestData('[user@gcp ~]$ ',              'user',  'gcp',         '~'),
    'test_gcp_tmp':             TestData('[user@gcp tmp]$ ',            'user',  'gcp',         'tmp'),
    'test_gcp_root_dir':        TestData('[user@gcp /]$ ',              'user',  'gcp',         '/'),
    'test_gcp_space':           TestData('[user@gcp ~/GOOGLE DRIVE]$ ', 'user',  'gcp',         '~/GOOGLE DRIVE'),
    'test_gcp_host_dash_home':  TestData('[user@gcp-test ~]$ ',         'user',  'gcp-test',    '~'),
    'test_gcp_root_user_home':  TestData('[root@gcp ~]# ',              'root',  'gcp',         '~'),
}

class TestZsh(unittest.TestCase):
    def test_zsh(self):
        for name, test in ZSH_DATA.items():
            with self.subTest(msg=name, prompt=test.prompt):
                match = SHELL_RE.match(test.prompt)
                self.assertIsNotNone(match, "Failed to match {name}")
                self.assertEqual(match.group(1), test.username)
                self.assertEqual(match.group(2), test.hostname)
                self.assertEqual(match.group(3), test.directory)


class TestBash(unittest.TestCase):
    def test_bash(self):
        for name, test in BASH_DATA.items():
            with self.subTest(msg=name, prompt=test.prompt):
                match = SHELL_RE.match(test.prompt)
                self.assertIsNotNone(match, "Failed to match {name}")
                self.assertEqual(match.group(1), test.username)
                self.assertEqual(match.group(2), test.hostname)
                self.assertEqual(match.group(3), test.directory)


class TestGCP(unittest.TestCase):
    def test_bash(self):
        for name, test in GCP_DATA.items():
            with self.subTest(msg=name, prompt=test.prompt):
                match = SHELL_RE.match(test.prompt)
                self.assertIsNotNone(match, "Failed to match {name}")
                self.assertEqual(match.group(1), test.username)
                self.assertEqual(match.group(2), test.hostname)
                self.assertEqual(match.group(3), test.directory)


if __name__ == '__main__':
    unittest.main()
