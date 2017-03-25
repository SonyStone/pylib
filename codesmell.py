"""code smell"""
import os
import sys

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

all_roots = [obj for obj in pmc.ls() if is_root_joint(obj)]
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

first_root = first_or_default(
    obj for obj
)