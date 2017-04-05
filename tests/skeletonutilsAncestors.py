"""test skeletinutils.ancestors"""
import pymel.core as pmc
import skeletonutils

j1 = pmc.joint(name='J1')
j2 = pmc.joint(name='J2')
j3 = pmc.joint(name='J3')

print skeletonutils.ancestors(j1)

print skeletonutils.ancestors(j3)