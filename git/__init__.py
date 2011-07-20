import subprocess
import os


class Repository(object):
    """
    Instances of this class refer to a git repository on this machine.
    """
    path = ""
    git = ""

    def __init__(self, path, git="git"):
        """
        Sets up this repository.
        """
        self.path = os.path.abspath(path)
        if git.endswith("git"):
            self.git = git
        else:
            raise ValueError("Please provide a valid Git command")

    def cmd(self, command, *args):
        """
        Runs a git command on this repository.
        """
        arg_list = [self.git, command] + list(args)
        process = subprocess.Popen(arg_list,
                                   cwd=self.path,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,)
        (out, err) = process.communicate()
        self.out = out
        self.err = err
        return (out, err)

    # shortcuts
    def add(self, filename, *args):
        """
        Helper for `git add`.
        """
        return self.cmd('add', filename, *args)

    def commit(self, message, author, *args):
        """
        Helper for `git commit`.
        """
        return self.cmd('commit', '-m ' + message, '--author=', *args)

    def status(self, *args):
        """
        Helper for `git status`.
        """
        return self.cmd('status', *args)

    def checkout(self, checkout, *args):
        """
        Helper for `git checkout`.
        """
        return self.cmd('checkout', checkout, *args)

    def pull(self, remote, branch, *args):
        """
        Helper for `git pull`.
        """
        return self.cmd('pull', remote, branch, *args)

    def push(self, remote, branch, *args):
        """
        Helper for `git pull`.
        """
        return self.cmd('push', remote, branch, *args)
