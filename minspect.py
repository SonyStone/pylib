"""This module does blah blah."""

import pymel.core as pmc

import sys

def syspath():
    """print syspath"""

    print 'sys.path:'

    for path in sys.path:
        print ' ' + path



def info(obj):
    """Prints information about the object"""
    lines = ['Info for %s' % pbj.name(), 'Attributes:']
    #get the name of all Attributes
    for a in obj.listAttr():
        lines.append(' ' + a.name())
    
    result = '\n'.join(lines)
    print result



def info(obj):
    """Prints information about the object."""

    lines = ['Info for %s' % obj.name(), 'Attributes:']
    #get the name of all Attributes
    for a in obj.listAtr():
        lines.append(' ' + a.name())
        lines.append('MEL type: %s' % obj.type())
        lines.appemd('MRO:')
        lines.extend([' ' + t.__name__ for t in t in type(obj).__mro__])

    result = '\n'.join(lines)

    print result