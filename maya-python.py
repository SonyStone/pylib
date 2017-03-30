Python for Maya

PYTHONPATH=$PYTHONPATH:~/mayapybook/pylib
# Maya Python

import maya.standalone
maya.standalone.initialize()
import pymel.core as pmc

xform, shape = pmc.polySphere()
type(xform)
# <class 'pymel.core.nodetypes.Transform'>

type(shape)
# <class 'pymel.core.nodetypes.PolySphere'>

dir(xform)


getattr(xform, 'getShape')
# <bound method Transform.getShape of nt.Transform(u'pSphere1')>
	
getattr(xform, 'translate')
# Attribute(u'pSphere1.translate')

import inspect
methods = []
for a in dir(xform):
    attr = getattr(xform, a)
    if inspect.ismethod(attr):
        methods.append(attr)

attrs = xform.listAttr()

methods
# [<bound method Transform.__add__ of nt.Transform(u'pSphere1')>,

# ProxyUnicode -> PyNode -> DependNode -> ContainerBase -> Entity -> DagNode -> Transform -> Joint

j = pmc.joint()
j.type()
u'joint'
type(j)
# <class 'pymel.core.nodetypes.Joint'>
type(j).__bases__
# (<class 'pymel.core.nodetypes.Transform'>,)
j.translate, j.rotate
# (Attribute(u'joint2.translate'), Attribute(u'joint2.rotate'))

type(j).__mro__
# (<class 'pymel.core.nodetypes.Joint'>,
#  <class 'pymel.core.nodetypes.Transform'>,
#  <class 'pymel.core.nodetypes.DagNode'>,
#  <class 'pymel.core.nodetypes.Entity'>,
#  <class 'pymel.core.nodetypes.ContainerBase'>,
#  <class 'pymel.core.nodetypes.DependNode'>,
#  <class 'pymel.core.general.PyNode'>,
#  <class 'pymel.util.utilitytypes.ProxyUnicode'>,
#  <type 'object'>)

objs = pmc.joint(), pmc.polySphere(), pmc.camera()
[o for o in pmc.ls() if minspect.is_exact_type(o, 'camera')]

[o for o in pmc.ls() if minspect.is_type(o, 'transform')]