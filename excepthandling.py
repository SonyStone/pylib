import os
import platform
import maya.utils
import sys
import pymel.core as pmc

def _normalize(p):
    return os.path.normpath(os.path.abspath(p))

LIB_DIR = _normalize(os.path.dirname(__file__))

__author__ = 'iliaverpa@gmail.com'

# def excepthook(tb_type, exc_object, tb, detail=2):
#     s = maya.utils._formatGuiException(etype, evalue, tb, detail)
#     lines = [
#         s,
#         'An unhandled exception occurred.',
#         'Please copy the error info above this nessage',
#         'and a copy of this file and email it to',
#         'mayasupport@robg3d.com. You should get a response',
#         'in three days or less.'
#     ]
#     return '\n'.join(lines)

def is_important_tb(tb):
    while tb:
        codepath = tb.tb_frame.f_code.co_filename
        if _normalize(codepath).startswith(LIB_DIR):
            return True
        tb = tb.tb_next
    return False

def is_important_tb_byauthor(tb):
    while tb:
        auth = tb.tb_frame.f_globals.get('__author__')
        if auth == __author__:
            return True
        tb = tb.tb_next
    return False

def excepthook(etype, evalue, tb, detail=2):
    result = origexcepthook(etype, evalue, tb, detail)
    if is_important_tb(tb):
        result = handleour_exc(etype, evalue, tb, detail)
    return result

def collectinfo():
    lines = []
    lines.append('Scene Info')
    lines.append(' Maya Scene: ' + pmc.sceneName())

    lines.append('Maya/Python Info')
    lines.append(' Maya Version: ' + pmc._about(version=True))
    lines.append(' Qt Version: ' + pmc._about(qtVersion=True))
    lines.append(' Maya64: ' + str(pmc._about(is64=True)))
    lines.append(' PyVersion: '+ sys.version)
    lines.append(' PyExe: ' + sys.executable)

    lines.append('Machine Info')
    lines.append(' OS: ' + pmc._about(os=True))
    lines.append(' Node: ' + platform.node())
    lines.append(' OSRelease: ' + platform.release())
    lines.append(' OSVersion: ' + platform.version())
    lines.append(' Machine: ' + platform.machine())
    lines.append(' Processor: ' + platform.processor())

    lines.append('Environment Info')
    lines.append(' EnvVars')
    for k in sorted(os.environ.keys()):
        lines.append(' %s: %s' %(k, os.environ[k]))
    lines.append(' SysPath')
    for p in sys.path:
        lines.append(' ' + p)
    return lines

def handleour_exc(etype, evalue, tb, detail):
    s = maya.utils._formatGuiException(etype, evalue, tb, detail)
    lines = [s]
    lines.extend(collectinfo())
    lines.extend([
        s,
        'An unhandled exception occurred.',
        'Please copy the error info above this message',
        'and a copy of this file and email it to',
        'mayasupport@robg3d.com. You should get a response',
        'in three days or less.'])
    return '\n'.join(lines)

maya.utils.formatGuiException = excepthook



