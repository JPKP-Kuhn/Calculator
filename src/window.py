from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/JPKPKuhn/PythonCalculator/window.ui')
class GtkMultiCalculatorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'GtkMultiCalculatorWindow'

    main_text_view = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
