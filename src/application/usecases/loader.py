from kink import di
import importlib

# pass le configurazioni qui

def loader_manager(**constants):
    driver = importlib.import_module(constants['path'], package=None)
    provider = getattr(driver,constants['name'])
    di[constants['name']] = lambda _di: provider(services=[di['persistence'],])

def loader_driver(**constants):
    driver = importlib.import_module(constants['path'], package=None)
    provider = getattr(driver,constants['name'])
    di[constants['name']] = lambda _di: provider()

def bootstrap_adapter() -> None:
    loader_manager(name='locator',path='application.manager.locator')

    loader_driver(name='messenger',path='infrastructure.message.redis')
    loader_driver(name='log',path='infrastructure.message.logging')
    loader_driver(name='persistence',path='infrastructure.persistence.ext4')
    loader_driver(name='presentation',path='infrastructure.presentation.flutter')
    loader_driver(name='console',path='infrastructure.console.unix')

    di['log'].speak(message="BOOTSTARP - LOADER")