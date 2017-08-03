"""This module does blah blah."""

import sys
import types
import webbrowser

import pymel.core as pmc

HELP_2014_ROOT_URL = ('http://download.autodesk.com/global/docs/'
                      'maya2014/en_us/PyMel/')

HELP_2016_ROOT_URL = ('http://help.autodesk.com/cloudhelp/'
                      '2016/ENU/Maya-Tech-Docs/PyMel/')

# generated/functions/pymel.core.animation/pymel.core.animation.joint.html

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
        webbrowser.open(HELP_2016_ROOT_URL + tail)

def syspath():
    """print syspath"""

    print 'sys.path:'

    for path in sys.path:
        print ' ' + path


def info(obj):
    """Prints information about the object."""

    lines = ['Info for %s' % obj.name(), 'Attributes:']
    #get the name of all Attributes
    for atr in obj.listAtr():
        lines.append(' ' + atr.name())
        lines.append('MEL type: %s' % obj.type())
        lines.append('MRO:')
        lines.extend([' ' + t.__name__ for t in t in type(obj).__mro__])

    result = '\n'.join(lines)

    print result

# Functinon converts a python objcet to a PyMEL help query url.
    # If the object is a string,
        # return a query string for a help search.
    # If the object se a PyMEL object,
        # return the appropriate url tail.
        # PyMEL functions, modules, types, instances,
        # and methods are all valid.
    # Non-PyMEL objects return None.

# Function takes a python object and returns a full help url.
    # Calls the first function.
    # If first function returns None,
    # just use builtin 'help' funciton.
    # Otherwise, open a web browser to the help page.
    #

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

def testpyto_helpstr():
    def dotest(obj, ideal):
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

class MyClass (object):
    def mymethod(self):
        pass
    @classmethod
    def myclassmethod(cls):
        pass
    @staticmethod
    def mystaticmethod():
        pass

def spam():
    def eggs():
        pass
    pass


def is_exact_type(node, typename):
    """node.type() == typename"""
    return node.type() == typename

def is_type(node, typename):
    """Return True if node.type() is typename or 
    any subclass of typename."""
    return typename in node.nodeType(inherited=True)

