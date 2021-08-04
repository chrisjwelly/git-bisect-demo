# Git Bisect Demo

This repository is an accompanying demo repository for my blog post: [Binary Searching bugs with Git Bisect](https://chrisjwelly.github.io/blog/2021/08/03/binary-searching-bugs-with-git-bisect/).

It is specifically designed such that it has more than a thousand commits with one "bad commit", in order to demonstrate how that "bad commit" can be identified quickly via [Git Bisect](https://git-scm.com/docs/git-bisect).

The repository contains 3 files:

- `good.txt`: changes to this file represents a "good commit"
- `bad.txt`: changes to this file represents a "bad commit"
- `bisect_demo_script.py`: to generate all the dummy commits required for an effective demo
