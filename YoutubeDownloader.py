#-------------------------------------------------------------------------------
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright 2019 Payam Maroufi
#-------------------------------------------------------------------------------
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk
import Downloader
import sys


# lists of rbbttons
lst_rbVideo = []
lst_rbMusic = []

class youtubeD(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Youtube Download GTK", application=app)
        self.set_border_width(10)
        self.set_size_request(620, 500)

        # HEADERBAR
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Youtube Downloader"
        self.set_titlebar(hb)

        btnSetting = Gtk.Button()
        icon = Gio.ThemedIcon(name="applications-system")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        btnSetting.add(image)
        btnSetting.connect("clicked", self.on_btnSetting_clicked)
        hb.pack_end(btnSetting)
        # END HEADERBAR

        # The main
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(main_box)

        # ## UPPER BOX
        first_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        first_box.set_border_width(4)

        # ## Button with image
        hbox = Gtk.HBox()
        hbox.set_halign(Gtk.Align.CENTER)

        add_button = Gtk.Button()
        plus_icon = Gio.ThemedIcon(name="list-add")
        image = Gtk.Image.new_from_gicon(plus_icon, Gtk.IconSize.BUTTON)
        add_button.add(image)
        # ## END Button with label

        # ## Label
        newLabel = Gtk.Label()
        newLabel.set_markup("<span font='Ubuntu 9' font_weight='normal'>Add new download</span>")
        # ## END Label

        # ## Label with icon and Combobox
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
        output_vector = ["Custom", "Video", "Audio"]
        for output in output_vector:
            cbOutput.append_text(output)

        cbOutput.set_entry_text_column(0)

        # ## END Label with icon and Combobox

        # ## ADDING TO LAYOUT
        hbox.pack_start(add_button, False, False, 0)
        hbox.pack_start(newLabel, False, False, 4)
        lbWithIcon.pack_start(Yimage, False, False, 0)
        lbWithIcon.pack_start(lbOutputType, False, False, 0)
        lbWithIcon.pack_start(cbOutput, False, False, 4)
        first_box.pack_start(hbox, False, False, 0)
        first_box.pack_start(lbWithIcon, True, True, 0)
        main_box.pack_start(first_box, False, True, 0)
        # ## END ADDING TO LAYOUT

        # ## EVENT FUNCTIONS FOR COMBOBOX AND BUTTON
        cbOutput.connect("changed", self.on_cbOuput_changed)
        add_button.connect("clicked", self.on_btnAdd_click)
        # ## END EVENT FUNCTIONS FOR COMBOBOX AND BUTTON
        # # END UPPER BOX


        # ## THE DOWN BOX CONSISTING OF A LISTBOX
        self.downBox = Gtk.ListBox()
        self.downBox.set_selection_mode(Gtk.SelectionMode.NONE)


        self.win_scroll = Gtk.ScrolledWindow()
        self.win_scroll.add(self.downBox)
        self.win_scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.win_scroll.set_min_content_height(100)
        main_box.pack_start(self.win_scroll, True, True, 0)
        # ## END ADDING TO LAYOUT
        # # END THE DOWN BOX CONSISTING OF A LISTBOX
        # END of ALL

    # ## METHODS

    def on_btnAdd_click(self, widget):
        # Adding new row to the list
        """
        Making a row
        Making a horizontal box downBox_main
        place pic in the horisontal box first,
        Make a vertical box and Put link in the box, make a horizontal box and place it in the vertical one with buttons
        Make a radiobuttons in a vertical box and Download button and place them in downBox_main
        """
        self.row = Gtk.ListBoxRow()
        self.row.set_border_width(5)

        downBox_main = Gtk.HBox()
        downBox_main.set_halign(Gtk.Align.CENTER)

        videoIcon = Gio.ThemedIcon(name="audio-x-generic")
        videoImage = Gtk.Image.new_from_gicon(videoIcon, Gtk.IconSize.DIALOG)

        vbox_link_and_butons = Gtk.VBox()
        vbox_link_and_butons.set_border_width(5)

        link_entry = Gtk.Entry()
        link_entry.set_placeholder_text("Paste the video link here")

        progress_bar = Gtk.ProgressBar()
        progress_bar.set_margin_bottom(2)
        progress_bar.set_margin_top(3)
        progress_bar.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("#58ACFA"))


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
        btnDownload.connect("clicked", lambda widget: self.on_btnDownload_click(link_entry, rbVideo, rbAudio))
        lst_rbVideo.append(rbVideo)
        lst_rbMusic.append(rbAudio)

        downBox_main.pack_start(videoImage, False, False, 0)
        vbox_link_and_butons.pack_start(link_entry, True, True, 0)
        vbox_link_and_butons.pack_start(progress_bar, True, True, 0)
        vbox_link_and_butons.pack_start(quality_hbox, True, True, 3)
        radiobtn_box.pack_start(rbVideo, False, True, 0)
        radiobtn_box.pack_start(rbAudio, False, True, 0)
        downBox_main.pack_start(vbox_link_and_butons, True, False, 8)
        downBox_main.pack_start(radiobtn_box, True, True, 0)
        downBox_main.pack_start(btnDownload, True, True, 3)
        self.row.add(downBox_main)
        self.downBox.add(self.row)
        self.downBox.show_all()


    def on_cbOuput_changed(self, combo):
        # is used when the combobox changes its member
        # Getting the index of the combox box
        index = combo.get_active_iter()
        if index is not None:
            model = combo.get_model()
            nrIndex = model[index][0]
            if nrIndex == 'Video':
                for rbVideos in lst_rbVideo:
                    Gtk.ToggleButton.set_active(rbVideos, True)

            elif nrIndex == 'Audio':
                for rbMusic in lst_rbMusic:
                    Gtk.ToggleButton.set_active(rbMusic, True)
            else:
                pass


    def on_btnDownload_click(self, link_entry, rbVideo, rbAudio):
        download_Url = link_entry.get_text()
        print(download_Url)
        link_entry.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("#F8F8F8"))
        link_entry.set_text(Downloader.YouTubeDLR.get_information(self, link_entry.get_text()))
        link_entry.set_editable(False)





    def on_btnSetting_clicked(self, button):
        # The form is ready
        from Settings import settingWindow
        win = settingWindow()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()


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
