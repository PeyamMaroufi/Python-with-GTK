import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class secondtut(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My second Tutorial")
        self.set_border_width(10)
        self.set_size_request(400, 600)
        
        box_out = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(box_out)
        
        # Making a listbox for simplicity
        # 1. First make a ListBox
        # 2. Make a ListBoxRow
        # 3. Make a Box
        # 4. Add the box to the listbox row       
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_out.pack_start(listbox, True, True, 0)     
        listbox_row = Gtk.ListBoxRow()
        
        # Make a horizontal box and then add it to the row
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        listbox_row.add(hbox)
        
        # Make a vertical box and then add it to the horizontal one. 
        # because we will have some vertical and horizontal stuff in the upper
        # row of the listbox
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing =5)
        hbox.pack_start(vbox, True, True, 0)
        
        # label name
        lbName = Gtk.Label("Automatic date & Time", xalign=0)
        lbLastName = Gtk.Label("Require internet acces", xalign=0)
        vbox.pack_start(lbName, True, True, 0)
        vbox.pack_start(lbLastName, True, True, 0)
        
        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switch, False, True, 0)
        # Add to the listbox
        listbox.add(listbox_row)
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation =Gtk.Orientation.HORIZONTAL, spacing = 50)
        row.add(hbox)
        
        label = Gtk.Label("Enable Automatic Update", xalign=0)
        check = Gtk.CheckButton()
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(check, False, True, 0)
        
        listbox.add(row)
        
        
        
win = secondtut()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
        
        
        
        
        
        
        