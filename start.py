import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
class start(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='My Window')
        self.set_border_width(10)
        self.set_size_request(400, 600)
        
        vbox = Gtk.Box(spacing=10)
        self.add(vbox)
        
        button1 = Gtk.Button(label="Click me first")
        button1.connect("clicked", self.on_button1_clicked)
        button2 = Gtk.Button(label="Click me later")
        button2.connect("clicked", self.on_button2_clicked)
        vbox.pack_start(button1, True, True, 0)
        vbox.pack_start(button2, True, True, 0)
        
    def on_button1_clicked(self, widget):
        print("HI")
    
    
    def on_button2_clicked(self, widget):
        print("HI second")
        
 
win = start()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
        
        
        
