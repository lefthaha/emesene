import gtk

import gui
import utils
import protocol.status as status
import extension

class StatusButton(gtk.Button):
    '''a button that when clicked displays a popup that allows the user to
    select a status'''
    NAME = 'Status Button'
    DESCRIPTION = 'A button to select the status'
    AUTHOR = 'Mariano Guerra'
    WEBSITE = 'www.emesene.org'

    def __init__(self, session=None):
        gtk.Button.__init__(self)
        self.session = session
        # a cache of gtk.Images to not load the images everytime we change
        # our status
        self.cache_imgs = {}

        self.set_status(status.ONLINE)
        self.set_relief(gtk.RELIEF_NONE)
        self.set_border_width(0)
        StatusMenu = extension.get_default('gtk menu status')
        self.menu = StatusMenu(self.set_status)
        self.menu.show_all()
        self.connect('clicked', self._on_clicked)

    def _on_clicked(self, button):
        '''callback called when the button is clicked'''
        self.menu.popup(None, None, None, 0, 0)

    def set_status(self, stat):
        '''load an image representing a status and store it on cache'''
        if stat not in status.ALL:
            return

        self.status = stat

        if stat not in self.cache_imgs:
            gtk_img = utils.safe_gtk_image_load(\
                gui.theme.status_icons[stat])
            self.cache_imgs[stat] = gtk_img
        else:
            gtk_img = self.cache_imgs[stat]

        self.set_image(gtk_img)

