# -------------------------------------------------------------------------------
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright 2019 Payam Maroufi
# -------------------------------------------------------------------------------
import sys
import Downloader
from gi.repository import Gtk, Gio, Gdk
import gi
gi.require_version('Gtk', '3.0')


# lists of rbbttons
lst_rbVideo = []
lst_rbMusic = []


class youtubeD(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Youtube Downloader", application=app)
        self.set_border_width(3)
        self.set_size_request(580, 500)
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
        self.add(main_box)

        """ Setting header. """
        __hb = Gtk.HeaderBar()
        __hb.set_show_close_button(True)
        __hb.props.title = "Youtube Downloader"
        __setting_btn = Gtk.Button()
        __setting_btn.add(Gtk.Image.new_from_gicon(Gio.ThemedIcon(
            name="applications-system"), Gtk.IconSize.BUTTON))
        __hb.pack_end(__setting_btn)
        self.set_titlebar(__hb)

        """ Adding download and output type box. """
        __hbox_setting = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        __hbox_setting.set_border_width(3)

        # Button in the setting bar
        __addDown_btn = Gtk.Button()
        __addDown_btn.add(Gtk.Image.new_from_gicon(
            Gio.ThemedIcon(name="list-add"), Gtk.IconSize.BUTTON))

        # Download label
        __addDown_lbl = Gtk.Label()
        __addDown_lbl.set_markup(
            "<span font='Ubuntu 9' font_weight='normal'> New download </span>")

        # Output type label
        __outputType_lbl = Gtk.Label()
        __outputType_lbl.set_markup(
            "<span font='Ubuntu 9' font_weight='normal'> Output type: </span>")

        # Output type combo box
        __output_cb = Gtk.ComboBoxText()
        output_vector = ["Custom", "Video", "Audio"]
        for output in output_vector:
            __output_cb.append_text(output)
        __output_cb.set_entry_text_column(0)

        # Add everything to the download and output box
        __hbox_setting.pack_start(__addDown_btn, False, False, 0)
        __hbox_setting.pack_start(__addDown_lbl, False, False, 4)
        __hbox_setting.pack_end(__output_cb, False, False, 4)
        __hbox_setting.pack_end(__outputType_lbl, False, False, 4)

        # Add the download and output box to the main box of the window
        main_box.pack_start(__hbox_setting, False, True, 0)

        """ Connecting each functional controller to its function """
        __setting_btn.connect("clicked", self.on_btnSetting_clicked)
        __output_cb.connect("changed", self.on_cbOuput_changed)
        __addDown_btn.connect("clicked", self.on_btnAdd_click)

        """ The download's section. """
        self.downBox = Gtk.ListBox()
        self.downBox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.win_scroll = Gtk.ScrolledWindow()
        self.win_scroll.add(self.downBox)
        self.win_scroll.set_policy(
            Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.win_scroll.set_min_content_height(100)

        main_box.pack_start(self.win_scroll, True, True, 0)

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
        self.row.set_border_width(3)

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
        progress_bar.modify_bg(Gtk.StateType.NORMAL,
                               Gdk.color_parse("#58ACFA"))

        self.quality_hbox = Gtk.HBox()

        radiobtn_box = Gtk.VBox()
        radiobtn_box.set_valign(Gtk.Align.CENTER)

        rbVideo = Gtk.RadioButton.new_with_label_from_widget(None, "Video")
        rbAudio = Gtk.RadioButton.new_from_widget(rbVideo)
        rbAudio.set_label("Audio")

        link_entry.connect("activate", lambda widget: self.entry_text_changed(
            link_entry, rbVideo, rbAudio))
        btnDownload = Gtk.Button()
        download_icon = Gio.ThemedIcon(name="down")
        image = Gtk.Image.new_from_gicon(download_icon, Gtk.IconSize.BUTTON)
        btnDownload.add(image)
        btnDownload.connect("clicked", lambda widget: self.on_btnDownload_click(
            link_entry, rbVideo, rbAudio))
        lst_rbVideo.append(rbVideo)
        lst_rbMusic.append(rbAudio)

        downBox_main.pack_start(videoImage, False, True, 0)
        vbox_link_and_butons.pack_start(link_entry, True, True, 0)
        vbox_link_and_butons.pack_start(progress_bar, True, True, 0)
        vbox_link_and_butons.pack_start(self.quality_hbox, True, True, 3)
        radiobtn_box.pack_start(rbVideo, False, True, 0)
        radiobtn_box.pack_start(rbAudio, False, True, 0)
        downBox_main.pack_start(vbox_link_and_butons, True, True, 8)
        downBox_main.pack_start(radiobtn_box, True, True, 0)
        downBox_main.pack_end(btnDownload, False, False, 3)
        self.row.add(downBox_main)
        self.downBox.add(self.row)
        self.downBox.show_all()
        self.selected_qualities = []
        self.selected_format = []
        self.y = False

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

    def entry_text_changed(self, link_entry, rbVideo, rbAudio):
        # ## The idea is that you get the text of the entry if there is any, and when there is
        # ## you use the help file Downloader.YoutubeDLR and ask for information.
        # ## From the class you will get an answer including the title of the video and
        # ## the info about fetching being succesfull. If the fetching is successful then
        # ## you set the title and so one. You make buttons for each quality based on how many
        # ## quality get_information returns.
        if link_entry.get_text() != "":
            self.download_Url = link_entry.get_text()

            print(self.download_Url)

            self.title_quality, self.y = Downloader.YouTubeDLR.get_information(
                self, self.download_Url)
            if self.y:
                if rbVideo.get_active():
                    link_entry.set_text(self.title_quality[2])
                    link_entry.set_editable(False)
                    print(self.title_quality[1])
                    self.available_format_code = self.title_quality[0]

                    # Creating toggle buttons for each quality
                    x = []
                    for buttonNames in self.title_quality[1]:
                        btn = Gtk.ToggleButton()
                        btn.set_label(buttonNames)
                        x.append(btn)
                        self.quality_hbox.pack_start(btn, True, True, 2)
                        btn.connect(
                            "toggled", lambda x: self.on_button_toggled(x))

                        self.quality_hbox.show_all()
                else:
                    link_entry.set_text(self.title_quality[2])
        else:
            link_entry.set_text("Something went wrong")

    def on_btnDownload_click(self, link_entry, rbVideo, rbAudio):
        # ## Without pressing enter no return value will be read. 'y' is set to false
        # ## at the beginning. If user press Enter key and the fetching is successful
        # ## the result will be used here. You can not do the fetch without pressing
        # ## Enter key.
        if self.y:
            if link_entry.get_text() != "" and rbVideo.get_active():
                if len(self.selected_qualities) != 0:
                    Downloader.YouTubeDLR.get_video(
                        self, self.download_Url, self.selected_format, self.selected_qualities)

            elif link_entry.get_text() != "" and rbAudio.get_active():
                print(self.download_Url)
                Downloader.YouTubeDLR.get_audio(self, self.download_Url)
        else:
            link_entry.set_text("SOMETHING WENT WRONG")

    def on_button_toggled(self, button):
        # Get the label of the toggle button to add to the select_qualities list.
        selected_Tbtn = button.get_label()
        if button.get_active():
            if selected_Tbtn not in self.selected_qualities:
                # Choosing the toggled options
                self.selected_qualities.append(selected_Tbtn)
                # Choosing the corresponding format code
                self.selected_format.append(
                    self.available_format_code[self.title_quality[1].index(selected_Tbtn)])
                print(self.selected_qualities)
                print(self.selected_format)
        else:
            self.selected_qualities.remove(selected_Tbtn)
            self.selected_format.remove(
                self.available_format_code[self.title_quality[1].index(selected_Tbtn)])
            print(self.selected_qualities)
            print(self.selected_format)
            print(len(self.selected_qualities))

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
