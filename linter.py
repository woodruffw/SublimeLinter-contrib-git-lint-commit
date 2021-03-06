#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by William Woodruff <william@yossarian.net>
# Copyright (c) 2017 William Woodruff <william@yossarian.net>
#
# License: MIT
#

"""This module exports the GitLintCommit plugin class."""

from SublimeLinter.lint import Linter, util


class GitLintCommit(Linter):
    """Provides an interface to git-lint-commit."""

    cmd = "git-lint-commit -"
    regex = r"^(?:(?P<warning>W)|(?P<error>E)): Line (?P<line>\d+): (?P<message>.+)"
    error_stream = util.STREAM_BOTH
    line_col_base = (1, 1)
    defaults = {"selector": "text.git.commit"}
