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
from lettuce.registry import world
from lettuce.registry import CALLBACK_REGISTRY
world._set = True

def absorb(thing, name=None):
    if not isinstance(name, basestring):
        name = thing.__name__

    setattr(world, name, thing)
    return thing

world.absorb = absorb

@world.absorb
def spew(name):
    if hasattr(world, name):
        item = getattr(world, name)
        delattr(world, name)
        return item

class Main(object):
    def __init__(self, callback):
        self.name = callback

    @classmethod
    def _add_method(cls, name, where, when):
        def method(self, fn):
            full_name = "%" in when and when % (self.name) or when
            CALLBACK_REGISTRY.append_to(where, full_name, fn)
        method.__name__ = method.fn_name = name
        setattr(cls, name, method)

for name, where, when in (
        ('all', 'all', '%s'),
        ('each_step', 'step', '%s_each'),
        ('each_scenario', 'scenario', '%s_each'),
        ('each_feature', 'feature', '%s_each'),
        ('harvest', 'harvest', '%s'),
        ('each_app', 'app', '%s_each'),
        ('runserver', 'runserver', '%s'),
        ('handle_request', 'handle_request', '%s'),
        ('outline', 'scenario', 'outline')):
    Main._add_method(name, where, when)

before = Main('before')
after = Main('after')
