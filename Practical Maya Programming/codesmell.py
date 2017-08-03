"""code smell"""
import os
import sys

import pymel.core as pmc

def say(string, use_stdout=True, stream=None):
    """code smell"""
    if stream is None:
        if use_stdout:
            stream = sys.stdout
        else:
            stream = sys.stderr
    stream.write(string + os.linesep)



def get_all_root_joints():
    roots = []
    for jnt in pmc.ls(type='joint'):
        if jnt.getParent() is None:
            roots.append(jnt)
    return roots


def is_root_joint(obj):
    return obj.type() == 'joint' and obj.getParent() is None

# all_roots = [obj for obj in pmc.ls() if is_root_joint(obj)]
new_roots = [obj for obj in pmc.importFile(some_file_path)
            if is_root_joint(obj)]

all_roots = [obj for obj in pmc.ls() if is_root_joint(obj)]
first_root = None
if all_roots:
    first_root = all_roots[0]


def first_or_default(sequence, default=None):
    for item in sequence:
        return item
    return default

first_root = first_or_default(obj for obj in pmc.ls() if is_root_joint(obj))

def first_or_default(sequence, predicate=None, default=None):
    for item in sequence:
        if predicate is None or predicate(item):
            return item
    return default

first_root = first_or_default(pmc.ls(), is_root_joint)

def head(sequence, count):
    result = []
    for item in sequence:
        if len(result) == count:
            break
        result.append(item)
    return result

head(pmc.ls(type='joiny'), 2)

def tail(sequence, count):
    result = list(sequence)
    return result[-count:]

tail(pmc.ls(type='joint'), 2)