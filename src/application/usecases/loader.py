from kink import di
import importlib

def bootstrap_adapter() -> None:
    module_port = importlib.import_module('infrastructure.message.redis', package=None)
    #print("--->",dir(module_port))

    ihh = getattr(module_port,'messenger')

    di['messenger'] = lambda _di: ihh()

    module_port = importlib.import_module('infrastructure.message.logging', package=None)
    #print("--->",dir(module_port))

    ihh_log = getattr(module_port,'log')

    di['log'] = lambda _di: ihh_log()

    fs_module_port = importlib.import_module('infrastructure.persistence.ext4', package=None)
    #print("--->",dir(module_port))

    fs_ihh = getattr(fs_module_port,'filesystem')
    di['filesystem'] = lambda _di: fs_ihh()

    gui_module = importlib.import_module('infrastructure.presentation.flutter', package=None)
    #print("--->",dir(module_port))

    gui_port = getattr(gui_module,'presentation')
    di['presentation'] = lambda _di: gui_port()

    di['log'].speak(message="BOOTSTARP - LOADER")