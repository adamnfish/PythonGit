=========
PythonGit
=========

If you want to control a Git repository from Python, you should use
GitPython.

If however, you were just going to run shell commands from Python then
save yourself the hassle of writing it and use this.

GitPython is just a collection of functions that will execute shell
commands to manage the repository.

Requirements
============

* Git

Since PythonGit merely executes shell commands to control the
repository, it must be installed on your system for this library to
work.

Install
=======

Download the source code from Github and run setup.py

Usage
=====

Import the git module, or specifically import the Repository class
therefrom.

    from git import Repository

Create an instance of the Repository class, providing the path to the
repository. This path will be run through `os.path.abspath` and used
as the `cwd` for git commands.

    repo = Repository("/path/to/repository/")

Repositories contain the following methods.

All the methods listed here return tuples containing the resulting
STDOUT and STDERR. Additionally, the instance's `out` and `err`
properties will always contain the STDOUT and STDERR respectively from
the last method called.

add
---

    repo.add(filename, *args)

The add method runs `git add <filename> [args1, ... ]` in the repository.

commit
------

    repo.commit(message, author, *args)

This method runs `git commit -m <message> --author=<author> [args1, ... ]` in the repository.

status
------

    repo.status(*args)

This is a method to run `git status  [args1, ... ]` in the repository.

checkout
--------

    repo.checkout(checkout, *args)

The checkout method runs `git checkout  [args1, ... ]` in the repository.

pull
----

    repo.pull(remote, branch, *args)

This method runs `git pull <remote> <branch> [args1, ... ]` in the repository.

push
----

    repo.push(remote, branch, *args)

The push method runs `git push <remote> <branch>  [args1, ... ]` in the repository.

cmd
---

    repo.cmd(command, *args)

This is the method used internally by the specific git command methods. It is a flexible interface to the git repository. If you need to use a git command that does not have a method built-in you can use this directly. The first argument is the git command to run and subsequent arguments are passed to it.
