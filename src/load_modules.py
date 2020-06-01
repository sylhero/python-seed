import logging
from importlib.metadata import entry_points

logger = logging.getLogger(__name__)


def load_modules(app=None):
    for ep in entry_points()["src"]:
        logger.info("Loading module: %s", ep.name)
        mod = ep.load()
        if app:
            init_app = getattr(mod, "init_app", None)
            if init_app:
                init_app(app)