# -*- coding: utf-8 -*-
# This file is part of beets.
# Copyright 2019, Schuyler Eldridge.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

"""An Aura RESFTful interface to beets."""
from __future__ import division, absolute_import, print_function

from beets.plugins import BeetsPlugin
from beets.ui import Subcommand

import flask

app = flask.Flask(__name__)

class Serve(BeetsPlugin):
    def __init__(self):
        super(Serve, self).__init__()
        self.config.add({
            'host': u'127.0.0.1',
            'port': 8338,
            'prefix': 'aura',
        })


    def commands(self):
        cmd = Subcommand('serve', help=u'start an Aura server')

        def func(lib, opts, args):
            print("Starting server...")

            app = App(self.config['prefix'])

            app.run( host=self.config['host'].as_str(),
                     port=self.config['port'].get(int),
                     threaded=True )

        cmd.func = func
        return [cmd]

    pass
