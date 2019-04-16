import os
if os.environ.get('DEBUG'):
    import logging
    import pprint as pp
    log = logging.getLogger("bitwarden")
    log.propagate = True


class T:

    @staticmethod
    def debug2(msg, name=''):
        if name:
            msg = name + ': ' + msg
        if os.environ.get('DEBUG'):
            log.log(5, pp.pformat(msg))

    @staticmethod
    def debug(msg, name=''):
        if name:
            msg = name + ': ' + msg
        if os.environ.get('DEBUG'):
            log.debug(pp.pformat(msg))

    @staticmethod
    def info(msg, name=''):
        if name:
            msg = name + ': ' + msg
        if os.environ.get('DEBUG'):
            log.info(pp.pformat(msg))

    @staticmethod
    def error(msg):
        if os.environ.get('DEBUG'):
            log.error(msg)
