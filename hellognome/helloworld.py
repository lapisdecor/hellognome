import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def helloworld():
    window = Gtk.Window(title="Hello World")
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    helloworld()
