#-------------------------------------------------------------------------------
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright 2019 Payam Maroufi
#-------------------------------------------------------------------------------
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class settingWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Settings')
        self.set_border_width(10)
        self.set_size_request(400, 100)

        main_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(main_box)

        # # First row, Directory
        bxFolder_box = Gtk.HBox()
        txtDown = Gtk.Label()
        txtDown.set_markup("<span font='Ubuntu 9' font_weight='normal'>Download directory: </span>")

        entDown = Gtk.Entry()
        entDown.set_placeholder_text("Default")

        btnBrowse = Gtk.Button("Browse")
        # # END First row, Directory

        # # Second Row, Number of max Download
        bxNumDown = Gtk.HBox()
        txtNumDown = Gtk.Label()
        txtNumDown.set_markup("<span font='Ubuntu 9' font_weight='normal'>Max number of downloads: </span>")
        adjustment = Gtk.Adjustment(0, 0, 20, 1, 10, 0)
        sbtnMaxDowns = Gtk.SpinButton()
        sbtnMaxDowns.set_adjustment(adjustment)

        # # ADD TO LAYOUT
        bxFolder_box.pack_start(txtDown, False, False, 0)
        bxFolder_box.pack_start(entDown, False, False, 3)
        bxFolder_box.pack_start(btnBrowse, True, True, 0)
        bxNumDown.pack_start(txtNumDown, False, True, 0)
        bxNumDown.pack_start(sbtnMaxDowns, True,True, 3)
        main_box.pack_start(bxFolder_box, False, False, 0)
        main_box.pack_start(bxNumDown, False, False, 0)

