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

from camp.tracker.song_factory import SongFactory
from camp.tracker.defaults import Defaults
from camp.tracker.instruments import Instruments
from camp.tracker.instrument import Instrument
from camp.tracker.patterns import RandomPatterns, BasicPatterns, EndlessPatterns
from camp.tracker.fx_buses import FxBuses
from camp.tracker.fx_bus import FxBus
from camp.tracker.scenes import Scenes
from camp.tracker.scene import Scene

# ---------------------------------------------------------------------------------
# WARNING -- THIS EXAMPLE IS UNDER DEVELOPMENT CURRENTLY
# AND IS NOT YET OPERATIONAL.  This also applies to the whole camp.tracker
# namespace.

# The next step after this is to build the generative API *on top* of the Tracker API
# as this manages instrument routing for us and is therefore easier to think about
# ----------------------------------------------------------------------------------

# a demo of using the Tracker API from Python to define compositions
# with somewhat less flexible routing but easier data entry
# SUBJECT TO CHANGE - MASSIVELY

def play():

    # We are building a house of fire, baby.

    song = SongFactory(
        name='Foo',
        author='Your Name'
    )

    song.set(

        Defaults().set(
            bpm = 120,
            scene_bar_count = 8
        ),

        # -- INSTRUMENTS --
        Instruments().set(
            strings = Instrument(channel=1),
            lead    = Instrument(channel=2),
            drums   = Instrument(channel=3, notation='literal')
        ),

        # -- PATTERNS --
        RandomPatterns(mode='probability').set(
            chordify_chance_pt = [ 0, 0.5 ]
        ),

        BasicPatterns().set(
            some_jam_pt1 = "4 6 1 6 | 4 4 4 4 | 6 6 4 1 | 1 4 6 4 | 6 4 4 4 | 4 6 4 6",
            some_jam_pt2 = "1 2 3 4 | 3 2 5 1 | 1 1 7 6 | 5 4 3 2 | 1 2 3 4 | 5 6 7 1"
        ),

        RandomPatterns(mode='choice').set(
            random_pt1 = "1 2 3 4 5 6 7",
            transpose_pt1 = [ 2, 0, -2 ]
        ),

        EndlessPatterns().set(
        ),

        # --- FX ---
        FxBuses().set(
            arpeggiate_strings = FxBus().set([
                dict(module='arp', splits=[4], octaves='transpose_pt1', mode='locked')
            ]),
            random_velocity_and_duration = FxBus().set([
                dict(module='velocity', levels='velocity_pt1'),
                dict(module='duration', lengths='duration_pt1')
            ]),
            chordify_lead = FxBus().set([
                dict(module='chordify', types='chordify_pt1', when='chordify_chance_pt1')
            ]),
            tranpose_lead = FxBus().set([
                dict(module='transpose', octaves='transpose_pt1')
            ])
        ),

        # -- SCENES --
        Scenes().set(
            overture = Scene().set(
                scale = "C4 major",
                bar_count = 12,
                pre_fx = dict(strings='random_velocity_and_duration'),
                post_fx = dict(strings='arpeggiate_strings', lead='transpose_lead'),
                patterns = dict(strings='basic_chords', lead=[ 'some_jam_pat', 'some_jam2_pat' ])
            ),
            llama_theme = Scene().set(
                scale = "C4 major",
                bar_count = 12,
                pre_fx = dict(strings = 'random_velocity_and_duration'),
                post_fx = dict(strings = 'arpeggiate_strings', lead = 'transpose_lead'),
                patterns = dict(strings = 'basic_chords', lead = [ 'some_jam_pat', 'some_jam2_pat' ])
            )
        )

    )

    # -- GO! --

    scene_names = ['overture', 'llama_theme']
    song.play(scene_names)



if __name__ == "__main__":
    play()
