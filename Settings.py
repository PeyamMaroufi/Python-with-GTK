import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class settingWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Settings')
        self.set_border_width(10)
        self.set_size_request(300, 200)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(main_box)

        # # First row, Directory
        bxFolder_box = Gtk.HBox()
        txtDown = Gtk.Label()
        txtDown.set_label("Download directory: ")

        entDown = Gtk.Entry()
        entDown.set_placeholder_text("Default")

        btnBrowse = Gtk.Button("Browse")
        # # END First row, Directory

        # # Second Row, Number of max Download
        bxNumDown = Gtk.HBox()
        txtNumDown = Gtk.Label()
        txtNumDown.set_label("Max number of downloads: ")


        # # ADD TO LAYOUT
        bxFolder_box.pack_start(txtDown, False, False, 0)
        bxFolder_box.pack_start(entDown, False, False, 0)
        bxFolder_box.pack_start(btnBrowse, False, False, 0)
        bxNumDown.pack_start(txtNumDown, False, False, 0)
        main_box.pack_start(bxFolder_box, True, True, 0)
        main_box.pack_start(bxNumDown, True, True, 0)



win = settingWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()