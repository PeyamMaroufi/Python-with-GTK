import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
import sys


class youtubeD(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Youtube Download GTK", application=app)
        self.set_border_width(10)
        self.set_size_request(500, 600)

        # HEADERBAR
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Youtube Downloader"
        self.set_titlebar(hb)

        btnSetting = Gtk.Button()
        icon = Gio.ThemedIcon(name="applications-system")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        btnSetting.add(image)
        hb.pack_end(btnSetting)
        # # END HEADERBAR

        # The main
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(main_box)

        # ## UPPER BOX
        first_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        first_box.set_border_width(4)

        # # Button with image
        hbox = Gtk.HBox()
        hbox.set_halign(Gtk.Align.CENTER)

        add_button = Gtk.Button()
        plus_icon = Gio.ThemedIcon(name="list-add")
        image = Gtk.Image.new_from_gicon(plus_icon, Gtk.IconSize.BUTTON)
        add_button.add(image)
        add_button.connect("clicked", self.on_btnAdd_click)
        # # END Button with label

        # # Label
        newLabel = Gtk.Label()
        newLabel.set_markup("<span font='Ubuntu 9' font_weight='normal'>Add new download</span>")
        # # END Label

        # # Label with icon and Combobox
        """
         Image
         label
         Combobox
         """
        lbWithIcon = Gtk.HBox()
        lbWithIcon.set_halign(Gtk.Align.END)

        Yimage = Gtk.Image()
        Yimage.set_from_icon_name("applications-multimedia", 4)

        lbOutputType = Gtk.Label()
        lbOutputType.set_markup("<span font='Ubuntu 9' font_weight='normal'> Output type: </span>")

        cbOutput = Gtk.ComboBoxText()
        output_vector = ["Custom","Video", "Audio"]
        for output in output_vector:
            cbOutput.append_text(output)

        cbOutput.set_entry_text_column(0)
        # # END Label with icon and Combobox


        # # ADDING TO LAYOUT
        hbox.pack_start(add_button, False, False, 0)
        hbox.pack_start(newLabel, False, False, 4)
        lbWithIcon.pack_start(Yimage, False, False, 0)
        lbWithIcon.pack_start(lbOutputType, False, False, 0)
        lbWithIcon.pack_start(cbOutput, False, False, 4)
        first_box.pack_start(hbox, False, False, 0)
        first_box.pack_start(lbWithIcon, True, True, 0)
        main_box.pack_start(first_box, False, True, 0)
        # # END ADDING TO LAYOUT
        # ## END UPPER BOX

        # ## THE DOWN BOX CONSISTING OF A LISTBOX
        self.downBox = Gtk.ListBox()
        self.downBox.set_selection_mode(Gtk.SelectionMode.NONE)
        # main_box.pack_start(self.downBox, True, True, 0)

        """
        Making a row
        Making a horizontal box downBox_main
        place pic in the horisontal box first,
        Make a vertical box and Put link in the box, make a horizontal box and place it in the vertical one with buttons
        Make a radiobuttons in a vertical box and Download button and place them in downBox_main
        """
        # # Row in Listbox
        row = Gtk.ListBoxRow()
        row.set_border_width(5)

        downBox_main = Gtk.HBox()
        downBox_main.set_halign(Gtk.Align.CENTER)

        videoIcon = Gio.ThemedIcon(name="audio-x-generic")
        videoImage = Gtk.Image.new_from_gicon(videoIcon, Gtk.IconSize.DIALOG)

        vbox_link_and_butons = Gtk.VBox()
        vbox_link_and_butons.set_border_width(5)

        link_entry = Gtk.Entry()
        link_entry.set_placeholder_text("Paste the video link here")

        quality_hbox = Gtk.HBox()

        btnsQuality = [("4320p"), ("2160p"), ("1440p"), ("1080p"), ("720p"), ("480p")]
        for buttonNames in btnsQuality:
            btn = Gtk.ToggleButton()
            btn.set_label(buttonNames)
            quality_hbox.pack_start(btn, False, False, 2)

        radiobtn_box = Gtk.VBox()
        radiobtn_box.set_valign(Gtk.Align.CENTER)

        rbVideo = Gtk.RadioButton.new_with_label_from_widget(None, "Video")
        rbAudio = Gtk.RadioButton.new_from_widget(rbVideo)
        rbAudio.set_label("Audio")

        btnDownload = Gtk.Button()
        download_icon = Gio.ThemedIcon(name="down")
        image = Gtk.Image.new_from_gicon(download_icon, Gtk.IconSize.BUTTON)
        btnDownload.add(image)

        # # ADDING TO LAYOUT
        downBox_main.pack_start(videoImage, False, False, 0)
        vbox_link_and_butons.pack_start(link_entry, True, True, 0)
        vbox_link_and_butons.pack_start(quality_hbox, True, True, 3)
        radiobtn_box.pack_start(rbVideo, False, True, 0)
        radiobtn_box.pack_start(rbAudio, False, True, 0)
        downBox_main.pack_start(vbox_link_and_butons, True, False, 8)
        downBox_main.pack_start(radiobtn_box, True, True, 0)
        downBox_main.pack_start(btnDownload, True, True, 3)
        row.add(downBox_main)
        self.downBox.add(row)
        self.win_scroll = Gtk.ScrolledWindow()
        self.win_scroll.add(self.downBox)
        self.win_scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.win_scroll.set_min_content_height(100)
        main_box.pack_start(self.win_scroll, True, True, 0)
        # # END ADDING TO LAYOUT
        # ## END THE DOWN BOX CONSISTING OF A LISTBOX


    ### METHODS
    def on_btnAdd_click(self, widget):

        row = Gtk.ListBoxRow()
        row.set_border_width(5)

        downBox_main = Gtk.HBox()
        downBox_main.set_halign(Gtk.Align.CENTER)

        videoIcon = Gio.ThemedIcon(name="audio-x-generic")
        videoImage = Gtk.Image.new_from_gicon(videoIcon, Gtk.IconSize.DIALOG)

        vbox_link_and_butons = Gtk.VBox()
        vbox_link_and_butons.set_border_width(5)

        link_entry = Gtk.Entry()
        link_entry.set_placeholder_text("Paste the video link here")

        quality_hbox = Gtk.HBox()

        btnsQuality = [("4320p"), ("2160p"), ("1440p"), ("1080p"), ("720p"), ("480p")]
        for buttonNames in btnsQuality:
            btn = Gtk.ToggleButton()
            btn.set_label(buttonNames)
            quality_hbox.pack_start(btn, False, False, 2)

        radiobtn_box = Gtk.VBox()
        radiobtn_box.set_valign(Gtk.Align.CENTER)

        rbVideo = Gtk.RadioButton.new_with_label_from_widget(None, "Video")
        rbAudio = Gtk.RadioButton.new_from_widget(rbVideo)
        rbAudio.set_label("Audio")

        btnDownload = Gtk.Button()
        download_icon = Gio.ThemedIcon(name="down")
        image = Gtk.Image.new_from_gicon(download_icon, Gtk.IconSize.BUTTON)
        btnDownload.add(image)

        downBox_main.pack_start(videoImage, False, False, 0)
        vbox_link_and_butons.pack_start(link_entry, True, True, 0)
        vbox_link_and_butons.pack_start(quality_hbox, True, True, 3)
        radiobtn_box.pack_start(rbVideo, False, True, 0)
        radiobtn_box.pack_start(rbAudio, False, True, 0)
        downBox_main.pack_start(vbox_link_and_butons, True, False, 8)
        downBox_main.pack_start(radiobtn_box, True, True, 0)
        downBox_main.pack_start(btnDownload, True, True, 3)
        row.add(downBox_main)
        self.downBox.add(row)
        self.downBox.show_all()


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = youtubeD(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)