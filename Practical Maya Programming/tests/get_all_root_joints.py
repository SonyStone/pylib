import pymel.core as pmc

def get_all_root_joints():
    roots = []
    for jnt in pmc.ls(type='joint'):
        if jnt.getParent() is None:
            roots.append(jnt)
    return roots