# Shell Prompt Regular Expression

## Introduction

This repository stores a Python-compatible regular expression used to match on the login prompts offered by a number of systems along with a number of test cases to test validity of the regex.

At the time of writing, the regular expression is,

```
^\[?(\w+)@([\w\d-]+)[:\s]([\w~/ ]*[\w~/]+)\]?(?:\s%|\s#|\$|#)\s
```


This regular expression includes three captures:

1. Username
2. Hostname
3. Directory

This regular expression was created to extract username, hostname and directory values from a shell prompt within iTerm2's Trigger functionality.

_(iTerm2 is popular terminal emulator for Apple Mac computers.)_

## Use

This script uses the `unittest` library built into Python; so no additional installations are required beyond a Python3 installation.

Simply start `python3`, giving the name of this script; the output should be similar to the following:

```
$ python3 test_shell_prompt_re.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

If you had other prompts that do not match on this regex; provide them and we'll try to integrate them into the regex if it doesn't make the regex too crazy.

