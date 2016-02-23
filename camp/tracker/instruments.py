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

from camp.tracker.instrument import Instrument

class Instruments(object):

    __slots__ = [ "_instruments", "_factory" ]

    def __init__(self):
        self._instruments = dict()

    def set(self, **kwargs):

        def callback(song):

            for (instrument_name, instrument) in kwargs.items():

                if getattr(instrument, '__call__', None) is not None:
                    print("YAY?")
                    instrument = instrument(song)

                if type(instrument) != Instrument:
                    raise Exception("instruments collection requires an instrument")

                self._instruments[instrument_name] = instrument

            return self
        return callback

    def as_dict(self):
        return self._instruments