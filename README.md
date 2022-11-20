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

