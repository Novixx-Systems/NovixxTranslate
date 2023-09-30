from pathlib import Path

from argostranslate import package, translate

import libretranslate.language


def boot(load_only=None, update_models=False):
    try:
        check_and_install_models(force=update_models, load_only_lang_codes=load_only)
    except Exception as e:
        print("Cannot update models (normal if you're offline): %s" % str(e))


def check_and_install_models(force=False, load_only_lang_codes=None):
    pass

