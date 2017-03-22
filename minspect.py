"""This module does blah blah."""

import sys

import pymel.core as pmc

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
    return None

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
           '#pynel.core.nodetypes.Joint')
    dotest(pmc.nodetypes.Joint(),
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint'
           '#pymel.core.nodetypes.Joint.getTranslation')
    dotest(pmc.joint,
           'generated/functions/pymel.core.animation/'
           'pymel.core.animation.joint.html'
           '#pymel.core.animation.joint')

