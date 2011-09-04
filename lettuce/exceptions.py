# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010-2011>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import traceback


class NoDefinitionFound(Exception):
    """ Exception raised by lettuce.core.Step, when trying to solve a
    Step, but does not find a matching step definition.

    This exception should never be visible to the user. It is only used so
    lettuce can filter undefined steps.
    """
    def __init__(self, step):
        self.step = step
        # old school for python 2.4
        Exception.__init__(self,
            'The step r"%s" is not defined' % self.step.sentence
        )


class ReasonToFail(object):
    """ Exception that contains detailed information about a
    AssertionError raised within a step definition.  With these data
    lettuce show detailed traceback to user in a nice representation.
    """
    def __init__(self, exc):
        self.exception = exc
        self.cause = unicode(exc)
        self.traceback = traceback.format_exc(exc)


class LettuceSyntaxError(SyntaxError):
    def __init__(self, filename, string):
        self.filename = filename
        self.msg = "Syntax error at: %s\n%s\n" % (filename, string)


class StepLoadingError(Exception):
    """Raised when a step cannot be loaded."""
    pass
