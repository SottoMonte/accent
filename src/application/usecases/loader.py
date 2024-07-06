from kink import di
import importlib

# pass le configurazioni qui

def loader(**constants):
    driver = importlib.import_module(constants['path'], package=None)
    provider = getattr(driver,constants['name'])
    di[constants['name']] = lambda _di: provider()

def bootstrap_adapter() -> None:
    loader(name='messenger',path='infrastructure.message.redis')
    loader(name='log',path='infrastructure.message.logging')
    loader(name='persistence',path='infrastructure.persistence.ext4')
    loader(name='presentation',path='infrastructure.presentation.flutter')
    loader(name='console',path='infrastructure.console.unix')

    loader(name='locator',path='application.orchestrator.locator')

    di['log'].speak(message="BOOTSTARP - LOADER")