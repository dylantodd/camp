"""
Copyright 2016, Michael DeHaan <michael.dehaan@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import importlib

def loop_around(alist):
    """
    Returns a generator that keeps looping around a pattern
    """
    while True:
        for item in alist:
            yield item

def roll_left(x):
    """
    Circularly shifts a list to the left
    [ 1,2,3] -> [2,3,1]
    """
    new_list = x[:]
    first = new_list.pop(0)
    new_list.append(first)
    return new_list

def roll_right(x):
    """
    Circularly shifts a list to the right
    [1,2,3] -> [3,1,2]
    """
    new_list = x[:]
    first = new_list.pop()
    new_list.insert(0, first)
    return new_list

def instance_produce(namespace, class_name, args, kwargs):
    """
    Produce a class by name.
    """
    mod= importlib.import_module(namespace)
    cls = getattr(mod, class_name.title())
    return cls(*args, **kwargs)

def exclude_dict(orig, keys):
    """
    Given a dictionary, return a new one without certain keys.
    """
    new = dict()
    for (k,v) in orig.items():
        if k not in keys:
            new[k] = v
    return new
