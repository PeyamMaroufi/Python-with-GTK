import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class youtubeD(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Youtube Download GTK")
        self.set_border_width(10)
        self.set_size_request(500, 600)
        
        # Headerbar
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Youtube Downloader"
        self.set_titlebar(hb)
        
        # The main
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(main_box)
        
        ## The upper box with a frame
        f = Gtk.Frame()
        first_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        first_box.set_border_width(4)
        f.set_shadow_type(Gtk.ShadowType.IN)
        f.add(first_box)
        
        # Adding box to the first box
        add_button = Gtk.Button()
        plus_icon = Gio.ThemedIcon(name="list-add")
        image = Gtk.Image.new_from_gicon(plus_icon, Gtk.IconSize.BUTTON)
        add_button.add(image)
        
        ## Label with icon
        lbWithIcon = Gtk.HBox()
        lbWithIcon.set_halign(Gtk.Align.CENTER)
        # Image
        Yimage = Gtk.Image()
        Yimage.set_from_icon_name("applications-multimedia", 4)
        lbWithIcon.pack_start(Yimage, False, False, 0)
        # label
        lbOutputType = Gtk.Label()
        lbOutputType.set_markup("<span font='Ubuntu 10' font_weight='normal'> Output type: </span>")
        lbWithIcon.pack_start(lbOutputType, False, False, 0)
        
        # Combobox
        cbOutput= Gtk.ComboBoxText()
        output_vector = ["Video", "Audio"]
        for output in output_vector:
            cbOutput.append_text(output)
        
        cbOutput.set_entry_text_column(0)
         
        ## ADDING TO MAIN LAYOUT     
        # Add button to the first box
        first_box.pack_start(add_button, False, False, 0)
        first_box.pack_start(lbWithIcon, True, True, 0)
        first_box.pack_end(cbOutput, False, False, 0)
        # Add first box to the main box
        main_box.pack_start(f, False, True, 0)
        
        
win = youtubeD()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()        