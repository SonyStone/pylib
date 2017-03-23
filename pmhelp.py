"""This module does blah blah."""

import sys
import types
import webbrowser

import pymel.core as pmc

HELP_ROOT_URL = ('http://help.autodesk.com/cloudhelp/'
                 '2016/ENU/Maya-Tech-Docs/PyMel/')



def pmhelp(obj):
    """Gives help for a pymel or python object.

    If obj is not a PyMEL object, use Python's builtin
    'help' function.
    If obj is a string, open a web browser to a search in the
    PyMEL help for the string.
    Otherwise, open a web browser to the page for the object.
    """
    tail = pyto_helpstr(obj)
    if tail is None:
        help(obj)
    else:
        webbrowser.open(HELP_ROOT_URL + tail)


def pyto_helpstr(obj):
    """Creating a query string for a PyMEL object"""
    if isinstance(obj, basestring):
        return 'search.html?q=%s' % (obj.replace(' ', '+'))
    if not ispymel(obj):
        return None
    if isinstance(obj, types.ModuleType):
        return ('generated/%(module)s.html#module-%(module)s' %
                dict(module=obj.__name__))
    if isinstance(obj, types.MethodType):
        return ('generated/classes/%(module)s/'
                '%(module)s.%(typename)s.html'
                '#%(module)s.%(typename)s.%(methname)s' % dict(
                    module=obj.__module__,
                    typename=obj.im_class.__name__,
                    methname=obj.__name__))
    if isinstance(obj, types.FunctionType):
        return ('generated/functions/%(module)s/'
                '%(module)s.%(funcname)s.html'
                '#%(module)s.%(funcname)s' % dict(
                    module=obj.__module__,
                    funcname=obj.__name__))
    if not isinstance(obj, type):
        obj = type(obj)
    return ('generated/classes/%(module)s/'
            '%(module)s.%(typename)s.html'
            '#%(module)s.%(typename)s' % dict(
                module=obj.__module__,
                typename=obj.__name__))



def ispymel(obj):
    '''Adding support fpr non-PyMEL objects'''
    try:
        module = obj.__module__
    except AttributeError:
        try:
            module = obj.__name__
        except AttributeError:
            return None
    return module.startswith('pymel')

def testpyto_helpstr():
    """Test pyto_helpstr()"""
    def dotest(obj, ideal):
        """tests function"""
        result = pyto_helpstr(obj)
        assert result == ideal, '%s != %s' % (result, ideal)

    dotest('maya rocks', 'search.html?q=maya+rocks')
    dotest('maya rocks', 'search.html?q=maya+rocks')
    dotest(pmc.nodetypes,
           'generated/pymel.core.nodetypes.html'
           '#module-pymel.core.nodetypes')
    dotest(pmc.nodetypes.Joint,
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint.html'
           '#pymel.core.nodetypes.Joint')
    dotest(pmc.nodetypes.Joint(),
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint.html'
           '#pymel.core.nodetypes.Joint')
    dotest(pmc.nodetypes.Joint().getTranslation,
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint.html'
           '#pymel.core.nodetypes.Joint.getTranslation')
    dotest(pmc.joint,
           'generated/functions/pymel.core.animation/'
           'pymel.core.animation.joint.html'
           '#pymel.core.animation.joint')
    dotest(object(), None)
    dotest(10, None)
    dotest([], None)
    dotest(sys, None)