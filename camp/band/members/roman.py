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

from camp.band.members.member import Member
from camp.notation.roman import Roman as RomanNotation

class Roman(Member):

    """
    The roman player listens to an incoming note signal and then only really pays attention to the velocity, duration, and scale data.
    The actual note played depends on a symbol off the scale, whether a note or a chord.

    As such, a ScaleSource makes the most sense to have higher up in the chain.

    For instance:

    r = RomanPlayer(symbols="I 2 3 4 IV 2 3 4 iii".split())
    """

    def __init__(self, symbols=None, channel=None):

        """
        scales - a list of what scales to play
        lengths - how many notes to play in each scale
        note_durations - a list of how long should each note be
        note_velocities - how loud should each note be
        channel - what MIDI channel to send to?
        """

        super().__init__(channel=channel)
        self._symbols = symbols
        self.reset()

    def reset(self):

        self.symbol_looper = self.draw_from(self._symbols)

    def on_signal(self, event, start_time, end_time):


        scale = event.flags.get('scale',None)
        if scale is None:
            raise Exception("missing scale data from note signal, something wrong here")

        try:
            symbol = next(self.symbol_looper)
        except StopIteration:
            return []

        event.notes = RomanNotation(scale=scale).do_notes(symbol)

        for send in self.sends:
            send.signal(event, start_time, end_time)

        return [ event ]
