import maya.utils

def excepthook(tb_type, exc_object, tb, detail=2):
    s = maya.utils._formatGuiException(etype, evalue, tb, detail)
    lines = [
        s,
        'An unhandled exception occurred.',
        'Please copy the error info above this nessage',
        'and a copy of this file and email it to',
        'mayasupport@robg3d.com. You should get a response',
        'in three days or less.'
    ]
    return '\n'.join(lines)

maya.utils.formatGuiException = excepthook



