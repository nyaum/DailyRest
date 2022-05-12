from distutils.log import error
import logging
import traceback as t
import common as c

def fail_log():
    log = logging.getLogger()
    log.addHandler(logging.FileHandler(filename='./bot/log/'+c.strftoday2+'.txt'))

    log.error('>> [DEBUG] ' + c.hours_minutes + t.format_exc())