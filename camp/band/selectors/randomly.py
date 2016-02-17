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

from camp.band.selectors.selector import Selector

import random

def endlessly_generate(alist):

    while True:

        choice = random.choice(alist)

        if type(choice) == dict:
            value = choice.get('value', None)
            length = choice.get('hold', 1)
            if value is None:
                raise Exception("expecting value in choice expression, usage of Randomly is munged")
            for count in range(0, length):
                yield value
        else:
            yield choice

class Randomly(Selector):

    # see examples/11_randomness.py for usage

    # TODO: implement serialism by allowing a serialism=True flag which will pop
    # the item off the list once consumed.  When done, update comments in 11_randomness.py
    # to show the example.

    def __init__(self, alist):
        self.data = alist
        self.my_generator = endlessly_generate(alist)

        random.seed()


    def draw(self):
        result = next(self.my_generator)
        return result