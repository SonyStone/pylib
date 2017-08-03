help(nt.Time)

class Time(DependNode)
 |  Method resolution order:
 |      Time
 |      DependNode
 |      pymel.core.general.PyNode
 |      pymel.util.utilitytypes.ProxyUnicode
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  addAttribute(self, attr)
 |      Add a new dynamic attibute to this node.
 |      
 |      :Parameters:
 |          attr : `PyNode`
 |              new attribute
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.addAttribute`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  attribute(self, index)
 |      Finds the attribute of this node at the given index. Index order is based on the order in which the attributes were added to the node.
 |      
 |      :Parameters:
 |          index : `int`
 |              the index of the attribute 
 |      
 |      
 |      :rtype: `PyNode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.attribute`
 |  
 |  attributeClass(self, attribute)
 |      Returns the class (normal, dynamic, extension) of the specified attribute.
 |      
 |      :Parameters:
 |          attribute : `PyNode`
 |              the attribute to check 
 |      
 |      
 |      :rtype: `DependNode.MAttrClass`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.attributeClass`
 |  
 |  dgCallbacks(self, timerType, callbackName, value)
 |      Node callbacks that occur when timing is enabled get logged with the node and can be queried via this method. See the dgCallbackIds method for getting a further breakdown of the time for an individual callback on this node.
 |      
 |      :Parameters:
 |          timerType : `DependNode.MdgTimerType`
 |              The timer we want to query, e.g. kTimerType_self for self time. 
 |      
 |              values: 'type_self', 'type_inclusive', 'type_count', 'types'
 |          callbackName : `list` list
 |              Returns an array of callback names that were invoked for this node since the last timer reset. 
 |          value : `float` list
 |              Returns an array of timing values. There is a one-to-one correspondence with the `callbackName' array.
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.dgCallbacks`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  dgTimer(self, timerMetric, timerType)
 |      The function returns the specified timer value for the current node. This is the total amount of time spent performing the requested operation since the timer was last reset (see  dgTimerReset()  for details). There are numerous timers per node and these are referenced by the metric and the timer type.
 |      
 |      :Parameters:
 |          timerMetric : `DependNode.MdgTimerMetric`
 |              The timing metric we wish to query. 
 |      
 |              values: 'metric_callback', 'metric_compute', 'metric_dirty', 'metric_draw', 'metric_fetch', 'metric_callbackViaAPI', 'metric_callbackNotViaAPI', 'metric_computeDuringCallback', 'metric_computeNotDuringCallback', 'metrics'
 |          timerType : `DependNode.MdgTimerType`
 |              The timer type we wish to query. 
 |      
 |              values: 'type_self', 'type_inclusive', 'type_count', 'types'
 |      
 |      
 |      :rtype: `float`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.dgTimer`
 |  
 |  dgTimerOff(self)
 |      Indicates that this node should no longer collect DG timing data when DG timing is enabled. See  dgTimerOn()  and  enableDGTiming()  for more details.
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.dgTimerOff`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  dgTimerOn(self)
 |      Indicates that this node should collect DG timing data whenever DG timing is enabled. See  enableDGTiming()  for more details.
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.dgTimerOn`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  dgTimerQueryState(self)
 |      The function returns the current on/off state of the node's timer.
 |      
 |      :rtype: `DependNode.MdgTimerState`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.dgTimerQueryState`
 |  
 |  dgTimerReset(self)
 |      The function resets the dependency graph timers and counters for this node to zero. Note that this method does not start or stop timing, it only resets the values to zero. If you want to turn on timing, use the method  dgTimerOn() . If you want to turn off timing, use  dgTimerOff() .
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.dgTimerReset`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  findAlias(self, alias)
 |      Retrieves the attribute with the given alias.
 |      
 |      :Parameters:
 |          alias : `unicode`
 |              alternative name of the attribute 
 |      
 |      
 |      :rtype: (`bool`, `PyNode`)
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.findAlias`
 |  
 |  findPlug(self, attr, wantNetworkedPlug)
 |      Attempt to find a plug for the given attribute. This method will first try to find the networked version of the plug if requested. The networked version of a plug is one that currently exists in the dependency graph at a particular connection point. If a networked version is not found, then a standard non-networked plug is returned.
 |      
 |      :Parameters:
 |          attr : `PyNode`
 |              attribute whose plug we wish to find 
 |          wantNetworkedPlug : `bool`
 |              if true, request a networked plug if it is available 
 |      
 |      
 |      :rtype: `PyNode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.findPlug`
 |  
 |  getAffectedAttributes(self, attr)
 |      Returns an array of attributes that are affected by the attribute passed in. That is, when the given attribute,  attr  is marked dirty (changed) all the  affectedAttributes  attributes will also be marked dirty. For nodes defined in plug-ins this call returns all those attributes that were marked as being affected by the given one via the  MPxNode::attributeAffects  call.
 |      
 |      :Parameters:
 |          attr : `PyNode`
 |              the attribute to check 
 |      
 |      
 |      :rtype: `PyNode` list
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.getAffectedAttributes`
 |  
 |  getAffectedByAttributes(self, attr)
 |      Returns an array of attributes that affect the attribute passed in,  attr . That is, when one of the attributes in  affectedByAttributes  is marked dirty (changed) then  attr  will also be marked dirty. For nodes defined in plug-ins this call returns all those attributes that were marked as affecting the given one via the  MPxNode::attributeAffects  call.
 |      
 |      :Parameters:
 |          attr : `PyNode`
 |              the attribute to check 
 |      
 |      
 |      :rtype: `PyNode` list
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.getAffectedByAttributes`
 |  
 |  getAliasAttr(self, force)
 |      Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases.
 |      
 |      :Parameters:
 |          force : `bool`
 |              To indicate whether the alias attr should be created. 
 |      
 |      
 |      :rtype: `PyNode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.getAliasAttr`
 |  
 |  getAliasList(self)
 |      Returns a list of all attribute aliases for this node. The aliases are pairs of strings with the first being the alias and the second being the attribute's real name.
 |      
 |      :rtype: (`bool`, `list` list)
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.getAliasList`
 |  
 |  getConnections(self)
 |      Get all of the current connections to this node as an array of plugs.
 |      
 |      :rtype: `PyNode` list
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.getConnections`
 |  
 |  getName(self)
 |      Returns the name of this node. Note that if the object the instance of this class is attached to is  data  instead of being in the graph (ie. the object was created by one of the MFn*Data function sets, or was passed to an  MPxNode::compute  function in a data block) then the  name  method will not work.
 |      
 |      :rtype: `unicode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.name`
 |  
 |  hasAttribute(self, attrName)
 |      Returns true if the node already has an attribute with the given name.
 |      
 |      :Parameters:
 |          attrName : `unicode`
 |              Name of attribute to be checked. 
 |      
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.hasAttribute`
 |  
 |  hasUniqueName(self)
 |      Indicates whether or not this node's name is unique within the scene.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.hasUniqueName`
 |  
 |  isFromReferencedFile(self)
 |      Indicates whether or not this node came from a referenced file. If it did, the node will be marked as read-only in the scene and changes to the node's attributes will be saved in the main scene file, not the referenced file from which the node came.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.isFromReferencedFile`
 |  
 |  isNewAttribute(self, attr)
 |      Indicates whether or not the specified attribute was added to this node within the current scene.
 |      
 |      :Parameters:
 |          attr : `PyNode`
 |              Attribute to check. 
 |      
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.isNewAttribute`
 |  
 |  plugsAlias(self, plug)
 |      Returns the alias for the plug's attribute or the empty string if that attribute has no alias.
 |      
 |      :Parameters:
 |          plug : `PyNode`
 |              plug for whose attribute we want the alias 
 |      
 |      
 |      :rtype: `unicode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.plugsAlias`
 |  
 |  removeAttribute(self, attribute)
 |      Remove a dynamic attribute from a node.
 |      
 |      :Parameters:
 |          attribute : `PyNode`
 |              attribute to remove
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.removeAttribute`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  reorderedAttribute(self, index)
 |      Some nodes, such as the various animCurve nodes, require that their attributes be set in a specific order for proper operation. Usually this ordering is only important when the node is being created during file I/O.
 |      
 |      :Parameters:
 |          index : `int`
 |              the reordered index of the attribute 
 |      
 |      
 |      :rtype: `PyNode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.reorderedAttribute`
 |  
 |  setAlias(self, alias, name, plug, add=True)
 |      Sets or removes an alias (i.e. an alternative name) for an attribute.
 |      
 |      :Parameters:
 |          alias : `unicode`
 |              alternative name for the attribute 
 |          name : `unicode`
 |              real name of the attribute 
 |          plug : `PyNode`
 |              plug to the attribute 
 |          add : `bool`
 |              true to add the alias, false to remove it 
 |      
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.setAlias`
 |  
 |  setFlag(self, flag, state)
 |      Sets the  state  of the specified  flag  for the node.
 |      
 |      :Parameters:
 |          flag : `int`
 |              flag to set 
 |          state : `bool`
 |              new state to which the flag will be set
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.setFlag`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  setName(self, name, createNamespace=False)
 |      Sets the name of this node.
 |      
 |      :Parameters:
 |          name : `unicode`
 |              the new name for the node 
 |          createNamespace : `bool`
 |              determine whether or not to create a new namespace when the given name includes a namespace which does not exist. 
 |      
 |      
 |      :rtype: `unicode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.setName`
 |  
 |  typeName(self)
 |      Returns the type name of this node. The string returned is the name of the node type as it is used in the ascii file format.
 |      
 |      :rtype: `unicode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.typeName`
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  allocateFlag(self, pluginName) from pymel.internal.factories.MetaMayaNodeWrapper
 |      Allocates a node flag for sole use by the caller. Note that the flag is not specific to any one node but is made available to the caller on all nodes. Furthermore, node flags only persist for the duration of the current Maya session: they are not saved with the scene.
 |      
 |      :Parameters:
 |          pluginName : `unicode`
 |              The name of the plugin which is allocating the flag. A plugin's name can be retrieved by calling MFnPlugin::name() within its initializePlugin() or uninitializePlugin() functions.
 |      
 |      
 |      :rtype: `int`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.allocateFlag`
 |  
 |  deallocateAllFlags(self, pluginName) from pymel.internal.factories.MetaMayaNodeWrapper
 |      Deallocates all of the node flags which are currently allocated to the specified plugin. The deallocated flags immediately become available for use by any plugin.
 |      
 |      :Parameters:
 |          pluginName : `unicode`
 |              The name of the plugin whose flags are to be deallocated. A plugin's name can be retrieved by calling MFnPlugin::name() within its initializePlugin() or uninitializePlugin() functions.
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.deallocateAllFlags`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  deallocateFlag(self, pluginName, flag) from pymel.internal.factories.MetaMayaNodeWrapper
 |      Deallocates a node  flag  which was previously allocated by a call to  allocateFlag . The flag subsequently becomes available for reallocation and use by someone else.
 |      
 |      :Parameters:
 |          pluginName : `unicode`
 |              The name of the plugin which allocated the flag. A plugin's name can be retrieved by calling MFnPlugin::name() within its initializePlugin() or uninitializePlugin() functions.
 |          flag : `int`
 |              Flag to deallocate.
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.deallocateFlag`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  MAttrClass = Enum(
 |  EnumValue('MAttrClass', 1, 'localDynamicAt...ttr'),...
 |  
 |  MdgTimerMetric = Enum(
 |  EnumValue('MdgTimerMetric', 0, 'metric_cal...ac...
 |  
 |  MdgTimerState = Enum(
 |  EnumValue('MdgTimerState', 0, 'off'),
 |  Enum...),
 |  ...
 |  
 |  MdgTimerType = Enum(
 |  EnumValue('MdgTimerType', 0, 'type_self'),...e_co...
 |  
 |  __apicls__ = <class 'maya.OpenMaya.MFnDependencyNode'>
 |  
 |  
 |  __melnode__ = u'time'
 |  
 |  __readonly__ = {'__readonly__': None}
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from DependNode:
 |  
 |  __apihandle__(self)
 |  
 |  __apimobject__(self)
 |      get the MObject for this node if it is valid
 |  
 |  __apiobject__(self)
 |      get the default API object (MObject) for this node if it is valid
 |  
 |  __getattr__(self, attr)
 |  
 |  __hash__(self)
 |  
 |  __melobject__ = newfunc(*args, **kwargs)
 |      Special method for returning a mel-friendly representation.
 |  
 |  __repr__(self)
 |      :rtype: `unicode`
 |  
 |  __str__(self)
 |  
 |  __unicode__(self)
 |  
 |  addAttr(self, attr, **kwargs)
 |      This command is used to add a dynamic attribute to a node or nodes. Either the longName or the shortName or both must be
 |      specified. If neither a dataType nor an attributeType is specified, a double attribute will be added.  The dataType flag
 |      can be specified more than once indicating that any of the supplied types will be accepted (logical-or).  To add a non-
 |      double attribute the following criteria can be used to determine whether the dataType or the attributeType flag is
 |      appropriate.  Some types, such as double3can use either. In these cases the -dtflag should be used when you only wish to
 |      access the data as an atomic entity (eg. you never want to access the three individual values that make up a double3).
 |      In general it is best to use the -atin these cases for maximum flexibility. In most cases the -dtversion will not
 |      display in the attribute editor as it is an atomic type and you are not allowed to change individual parts of it.  All
 |      attributes flagged as (compound)below or the compound attribute itself are not actually added to the node until all of
 |      the children are defined (using the -pflag to set their parent to the compound being created).  See the EXAMPLES section
 |      for more details.  Type of attribute              Flag and argument to use      boolean
 |      -at bool                      32 bit integer                                 -at long                      16 bit
 |      integer                                 -at short                     8 bit integer                                  -at
 |      byte                      char                                                   -at char                      enum
 |      -at enum (specify the enum names using the enumName flag) float                                                  -at
 |      float(use quotes                                                                         since float is a mel keyword)
 |      double                                                 -at double            angle value
 |      -at doubleAngle       linear value                                   -at doubleLinear      string
 |      -dt string(use quotes                                                                         since string is a mel
 |      keyword)  array of strings                               -dt stringArray       compound
 |      -at compound          message (no data)                              -at message           time
 |      -at time                      4x4 double matrix                              -dt matrix(use quotes
 |      since matrix is a mel keyword)  4x4 float matrix                               -at fltMatrix         reflectance
 |      -dt reflectanceRGBreflectance (compound)                 -at reflectance       spectrum
 |      -dt spectrumRGB       spectrum (compound)                    -at spectrum          2 floats
 |      -dt float2            2 floats (compound)                    -at float2            3 floats
 |      -dt float3            3 floats (compound)                    -at float3            2 doubles
 |      -dt double2           2 doubles (compound)                   -at double2           3 doubles
 |      -dt double3           3 doubles (compound)                   -at double3           2 32-bit integers
 |      -dt long2                     2 32-bit integers (compound)   -at long2                     3 32-bit integers
 |      -dt long3                     3 32-bit integers (compound)   -at long3                     2 16-bit integers
 |      -dt short2            2 16-bit integers (compound)   -at short2            3 16-bit integers
 |      -dt short3            3 16-bit integers (compound)   -at short3            array of doubles
 |      -dt doubleArray       array of floats                                -dt floatArray        array of 32-bit ints
 |      -dt Int32Array        array of vectors                               -dt vectorArray       nurbs curve
 |      -dt nurbsCurve        nurbs surface                                  -dt nurbsSurface      polygonal mesh
 |      -dt mesh                      lattice                                                -dt lattice           array of
 |      double 4D points              -dt pointArray        In query mode, return type is based on queried flag.
 |      
 |      Flags:
 |        - attributeType : at             (unicode)       [create,query]
 |            Specifies the attribute type, see above table for more details. Note that the attribute types float, matrixand stringare
 |            also MEL keywords and must be enclosed in quotes.
 |      
 |        - binaryTag : bt                 (unicode)       [create,query]
 |            This flag is obsolete and does not do anything any more
 |      
 |        - cachedInternally : ci          (bool)          [create,query]
 |            Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and
 |            false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be
 |            uncached as this will make it impossible to set keyframes.
 |      
 |        - category : ct                  (unicode)       [create,query,edit]
 |            An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created
 |            the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
 |            categories can not be removed once associated.
 |      
 |        - dataType : dt                  (unicode)       [create,query]
 |            Specifies the data type.  See setAttrfor more information on data type names.
 |      
 |        - defaultValue : dv              (float)         [create,query,edit]
 |            Specifies the default value for the attribute (can only be used for numeric attributes).
 |      
 |        - disconnectBehaviour : dcb      (int)           [create,query]
 |            defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
 |      
 |        - enumName : en                  (unicode)       [create,query,edit]
 |            Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-
 |            separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
 |            starting with 0. For example: -enumName A:B:Cwould produce options: A,B,C with values of 0,1,2; -enumName
 |            zero:one:two:thousand=1000would produce four options with values 0,1,2,1000; and -enumName
 |            solo=1:triplet=3:quintet=5would produce three options with values 1,3,5.  (Note that there is a current limitation of
 |            the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can
 |            appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential
 |            values for the options of any enumerated attributes that will appear in the Channel Box.  For example:
 |            solo=1:triplet=2:quintet=3.)
 |      
 |        - exists : ex                    (bool)          [create,query]
 |            Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
 |            Flag can have multiple arguments, passed either as a tuple or a list.
 |      
 |        - fromPlugin : fp                (bool)          [create,query]
 |            Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here
 |            to support storing it in a file independently from the creating plugin.
 |      
 |        - hasMaxValue : hxv              (bool)          [create,query,edit]
 |            Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
 |      
 |        - hasMinValue : hnv              (bool)          [create,query,edit]
 |            Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
 |      
 |        - hasSoftMaxValue : hsx          (bool)          [create,query]
 |            Flag indicating whether a numeric attribute has a soft maximum.
 |      
 |        - hasSoftMinValue : hsn          (bool)          [create,query]
 |            Flag indicating whether a numeric attribute has a soft minimum.
 |      
 |        - hidden : h                     (bool)          [create,query]
 |            Will this attribute be hidden from the UI?
 |      
 |        - indexMatters : im              (bool)          [create,query]
 |            Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the
 |            attribute to non-readable.
 |      
 |        - internalSet : internalSet      (bool)          [create,query]
 |            Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for
 |            updating UI elements.
 |      
 |        - keyable : k                    (bool)          [create,query]
 |            Is the attribute keyable by default?
 |      
 |        - longName : ln                  (unicode)       [create,query]
 |            Sets the long name of the attribute.
 |      
 |        - maxValue : max                 (float)         [create,query,edit]
 |            Specifies the maximum value for the attribute (can only be used for numeric attributes).
 |      
 |        - minValue : min                 (float)         [create,query,edit]
 |            Specifies the minimum value for the attribute (can only be used for numeric attributes).
 |      
 |        - multi : m                      (bool)          [create,query]
 |            Makes the new attribute a multi-attribute.
 |      
 |        - niceName : nn                  (unicode)       [create,query,edit]
 |            Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string
 |            overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
 |            attributeNiceNameand attributeQuery -niceNameto lookup an attribute's nice name in the catalog.)
 |      
 |        - numberOfChildren : nc          (int)           [create,query]
 |            How many children will the new attribute have?
 |      
 |        - parent : p                     (unicode)       [create,query]
 |            Attribute that is to be the new attribute's parent.
 |      
 |        - readable : r                   (bool)          [create,query]
 |            Can outgoing connections be made from this attribute?
 |      
 |        - shortName : sn                 (unicode)       [create,query]
 |            Sets the short name of the attribute.
 |      
 |        - softMaxValue : smx             (float)         [create,query,edit]
 |            Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
 |      
 |        - softMinValue : smn             (float)         [create,query,edit]
 |            Soft minimum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
 |      
 |        - storable : s                   (bool)          [create,query]
 |            Can the attribute be stored out to a file?
 |      
 |        - usedAsColor : uac              (bool)          [create,query]
 |            Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The
 |            attribute type -atshould be double3or float3as appropriate.  It can also be used to less effect with data types -dtas
 |            double3or float3as well but some parts of the code do not support this alternative.  The special attribute types/data
 |            spectrumand reflectancealso support the color flag and on them it is set by default.
 |      
 |        - usedAsFilename : uaf           (bool)          [create,query]
 |            Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type -dtof
 |            string.
 |      
 |        - writable : w                   (bool)          [create,query]
 |            Can incoming connections be made to this attribute?
 |      
 |      
 |      Derived from mel command `maya.cmds.addAttr`
 |  
 |  attr(self, attr)
 |      access to attribute plug of a node. returns an instance of the Attribute class for the
 |      given attribute name.
 |      
 |      :rtype: `Attribute`
 |  
 |  attrDefaults = newfunc(*args, **kwargs)
 |      Access to an attribute of a node.  This does not require an instance:
 |      
 |          >>> nt.Transform.attrDefaults('tx').isKeyable()
 |          True
 |      
 |      but it can use one if needed ( for example, for dynamically created attributes )
 |      
 |          >>> nt.Transform(u'persp').attrDefaults('tx').isKeyable()
 |      
 |      Note: this is still experimental.
 |  
 |  attrInfo(self, **kwargs)
 |      attributeInfo
 |      
 |      :rtype: `Attribute` list
 |  
 |  attributeCount(self)
 |      Returns the number of attributes that this node has.
 |      
 |      :rtype: `int`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.attributeCount`
 |  
 |  canBeWritten(self)
 |      Returns the do not write state of the node. Will be true if the node can be written/exported to scene files.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.canBeWritten`
 |  
 |  cast(self, swapNode, **kwargs)
 |      nodeCast
 |  
 |  classification(self)
 |      getClassification
 |  
 |  connectAttr(self, attr, destination, **kwargs)
 |      Connect the attributes of two dependency nodes and return the names of the two connected attributes. The connected
 |      attributes must be be of compatible types. First argument is the source attribute, second one is the destination. Refer
 |      to dependency node documentation.
 |      
 |      Flags:
 |        - force : f                      (bool)          [create]
 |            Forces the connection.  If the destination is already connected, the old connection is broken and the new one made.
 |      
 |        - lock : l                       (bool)          [create]
 |            If the argument is true, the destination attribute is locked after making the connection. If the argument is false, the
 |            connection is unlocked before making the connection.
 |      
 |        - nextAvailable : na             (bool)          [create]
 |            If the destination multi-attribute has set the indexMatters to be false with this flag specified, a connection is made
 |            to the next available index. No index need be specified.
 |      
 |        - referenceDest : rd             (unicode)       [create]
 |            This flag is used for file io only. The flag indicates that the connection replaces a connection made in a referenced
 |            file, and the flag argument indicates the original destination from the referenced file. This flag is used so that if
 |            the reference file is modified, maya can still attempt to make the appropriate connections in the main scene to the
 |            referenced object.                        Flag can have multiple arguments, passed either as a tuple or a list.
 |      
 |      
 |      Derived from mel command `maya.cmds.connectAttr`
 |  
 |  deleteAttr(self, attr, *args, **kwargs)
 |      This command is used to delete a dynamic attribute from a node or nodes. The attribute can be specified by using either
 |      the long or short name. Only one dynamic attribute can be deleted at a time. Static attributes cannot be deleted.
 |      Children of a compound attribute cannot be deleted. You must delete the complete compound attribute. This command has no
 |      edit capabilities. The only query ability is to list all the dynamic attributes of a node. In query mode, return type is
 |      based on queried flag.
 |      
 |      Flags:
 |        - attribute : at                 (unicode)       [create]
 |            Specify either the long or short name of the attribute.                   Flag can have multiple arguments, passed
 |            either as a tuple or a list.
 |      
 |        - name : n                       (unicode)       [create]
 |            The name of the node.
 |      
 |      
 |      Derived from mel command `maya.cmds.deleteAttr`
 |  
 |  deletePreset(self, presetName)
 |  
 |  destinations(self, **kwargs)
 |      listConnections -source 0 -destination 1
 |      
 |      :rtype: `PyNode` list
 |  
 |  disconnectAttr(self, attr, destination=None, **kwargs)
 |      Disconnects two connected attributes. First argument is the source attribute, second is the destination.
 |      
 |      Flags:
 |        - nextAvailable : na             (bool)          [create]
 |            If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching
 |            connection.  No index needs to be specified.                      Flag can have multiple arguments, passed either as a
 |            tuple or a list.
 |      
 |      
 |      Derived from mel command `maya.cmds.disconnectAttr`
 |  
 |  duplicate(*args, **kwargs)
 |      This command duplicates the given objects. If no objects are given, then the selected list is duplicated. The smart
 |      transform feature allows duplicate to transform newly duplicated objects based on previous transformations between
 |      duplications. Example: Duplicate an object and move it to a new location. Duplicate it again with the smart duplicate
 |      flag. It should have moved once again the distance you had previously moved it. Note: changing the selected list between
 |      smart duplications will cause the transform information to be deleted The upstream Nodes option forces duplication of
 |      all upstream nodes leading upto the selected objects.. Upstream nodes are defined as all nodes feeding into selected
 |      nodes. During traversal of Dependency graph, if another dagObject is encountered, then that node and all it's parent
 |      transforms are also duplicated. The inputConnections option forces the duplication of input connections to the nodes
 |      that are to be duplicated. This is very useful especially in cases where two nodes that are connected to each other are
 |      specified as nodes to be duplicated. In that situation, the connection between the nodes is also duplicated. See
 |      also:instance
 |      
 |      Modifications:
 |        - new option: addShape
 |              If addShape evaluates to True, then all arguments fed in must be shapes, and each will be duplicated and added under
 |              the existing parent transform, instead of duplicating the parent transform.
 |              The following arguments are incompatible with addShape, and will raise a ValueError if enabled along with addShape:
 |                  renameChildren (rc), instanceLeaf (ilf), parentOnly (po), smartTransform (st)
 |        - returns wrapped classes
 |        - returnRootsOnly is forced on for dag objects. This is because the duplicate command does not use full paths when returning
 |          the names of duplicated objects and will fail if the name is not unique.
 |      
 |      Flags:
 |        - inputConnections : ic          (bool)          [create]
 |            Input connections to the node to be duplicated, are also duplicated. This would result in a fan-out scenario as the
 |            nodes at the input side are not duplicated (unlike the -un option).
 |      
 |        - instanceLeaf : ilf             (bool)          [create]
 |            instead of duplicating leaf DAG nodes, instance them.
 |      
 |        - name : n                       (unicode)       [create]
 |            name to give duplicated object(s)
 |      
 |        - parentOnly : po                (bool)          [create]
 |            Duplicate only the specified DAG node and not any of its children.                        Flag can have multiple
 |            arguments, passed either as a tuple or a list.
 |      
 |        - renameChildren : rc            (bool)          [create]
 |            rename the child nodes of the hierarchy, to make them unique.
 |      
 |        - returnRootsOnly : rr           (bool)          [create]
 |            return only the root nodes of the new hierarchy. When used with upstreamNodes flag, the upstream nodes will be omitted
 |            in the result.  This flag controls only what is returned in the output string[], and it does NOT change the behaviour of
 |            the duplicate command.
 |      
 |        - smartTransform : st            (bool)          [create]
 |            remembers last transformation and applies it to duplicated object(s)
 |      
 |        - upstreamNodes : un             (bool)          [create]
 |            the upstream nodes leading upto the selected nodes (along with their connections) are also duplicated.
 |      
 |      
 |      Derived from mel command `maya.cmds.duplicate`
 |  
 |  extractNum(self)
 |      Return the trailing numbers of the node name. If no trailing numbers are found
 |      an error will be raised.
 |      
 |      >>> from pymel.core import *
 |      >>> SCENE.lambert1.extractNum()
 |      u'1'
 |      
 |      :rtype: `unicode`
 |  
 |  getAttr(self, attr, *args, **kwargs)
 |      This command returns the value of the named object's attribute. UI units are used where applicable. Currently, the types
 |      of attributes that can be displayed are: numeric attributesstring attributesmatrix attributesnumeric compound attributes
 |      (whose children are all numeric)vector array attributesdouble array attributesint32 array attributespoint array
 |      attributesdata component list attributesOther data types cannot be retrieved. No result is returned if the attribute
 |      contains no data.
 |      
 |      Flags:
 |        - asString : asString            (bool)          [create]
 |            This flag is only valid for enum attributes. It allows you to get the attribute values as strings instead of integer
 |            values. Note that the returned string value is dependent on the UI language Maya is running in (about -uiLanguage).
 |      
 |        - caching : ca                   (bool)          [create]
 |            Returns whether the attribute is set to be cached internally
 |      
 |        - channelBox : cb                (bool)          [create]
 |            Returns whether the attribute is set to show in the channelBox. Keyable attributes also show in the channel box.
 |      
 |        - expandEnvironmentVariables : x (bool)          [create]
 |            Expand any environment variable and (tilde characters on UNIX) found in string attributes which are returned.
 |      
 |        - keyable : k                    (bool)          [create]
 |            Returns the keyable state of the attribute.
 |      
 |        - lock : l                       (bool)          [create]
 |            Returns the lock state of the attribute.
 |      
 |        - multiIndices : mi              (bool)          [create]
 |            If the attribute is a multi, this will return a list containing all of the valid indices for the attribute.
 |            Flag can have multiple arguments, passed either as a tuple or a list.
 |      
 |        - settable : se                  (bool)          [create]
 |            Returns 1 if this attribute is currently settable by setAttr, 0 otherwise. An attribute is settable if it's not locked
 |            and either not connected, or has only keyframed animation.
 |      
 |        - silent : sl                    (bool)          [create]
 |            When evaluating an attribute that is not a numeric or string value, suppress the error message saying that the data
 |            cannot be displayed. The attribute will be evaluated even though its data cannot be displayed. This flag does not
 |            suppress all error messages, only those that are benign.
 |      
 |        - size : s                       (bool)          [create]
 |            Returns the size of a multi-attribute array.  Returns 1 if non-multi.
 |      
 |        - time : t                       (time)          [create]
 |            Evaluate the attribute at the given time instead of the current time.
 |      
 |        - type : typ                     (bool)          [create]
 |            Returns the type of data currently in the attribute. Attributes of simple types such as strings and numerics always
 |            contain data, but attributes of complex types (arrays, meshes, etc) may contain no data if none has ever been assigned
 |            to them. When this happens the command will return with no result: not an empty string, but no result at all. Attempting
 |            to directly compare this non-result to another value or use it in an expression will result in an error, but you can
 |            assign it to a variable in which case the variable will be set to the default value for its type (e.g. an empty string
 |            for a string variable, zero for an integer variable, an empty array for an array variable). So to be safe when using
 |            this flag, always assign its result to a string variable, never try to use it directly.
 |      
 |      
 |      Derived from mel command `maya.cmds.getAttr`
 |  
 |  getIcon(self)
 |      Returns the custom icon filename associated with the node. The icon can be assigned using  setIcon() .
 |      
 |      :rtype: `unicode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.icon`
 |  
 |  hasAttr(pyObj, attr, checkShape=True)
 |      convenience function for determining if an object has an attribute.
 |      If checkShape is enabled, the shape node of a transform will also be checked for the attribute.
 |      
 |      :rtype: `bool`
 |  
 |  inputs(self, **kwargs)
 |      listConnections -source 1 -destination 0
 |      
 |      :rtype: `PyNode` list
 |  
 |  isDefaultNode(self)
 |      Returns true if the node is a default node.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.isDefaultNode`
 |  
 |  isFlagSet(self, flag)
 |      Retrieves the current state of the specified  flag  for a node.
 |      
 |      :Parameters:
 |          flag : `int`
 |              number of the flag to retrieve. 
 |      
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.isFlagSet`
 |  
 |  isLocked(self)
 |      Indicates whether or not this node is locked. See the  setLocked  method for more information on what it means for a node to be locked.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.isLocked`
 |  
 |  isReadOnly(self)
 |      Indicates whether or not this node came from a referenced file. If it did, the node will be marked as read-only in the scene and changes to the node's attributes will be saved in the main scene file, not the referenced file from which the node came.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.isFromReferencedFile`
 |  
 |  isReferenced(self)
 |      Indicates whether or not this node came from a referenced file. If it did, the node will be marked as read-only in the scene and changes to the node's attributes will be saved in the main scene file, not the referenced file from which the node came.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.isFromReferencedFile`
 |  
 |  isShared(self)
 |      Indicates whether or not this node is shared. This comes into play when you attempt to create a new node with the same name as an existing node. If the existing node is shared, then no new node will be created. If the existing node is not shared, then the new node will be created and given a different name.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.isShared`
 |  
 |  isTrackingEdits(self)
 |      Returns whether or not edits on the given node are being tracked by the generalized edit system.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.isTrackingEdits`
 |  
 |  isUniquelyNamed(self)
 |      Indicates whether or not this node's name is unique within the scene.
 |      
 |      :rtype: `bool`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.hasUniqueName`
 |  
 |  listAliases(self)
 |      aliasAttr
 |      
 |      Modifications:
 |        - returns an empty list when the result is None
 |        - when queried, returns a list of (alias, `Attribute`) pairs.
 |      
 |      :rtype: (`str`, `Attribute`) list
 |  
 |  listAnimatable(*args, **kwargs)
 |      This command list the animatable attributes of a node.  Command flags allow filtering by the current manipulator, or
 |      node type.
 |      
 |      Modifications:
 |          - returns an empty list when the result is None
 |          - returns wrapped classes
 |      
 |      Flags:
 |        - active : act                   (bool)          [create]
 |            This flag is obsolete and no longer supported.
 |      
 |        - manip : m                      (bool)          [create]
 |            Return only those attributes affected by the current manip. If there is no manip active and any other flags are
 |            specified, output is the same as if the -manipflag were not present.
 |      
 |        - manipHandle : mh               (bool)          [create]
 |            Return only those attributes affected by the current manip handle. If there is no manip handle active and any other
 |            flags are specified, output is the same as if the -manipHandleflag were not present.
 |      
 |        - shape : s                      (bool)          [create]
 |            This flag is obsolete and no longer supported.                    Flag can have multiple arguments, passed either as a
 |            tuple or a list.
 |      
 |        - type : typ                     (bool)          [create]
 |            Instead of returning attributes, Return the types of nodes that are currently animatable.
 |      
 |      
 |      Derived from mel command `maya.cmds.listAnimatable`
 |  
 |  listAttr(self, **kwargs)
 |      listAttr
 |      
 |      Modifications:
 |        - returns an empty list when the result is None
 |        - added 'alias' keyword to list attributes that have aliases
 |        - added 'topLevel' keyword to only return attributes that are not
 |          compound children; may not be used in combination with
 |          'descendants'
 |        - added 'descendants' keyword to return all top-level attributes
 |          and all their descendants; note that the standard call may return
 |          some attributes that 'descendants' will not, if there are compound
 |          multi attributes with no existing indices; ie, the standard call
 |          might return "node.parentAttr[-1].childAttr", but the 'descendants'
 |          version would only return childAttr if an index exists for
 |          parentAttr, ie "node.parentAttr[0].childAttr"; may not be used in
 |          combination with 'topLevel'
 |      :rtype: `Attribute` list
 |  
 |  listPresets(self)
 |  
 |  loadPreset(self, presetName)
 |  
 |  lock(self, **kwargs)
 |      lockNode -lock 1
 |  
 |  longName(self, **kwargs)
 |      This produces the same results as `DependNode.name` and is included to simplify looping over lists
 |      of nodes that include both Dag and Depend nodes.
 |      
 |      :rtype: `unicode`
 |  
 |  name(self, update=True, stripNamespace=False, levels=0, long=False, stripUnderWorld=False)
 |      The name of the node
 |      
 |      Returns
 |      -------
 |      unicode
 |      
 |      Parameters
 |      ----------
 |      update : bool
 |          if True, will always query to underlying maya object to get it's
 |          current name (and will therefore detect renames, re-parenting, etc);
 |          if False, it will use a cached value if available (which is slightly
 |          faster, but may be out of date)
 |      stripNamespace : bool
 |          if True, all nodes will have their namespaces stipped off of them
 |          (or a certain number of them, if levels is also used)
 |      levels : int
 |          if stripNamespace is True, then this number will determine the how
 |          many namespaces will be removed; if 0 (the default), then all
 |          leading namespaces will be removed; otherwise, this value gives the
 |          number of left-most levels to strip
 |      long : bool
 |          ignored; included simply to unify the interface between DependNode
 |          and DagNode, to make it easier to loop over lists of them
 |      stripUnderWorld : bool
 |          ignored; included simply to unify the interface between DependNode
 |          and DagNode, to make it easier to loop over lists of them
 |      
 |      
 |      Examples
 |      --------
 |      >>> import pymel.core as pm
 |      >>> pm.newFile(f=1)
 |      ''
 |      >>> node = pm.createNode('blinn')
 |      
 |      >>> pm.namespace(add='foo')
 |      u'foo'
 |      >>> pm.namespace(add='bar', parent='foo')
 |      u'foo:bar'
 |      >>> pm.namespace(add='stuff', parent='foo:bar')
 |      u'foo:bar:stuff'
 |      
 |      >>> node.rename(':foo:bar:stuff:blinn1')
 |      nt.Blinn(u'foo:bar:stuff:blinn1')
 |      
 |      >>> node.name()
 |      u'foo:bar:stuff:blinn1'
 |      >>> node.name(stripNamespace=True)
 |      u'blinn1'
 |      >>> node.name(stripNamespace=True, levels=1)
 |      u'bar:stuff:blinn1'
 |      >>> node.name(stripNamespace=True, levels=2)
 |      u'stuff:blinn1'
 |  
 |  namespace(self, root=False)
 |      Returns the namespace of the object with trailing colon included.
 |      
 |      See `DependNode.parentNamespace` for a variant which does not include
 |      the trailing colon.
 |      
 |      By default, if the object is in the root namespace, an empty string is
 |      returned; if root is True, ':' is returned in this case.
 |      
 |      Returns
 |      -------
 |      unicode
 |  
 |  nextName(self)
 |      Increment the trailing number of the object by 1
 |      
 |      Raises an error if the name has no trailing number.
 |      
 |      >>> from pymel.core import *
 |      >>> SCENE.lambert1.nextName()
 |      DependNodeName(u'lambert2')
 |      
 |      :rtype: `unicode`
 |  
 |  nextUniqueName(self)
 |      Increment the trailing number of the object until a unique name is found
 |      
 |      If there is no trailing number, appends '1' to the name.
 |      
 |      :rtype: `unicode`
 |  
 |  node(self)
 |      for compatibility with Attribute class
 |      
 |      :rtype: `DependNode`
 |  
 |  nodeName(self, **kwargs)
 |      This produces the same results as `DependNode.name` and is included to simplify looping over lists
 |      of nodes that include both Dag and Depend nodes.
 |      
 |      :rtype: `unicode`
 |  
 |  outputs(self, **kwargs)
 |      listConnections -source 0 -destination 1
 |      
 |      :rtype: `PyNode` list
 |  
 |  parentNamespace(self)
 |      Returns the name of the namespace in which this node resides. Namespaces are often used when importing files to prevent name collisions.
 |      
 |      :rtype: `unicode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.parentNamespace`
 |  
 |  pluginName(self)
 |      Returns the name of the plug-in this MFnDependendencyNode was defined in. The name returned is the name of the plug-in on disk, and may contain pathname separators (such as `/') and drive letters (e.g. C:). If this object is not an MFnDependency node, then  MS::kFailure  is returned instead.
 |      
 |      :rtype: `unicode`
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.pluginName`
 |  
 |  prevName(self)
 |      Decrement the trailing number of the object by 1
 |      
 |      Raises an error if the name has no trailing number.
 |      
 |      :rtype: `unicode`
 |  
 |  referenceFile(self)
 |      referenceQuery -file
 |      Return the reference file to which this object belongs.  None if object is not referenced
 |      
 |      :rtype: `FileReference`
 |  
 |  rename(self, name, **kwargs)
 |      :rtype: `DependNode`
 |  
 |  savePreset(self, presetName, custom=None, attributes=[])
 |  
 |  setAttr(self, attr, *args, **kwargs)
 |      Sets the value of a dependency node attribute.  No value for the the attribute is needed when the -l/-k/-s flags are
 |      used. The -type flag is only required when setting a non-numeric attribute. The following chart outlines the syntax of
 |      setAttr for non-numeric data types: TYPEbelow means any number of values of type TYPE, separated by a space[TYPE]means
 |      that the value of type TYPEis optionalA|Bmeans that either of Aor Bmay appearIn order to run its examples, first execute
 |      these commands to create the sample attribute types:sphere -n node; addAttr -ln short2Attr -at short2; addAttr -ln
 |      short2a -p short2Attr -at short; addAttr -ln short2b -p short2Attr -at short; addAttr -ln short3Attr -at short3; addAttr
 |      -ln short3a -p short3Attr -at short; addAttr -ln short3b -p short3Attr -at short; addAttr -ln short3c -p short3Attr -at
 |      short; addAttr -ln long2Attr -at long2; addAttr -ln long2a -p long2Attr -at long; addAttr -ln long2b -p long2Attr -at
 |      long; addAttr -ln long3Attr -at long3; addAttr -ln long3a -p long3Attr -at long; addAttr -ln long3b -p long3Attr -at
 |      long; addAttr -ln long3c -p long3Attr -at long; addAttr -ln float2Attr -at float2; addAttr -ln float2a -p float2Attr -at
 |      float; addAttr -ln float2b -p float2Attr -at float; addAttr -ln float3Attr -at float3; addAttr -ln float3a -p float3Attr
 |      -at float; addAttr -ln float3b -p float3Attr -at float; addAttr -ln float3c -p float3Attr -at float; addAttr -ln
 |      double2Attr -at double2; addAttr -ln double2a -p double2Attr -at double; addAttr -ln double2b -p double2Attr -at double;
 |      addAttr -ln double3Attr -at double3; addAttr -ln double3a -p double3Attr -at double; addAttr -ln double3b -p double3Attr
 |      -at double; addAttr -ln double3c -p double3Attr -at double; addAttr -ln int32ArrayAttr -dt Int32Array; addAttr -ln
 |      doubleArrayAttr -dt doubleArray; addAttr -ln pointArrayAttr -dt pointArray; addAttr -ln vectorArrayAttr -dt vectorArray;
 |      addAttr -ln stringArrayAttr -dt stringArray; addAttr -ln stringAttr -dt string; addAttr -ln matrixAttr -dt matrix;
 |      addAttr -ln sphereAttr -dt sphere; addAttr -ln coneAttr -dt cone; addAttr -ln meshAttr -dt mesh; addAttr -ln latticeAttr
 |      -dt lattice; addAttr -ln spectrumRGBAttr -dt spectrumRGB; addAttr -ln reflectanceRGBAttr -dt reflectanceRGB; addAttr -ln
 |      componentListAttr -dt componentList; addAttr -ln attrAliasAttr -dt attributeAlias; addAttr -ln curveAttr -dt nurbsCurve;
 |      addAttr -ln surfaceAttr -dt nurbsSurface; addAttr -ln trimFaceAttr -dt nurbsTrimface; addAttr -ln polyFaceAttr -dt
 |      polyFaces; -type short2Array of two short integersValue Syntaxshort shortValue Meaningvalue1 value2Mel ExamplesetAttr
 |      node.short2Attr -type short2 1 2;Python Examplecmds.setAttr('node.short2Attr',1,2,type='short2')-type short3Array of
 |      three short integersValue Syntaxshort short shortValue Meaningvalue1 value2 value3Mel ExamplesetAttr node.short3Attr
 |      -type short3 1 2 3;Python Examplecmds.setAttr('node.short3Attr',1,2,3,type='short3')-type long2Array of two long
 |      integersValue Syntaxlong longValue Meaningvalue1 value2Mel ExamplesetAttr node.long2Attr -type long2 1000000
 |      2000000;Python Examplecmds.setAttr('node.long2Attr',1000000,2000000,type='long2')-type long3Array of three long
 |      integersValue Syntaxlong long longValue Meaningvalue1 value2 value3Mel ExamplesetAttr node.long3Attr -type long3 1000000
 |      2000000 3000000;Python Examplecmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')-type
 |      Int32ArrayVariable length array of long integersValue SyntaxValue MeaningMel ExamplesetAttr node.int32ArrayAttr -type
 |      Int32Array 2 12 75;Python Examplecmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')-type float2Array of two
 |      floatsValue Syntaxfloat floatValue Meaningvalue1 value2Mel ExamplesetAttr node.float2Attr -type float2 1.1 2.2;Python
 |      Examplecmds.setAttr('node.float2Attr',1.1,2.2,type='float2')-type float3Array of three floatsValue Syntaxfloat float
 |      floatValue Meaningvalue1 value2 value3Mel ExamplesetAttr node.float3Attr -type float3 1.1 2.2 3.3;Python
 |      Examplecmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')-type double2Array of two doublesValue Syntaxdouble
 |      doubleValue Meaningvalue1 value2Mel ExamplesetAttr node.double2Attr -type double2 1.1 2.2;Python
 |      Examplecmds.setAttr('node.double2Attr',1.1,2.2,type='double2')-type double3Array of three doublesValue Syntaxdouble
 |      double doubleValue Meaningvalue1 value2 value3Mel ExamplesetAttr node.double3Attr -type double3 1.1 2.2 3.3;Python
 |      Examplecmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')-type doubleArrayVariable length array of doublesValue
 |      SyntaxValue MeaningMel ExamplesetAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;Python Examplecmds.setAttr(
 |      node.doubleArrayAttr, (2, 3.14159, 2.782,), type=doubleArray)-type matrix4x4 matrix of doublesValue Syntaxdouble double
 |      double doubledouble double double doubledouble double double doubledouble double double doubleValue Meaningrow1col1
 |      row1col2 row1col3 row1col4row2col1 row2col2 row2col3 row2col4row3col1 row3col2 row3col3 row3col4row4col1 row4col2
 |      row4col3 row4col4Alternate Syntaxstring double double doubledouble double doubleintegerdouble double doubledouble double
 |      doubledouble double doubledouble double doubledouble double doubledouble double doubledouble double double doubledouble
 |      double double doubledouble double doublebooleanAlternate MeaningxformscaleX scaleY scaleZrotateX rotateY
 |      rotateZrotationOrder (0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)translateX translateY translateZshearXY shearXZ
 |      shearYZscalePivotX scalePivotY scalePivotZscaleTranslationX scaleTranslationY scaleTranslationZrotatePivotX rotatePivotY
 |      rotatePivotZrotateTranslationX rotateTranslationY rotateTranslationZrotateOrientW rotateOrientX rotateOrientY
 |      rotateOrientZjointOrientW jointOrientX jointOrientY jointOrientZinverseParentScaleX inverseParentScaleY
 |      inverseParentScaleZcompensateForParentScale Mel ExamplesetAttr node.matrixAttr -type matrix1 0 0 0 0 1 0 0 0 0 1 0 2 3 4
 |      1;setAttr node.matrixAttr -type matrixxform1 1 1 0 0 0 0 2 3 4 0 0 00 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0
 |      false;Python Examplecmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,3,4,1),type='matrix')cmds.setAttr('node.ma
 |      trixAttr','xform',(1,1,1),(0,0,0),0,(2,3,4),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,ty
 |      pe=matrix)-type pointArrayVariable length array of pointsValue SyntaxValue MeaningMel ExamplesetAttr node.pointArrayAttr
 |      -type pointArray 2 1 1 1 1 2 2 2 1;Python
 |      Examplecmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='pointArray')-type vectorArrayVariable length array
 |      of vectorsValue SyntaxValue MeaningMel ExamplesetAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2 2;Python
 |      Examplecmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vectorArray')-type stringCharacter stringValue
 |      SyntaxstringValue MeaningcharacterStringValueMel ExamplesetAttr node.stringAttr -type stringblarg;Python
 |      Examplecmds.setAttr('node.stringAttr',blarg,type=string)-type stringArrayVariable length array of stringsValue
 |      SyntaxValue MeaningMel ExamplesetAttr node.stringArrayAttr -type stringArray 3 abc;Python
 |      Examplecmds.setAttr('node.stringArrayAttr',3,a,b,c,type='stringArray')-type sphereSphere dataValue SyntaxdoubleValue
 |      MeaningsphereRadiusExamplesetAttr node.sphereAttr -type sphere 5.0;-type coneCone dataValue Syntaxdouble doubleValue
 |      MeaningconeAngle coneCapMel ExamplesetAttr node.coneAttr -type cone 45.0 5.0;Python
 |      Examplecmds.setAttr('node.coneAttr',45.0,5.0,type='cone')-type reflectanceRGBReflectance dataValue Syntaxdouble double
 |      doubleValue MeaningredReflect greenReflect blueReflectMel ExamplesetAttr node.reflectanceRGBAttr -type reflectanceRGB
 |      0.5 0.5 0.1;Python Examplecmds.setAttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')-type
 |      spectrumRGBSpectrum dataValue Syntaxdouble double doubleValue MeaningredSpectrum greenSpectrum blueSpectrumMel
 |      ExamplesetAttr node.spectrumRGBAttr -type spectrumRGB 0.5 0.5 0.1;Python
 |      Examplecmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')-type componentListVariable length array of
 |      componentsValue SyntaxValue MeaningMel ExamplesetAttr node.componentListAttr -type componentList 3 cv[1] cv[12]
 |      cv[3];Python Examplecmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv[3]',type='componentList')-type
 |      attributeAliasString alias dataValue Syntaxstring stringValue MeaningnewAlias currentNameMel ExamplesetAttr
 |      node.attrAliasAttr -type attributeAliasGoUp, translateY, GoLeft, translateX;Python
 |      Examplecmds.setAttr('node.attrAliasAttr',(GoUp, translateY,GoLeft, translateX),type='attributeAlias')-type
 |      nurbsCurveNURBS curve dataValue SyntaxValue MeaningMel Example// degree is the degree of the curve(range 1-7)// spans is
 |      the number of spans // form is open (0), closed (1), periodic (2)// dimension is 2 or 3, depending on the dimension of
 |      the curve// isRational is true if the curve CVs contain a rational component // knotCount is the size of the knot list//
 |      knotValue is a single entry in the knot list// cvCount is the number of CVs in the curve//  xCVValue,yCVValue,[zCVValue]
 |      [wCVValue] is a single CV.//  zCVValue is only present when dimension is 3.//  wCVValue is only present when isRational
 |      is true.//setAttr node.curveAttr -type nurbsCurve 3 1 0 no 36 0 0 0 1 1 14 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;-type
 |      nurbsSurfaceNURBS surface dataValue Syntaxint int int int bool Value MeaninguDegree vDegree uForm vForm
 |      isRationalTRIM|NOTRIMExample// uDegree is degree of the surface in U direction (range 1-7)// vDegree is degree of the
 |      surface in V direction (range 1-7)// uForm is open (0), closed (1), periodic (2) in U direction// vForm is open (0),
 |      closed (1), periodic (2) in V direction// isRational is true if the surface CVs contain a rational component//
 |      uKnotCount is the size of the U knot list//  uKnotValue is a single entry in the U knot list// vKnotCount is the size of
 |      the V knot list//  vKnotValue is a single entry in the V knot list// If TRIMis specified then additional trim
 |      information is expected// If NOTRIMis specified then the surface is not trimmed// cvCount is the number of CVs in the
 |      surface//  xCVValue,yCVValue,zCVValue [wCVValue]is a single CV.//  zCVValue is only present when dimension is 3.//
 |      wCVValue is only present when isRational is true//setAttr node.surfaceAttr -type nurbsSurface 3 3 0 0 no 6 0 0 0 1 1 16
 |      0 0 0 1 1 116 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0-1 3 0 -1 1 0 -1 -1 0 -1 -3 01 3 0 1 1 0 1 -1 0 1 -3 03 3 0 3 1 0 3 -1 0 3 -3
 |      0;-type nurbsTrimfaceNURBS trim face dataValue SyntaxValue MeaningExample// flipNormal if true turns the surface inside
 |      out// boundaryCount: number of boundaries// boundaryType: // tedgeCountOnBoundary    : number of edges in a boundary//
 |      splineCountOnEdge    : number of splines in an edge in// edgeTolerance        : tolerance used to build the 3d edge//
 |      isEdgeReversed        : if true, the edge is backwards// geometricContinuity    : if true, the edge is tangent
 |      continuous// splineCountOnPedge    : number of splines in a 2d edge// isMonotone            : if true, curvature is
 |      monotone// pedgeTolerance        : tolerance for the 2d edge//-type polyFacePolygon face dataValue SyntaxfhmfmhmufcValue
 |      MeaningfhmfmhmufcExample// This data type (polyFace) is meant to be used in file I/O// after setAttrs have been written
 |      out for vertex position// arrays, edge connectivity arrays (with corresponding start// and end vertex descriptions),
 |      texture coordinate arrays and// color arrays.  The reason is that this data type references// all of its data through
 |      ids created by the former types.//// fspecifies the ids of the edges making up a face -//     negative value if the edge
 |      is reversed in the face// hspecifies the ids of the edges making up a hole -//     negative value if the edge is
 |      reversed in the face// mfspecifies the ids of texture coordinates (uvs) for a face.//     This data type is obsolete as
 |      of version 3.0. It is replaced by mu.// mhspecifies the ids of texture coordinates (uvs) for a hole//     This data type
 |      is obsolete as of version 3.0. It is replaced by mu.// muThe  first argument refers to the uv set. This is a zero-
 |      based//     integer number. The second argument refers to the number of vertices (n)//     on the face which have valid
 |      uv values. The last n values are the uv//     ids of the texture coordinates (uvs) for the face. These indices//     are
 |      what used to be represented by the mfand mhspecification.//     There may be more than one muspecification, one for each
 |      unique uv set.// fcspecifies the color index values for a face//setAttr node.polyFaceAttr -type polyFaces f3 1 2 3 fc3 4
 |      4 6;-type meshPolygonal meshValue SyntaxValue Meaningvvn[vtesmooth|hard]Example// vspecifies the vertices of the
 |      polygonal mesh// vnspecifies the normal of each vertex// vtis optional and specifies a U,V texture coordinate for each
 |      vertex// especifies the edge connectivity information between vertices//setAttr node.meshAttr -type mesh v3 0 0 0 0 1 0
 |      0 0 1vn3 1 0 0 1 0 0 1 0 0vt3 0 0 0 1 1 0e3 0 1 hard1 2 hard2 0 hard;-type latticeLattice dataValue SyntaxValue
 |      MeaningsDivisionCount tDivisionCount uDivisionCountExample// sDivisionCount is the horizontal lattice division count//
 |      tDivisionCount is the vertical lattice division count// uDivisionCount is the depth lattice division count// pointCount
 |      is the total number of lattice points// pointX,pointY,pointZ is one lattice point.  The list is//   specified varying
 |      first in S, then in T, last in U so the//   first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)//setAttr node.latticeAttr
 |      -type lattice 2 5 2 20-2 -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -22 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2-2 -2 2 2 -2 2 -2 -1
 |      2 2 -1 2 -2 0 22 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;In query mode, return type is based on queried flag.
 |      
 |      Flags:
 |        - alteredValue : av              (bool)          [create]
 |            The value is only the current value, which may change in the next evalution (if the attribute has an incoming
 |            connection). This flag is only used during file I/O, so that attributes with incoming connections do not have their data
 |            overwritten during the first evaluation after a file is opened.
 |      
 |        - caching : ca                   (bool)          [create]
 |            Sets the attribute's internal caching on or off. Not all attributes can be defined as caching. Only those attributes
 |            that are not defined by default to be cached can be made caching.  As well, multi attribute elements cannot be made
 |            caching. Caching also affects child attributes for compound attributes.
 |      
 |        - capacityHint : ch              (int)           [create]
 |            Used to provide a memory allocation hint to attributes where the -size flag cannot provide enough information. This flag
 |            is optional and is primarily intended to be used during file I/O. Only certain attributes make use of this flag, and the
 |            interpretation of the flag value varies per attribute. This flag is currently used by (node.attribute): mesh.face -
 |            hints the total number of elements in the face edge listsFlag can have multiple arguments, passed either as a tuple or a
 |            list.
 |      
 |        - channelBox : cb                (bool)          [create]
 |            Sets the attribute's display in the channelBox on or off. Keyable attributes are always display in the channelBox
 |            regardless of the channelBox settting.
 |      
 |        - clamp : c                      (bool)          [create]
 |            For numeric attributes, if the value is outside the range of the attribute, clamp it to the min or max instead of
 |            failing
 |      
 |        - keyable : k                    (bool)          [create]
 |            Sets the attribute's keyable state on or off.
 |      
 |        - lock : l                       (bool)          [create]
 |            Sets the attribute's lock state on or off.
 |      
 |        - size : s                       (int)           [create]
 |            Defines the size of a multi-attribute array. This is only a hint, used to help allocate memory as efficiently as
 |            possible.
 |      
 |        - type : typ                     (unicode)       [create]
 |            Identifies the type of data.  If the -type flag is not present, a numeric type is assumed.
 |      
 |      
 |      Derived from mel command `maya.cmds.setAttr`
 |  
 |  setDoNotWrite(self, flag)
 |      Use this method to mark the "do not write" state of this node. If set, this node will not be saved when the Maya model is written out.
 |      
 |      :Parameters:
 |          flag : `bool`
 |              True if the node should not be saved. 
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.setDoNotWrite`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  setDynamicAttr(self, attr, *args, **kwargs)
 |      Sets the value of a dependency node attribute.  No value for the the attribute is needed when the -l/-k/-s flags are
 |      used. The -type flag is only required when setting a non-numeric attribute. The following chart outlines the syntax of
 |      setAttr for non-numeric data types: TYPEbelow means any number of values of type TYPE, separated by a space[TYPE]means
 |      that the value of type TYPEis optionalA|Bmeans that either of Aor Bmay appearIn order to run its examples, first execute
 |      these commands to create the sample attribute types:sphere -n node; addAttr -ln short2Attr -at short2; addAttr -ln
 |      short2a -p short2Attr -at short; addAttr -ln short2b -p short2Attr -at short; addAttr -ln short3Attr -at short3; addAttr
 |      -ln short3a -p short3Attr -at short; addAttr -ln short3b -p short3Attr -at short; addAttr -ln short3c -p short3Attr -at
 |      short; addAttr -ln long2Attr -at long2; addAttr -ln long2a -p long2Attr -at long; addAttr -ln long2b -p long2Attr -at
 |      long; addAttr -ln long3Attr -at long3; addAttr -ln long3a -p long3Attr -at long; addAttr -ln long3b -p long3Attr -at
 |      long; addAttr -ln long3c -p long3Attr -at long; addAttr -ln float2Attr -at float2; addAttr -ln float2a -p float2Attr -at
 |      float; addAttr -ln float2b -p float2Attr -at float; addAttr -ln float3Attr -at float3; addAttr -ln float3a -p float3Attr
 |      -at float; addAttr -ln float3b -p float3Attr -at float; addAttr -ln float3c -p float3Attr -at float; addAttr -ln
 |      double2Attr -at double2; addAttr -ln double2a -p double2Attr -at double; addAttr -ln double2b -p double2Attr -at double;
 |      addAttr -ln double3Attr -at double3; addAttr -ln double3a -p double3Attr -at double; addAttr -ln double3b -p double3Attr
 |      -at double; addAttr -ln double3c -p double3Attr -at double; addAttr -ln int32ArrayAttr -dt Int32Array; addAttr -ln
 |      doubleArrayAttr -dt doubleArray; addAttr -ln pointArrayAttr -dt pointArray; addAttr -ln vectorArrayAttr -dt vectorArray;
 |      addAttr -ln stringArrayAttr -dt stringArray; addAttr -ln stringAttr -dt string; addAttr -ln matrixAttr -dt matrix;
 |      addAttr -ln sphereAttr -dt sphere; addAttr -ln coneAttr -dt cone; addAttr -ln meshAttr -dt mesh; addAttr -ln latticeAttr
 |      -dt lattice; addAttr -ln spectrumRGBAttr -dt spectrumRGB; addAttr -ln reflectanceRGBAttr -dt reflectanceRGB; addAttr -ln
 |      componentListAttr -dt componentList; addAttr -ln attrAliasAttr -dt attributeAlias; addAttr -ln curveAttr -dt nurbsCurve;
 |      addAttr -ln surfaceAttr -dt nurbsSurface; addAttr -ln trimFaceAttr -dt nurbsTrimface; addAttr -ln polyFaceAttr -dt
 |      polyFaces; -type short2Array of two short integersValue Syntaxshort shortValue Meaningvalue1 value2Mel ExamplesetAttr
 |      node.short2Attr -type short2 1 2;Python Examplecmds.setAttr('node.short2Attr',1,2,type='short2')-type short3Array of
 |      three short integersValue Syntaxshort short shortValue Meaningvalue1 value2 value3Mel ExamplesetAttr node.short3Attr
 |      -type short3 1 2 3;Python Examplecmds.setAttr('node.short3Attr',1,2,3,type='short3')-type long2Array of two long
 |      integersValue Syntaxlong longValue Meaningvalue1 value2Mel ExamplesetAttr node.long2Attr -type long2 1000000
 |      2000000;Python Examplecmds.setAttr('node.long2Attr',1000000,2000000,type='long2')-type long3Array of three long
 |      integersValue Syntaxlong long longValue Meaningvalue1 value2 value3Mel ExamplesetAttr node.long3Attr -type long3 1000000
 |      2000000 3000000;Python Examplecmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')-type
 |      Int32ArrayVariable length array of long integersValue SyntaxValue MeaningMel ExamplesetAttr node.int32ArrayAttr -type
 |      Int32Array 2 12 75;Python Examplecmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')-type float2Array of two
 |      floatsValue Syntaxfloat floatValue Meaningvalue1 value2Mel ExamplesetAttr node.float2Attr -type float2 1.1 2.2;Python
 |      Examplecmds.setAttr('node.float2Attr',1.1,2.2,type='float2')-type float3Array of three floatsValue Syntaxfloat float
 |      floatValue Meaningvalue1 value2 value3Mel ExamplesetAttr node.float3Attr -type float3 1.1 2.2 3.3;Python
 |      Examplecmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')-type double2Array of two doublesValue Syntaxdouble
 |      doubleValue Meaningvalue1 value2Mel ExamplesetAttr node.double2Attr -type double2 1.1 2.2;Python
 |      Examplecmds.setAttr('node.double2Attr',1.1,2.2,type='double2')-type double3Array of three doublesValue Syntaxdouble
 |      double doubleValue Meaningvalue1 value2 value3Mel ExamplesetAttr node.double3Attr -type double3 1.1 2.2 3.3;Python
 |      Examplecmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')-type doubleArrayVariable length array of doublesValue
 |      SyntaxValue MeaningMel ExamplesetAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;Python Examplecmds.setAttr(
 |      node.doubleArrayAttr, (2, 3.14159, 2.782,), type=doubleArray)-type matrix4x4 matrix of doublesValue Syntaxdouble double
 |      double doubledouble double double doubledouble double double doubledouble double double doubleValue Meaningrow1col1
 |      row1col2 row1col3 row1col4row2col1 row2col2 row2col3 row2col4row3col1 row3col2 row3col3 row3col4row4col1 row4col2
 |      row4col3 row4col4Alternate Syntaxstring double double doubledouble double doubleintegerdouble double doubledouble double
 |      doubledouble double doubledouble double doubledouble double doubledouble double doubledouble double double doubledouble
 |      double double doubledouble double doublebooleanAlternate MeaningxformscaleX scaleY scaleZrotateX rotateY
 |      rotateZrotationOrder (0=XYZ, 1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)translateX translateY translateZshearXY shearXZ
 |      shearYZscalePivotX scalePivotY scalePivotZscaleTranslationX scaleTranslationY scaleTranslationZrotatePivotX rotatePivotY
 |      rotatePivotZrotateTranslationX rotateTranslationY rotateTranslationZrotateOrientW rotateOrientX rotateOrientY
 |      rotateOrientZjointOrientW jointOrientX jointOrientY jointOrientZinverseParentScaleX inverseParentScaleY
 |      inverseParentScaleZcompensateForParentScale Mel ExamplesetAttr node.matrixAttr -type matrix1 0 0 0 0 1 0 0 0 0 1 0 2 3 4
 |      1;setAttr node.matrixAttr -type matrixxform1 1 1 0 0 0 0 2 3 4 0 0 00 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1 0
 |      false;Python Examplecmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,3,4,1),type='matrix')cmds.setAttr('node.ma
 |      trixAttr','xform',(1,1,1),(0,0,0),0,(2,3,4),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,ty
 |      pe=matrix)-type pointArrayVariable length array of pointsValue SyntaxValue MeaningMel ExamplesetAttr node.pointArrayAttr
 |      -type pointArray 2 1 1 1 1 2 2 2 1;Python
 |      Examplecmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='pointArray')-type vectorArrayVariable length array
 |      of vectorsValue SyntaxValue MeaningMel ExamplesetAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2 2;Python
 |      Examplecmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vectorArray')-type stringCharacter stringValue
 |      SyntaxstringValue MeaningcharacterStringValueMel ExamplesetAttr node.stringAttr -type stringblarg;Python
 |      Examplecmds.setAttr('node.stringAttr',blarg,type=string)-type stringArrayVariable length array of stringsValue
 |      SyntaxValue MeaningMel ExamplesetAttr node.stringArrayAttr -type stringArray 3 abc;Python
 |      Examplecmds.setAttr('node.stringArrayAttr',3,a,b,c,type='stringArray')-type sphereSphere dataValue SyntaxdoubleValue
 |      MeaningsphereRadiusExamplesetAttr node.sphereAttr -type sphere 5.0;-type coneCone dataValue Syntaxdouble doubleValue
 |      MeaningconeAngle coneCapMel ExamplesetAttr node.coneAttr -type cone 45.0 5.0;Python
 |      Examplecmds.setAttr('node.coneAttr',45.0,5.0,type='cone')-type reflectanceRGBReflectance dataValue Syntaxdouble double
 |      doubleValue MeaningredReflect greenReflect blueReflectMel ExamplesetAttr node.reflectanceRGBAttr -type reflectanceRGB
 |      0.5 0.5 0.1;Python Examplecmds.setAttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')-type
 |      spectrumRGBSpectrum dataValue Syntaxdouble double doubleValue MeaningredSpectrum greenSpectrum blueSpectrumMel
 |      ExamplesetAttr node.spectrumRGBAttr -type spectrumRGB 0.5 0.5 0.1;Python
 |      Examplecmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')-type componentListVariable length array of
 |      componentsValue SyntaxValue MeaningMel ExamplesetAttr node.componentListAttr -type componentList 3 cv[1] cv[12]
 |      cv[3];Python Examplecmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv[3]',type='componentList')-type
 |      attributeAliasString alias dataValue Syntaxstring stringValue MeaningnewAlias currentNameMel ExamplesetAttr
 |      node.attrAliasAttr -type attributeAliasGoUp, translateY, GoLeft, translateX;Python
 |      Examplecmds.setAttr('node.attrAliasAttr',(GoUp, translateY,GoLeft, translateX),type='attributeAlias')-type
 |      nurbsCurveNURBS curve dataValue SyntaxValue MeaningMel Example// degree is the degree of the curve(range 1-7)// spans is
 |      the number of spans // form is open (0), closed (1), periodic (2)// dimension is 2 or 3, depending on the dimension of
 |      the curve// isRational is true if the curve CVs contain a rational component // knotCount is the size of the knot list//
 |      knotValue is a single entry in the knot list// cvCount is the number of CVs in the curve//  xCVValue,yCVValue,[zCVValue]
 |      [wCVValue] is a single CV.//  zCVValue is only present when dimension is 3.//  wCVValue is only present when isRational
 |      is true.//setAttr node.curveAttr -type nurbsCurve 3 1 0 no 36 0 0 0 1 1 14 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;-type
 |      nurbsSurfaceNURBS surface dataValue Syntaxint int int int bool Value MeaninguDegree vDegree uForm vForm
 |      isRationalTRIM|NOTRIMExample// uDegree is degree of the surface in U direction (range 1-7)// vDegree is degree of the
 |      surface in V direction (range 1-7)// uForm is open (0), closed (1), periodic (2) in U direction// vForm is open (0),
 |      closed (1), periodic (2) in V direction// isRational is true if the surface CVs contain a rational component//
 |      uKnotCount is the size of the U knot list//  uKnotValue is a single entry in the U knot list// vKnotCount is the size of
 |      the V knot list//  vKnotValue is a single entry in the V knot list// If TRIMis specified then additional trim
 |      information is expected// If NOTRIMis specified then the surface is not trimmed// cvCount is the number of CVs in the
 |      surface//  xCVValue,yCVValue,zCVValue [wCVValue]is a single CV.//  zCVValue is only present when dimension is 3.//
 |      wCVValue is only present when isRational is true//setAttr node.surfaceAttr -type nurbsSurface 3 3 0 0 no 6 0 0 0 1 1 16
 |      0 0 0 1 1 116 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0-1 3 0 -1 1 0 -1 -1 0 -1 -3 01 3 0 1 1 0 1 -1 0 1 -3 03 3 0 3 1 0 3 -1 0 3 -3
 |      0;-type nurbsTrimfaceNURBS trim face dataValue SyntaxValue MeaningExample// flipNormal if true turns the surface inside
 |      out// boundaryCount: number of boundaries// boundaryType: // tedgeCountOnBoundary    : number of edges in a boundary//
 |      splineCountOnEdge    : number of splines in an edge in// edgeTolerance        : tolerance used to build the 3d edge//
 |      isEdgeReversed        : if true, the edge is backwards// geometricContinuity    : if true, the edge is tangent
 |      continuous// splineCountOnPedge    : number of splines in a 2d edge// isMonotone            : if true, curvature is
 |      monotone// pedgeTolerance        : tolerance for the 2d edge//-type polyFacePolygon face dataValue SyntaxfhmfmhmufcValue
 |      MeaningfhmfmhmufcExample// This data type (polyFace) is meant to be used in file I/O// after setAttrs have been written
 |      out for vertex position// arrays, edge connectivity arrays (with corresponding start// and end vertex descriptions),
 |      texture coordinate arrays and// color arrays.  The reason is that this data type references// all of its data through
 |      ids created by the former types.//// fspecifies the ids of the edges making up a face -//     negative value if the edge
 |      is reversed in the face// hspecifies the ids of the edges making up a hole -//     negative value if the edge is
 |      reversed in the face// mfspecifies the ids of texture coordinates (uvs) for a face.//     This data type is obsolete as
 |      of version 3.0. It is replaced by mu.// mhspecifies the ids of texture coordinates (uvs) for a hole//     This data type
 |      is obsolete as of version 3.0. It is replaced by mu.// muThe  first argument refers to the uv set. This is a zero-
 |      based//     integer number. The second argument refers to the number of vertices (n)//     on the face which have valid
 |      uv values. The last n values are the uv//     ids of the texture coordinates (uvs) for the face. These indices//     are
 |      what used to be represented by the mfand mhspecification.//     There may be more than one muspecification, one for each
 |      unique uv set.// fcspecifies the color index values for a face//setAttr node.polyFaceAttr -type polyFaces f3 1 2 3 fc3 4
 |      4 6;-type meshPolygonal meshValue SyntaxValue Meaningvvn[vtesmooth|hard]Example// vspecifies the vertices of the
 |      polygonal mesh// vnspecifies the normal of each vertex// vtis optional and specifies a U,V texture coordinate for each
 |      vertex// especifies the edge connectivity information between vertices//setAttr node.meshAttr -type mesh v3 0 0 0 0 1 0
 |      0 0 1vn3 1 0 0 1 0 0 1 0 0vt3 0 0 0 1 1 0e3 0 1 hard1 2 hard2 0 hard;-type latticeLattice dataValue SyntaxValue
 |      MeaningsDivisionCount tDivisionCount uDivisionCountExample// sDivisionCount is the horizontal lattice division count//
 |      tDivisionCount is the vertical lattice division count// uDivisionCount is the depth lattice division count// pointCount
 |      is the total number of lattice points// pointX,pointY,pointZ is one lattice point.  The list is//   specified varying
 |      first in S, then in T, last in U so the//   first two entries are (S=0,T=0,U=0) (s=1,T=0,U=0)//setAttr node.latticeAttr
 |      -type lattice 2 5 2 20-2 -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -22 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2-2 -2 2 2 -2 2 -2 -1
 |      2 2 -1 2 -2 0 22 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;In query mode, return type is based on queried flag.
 |      
 |      same as `DependNode.setAttr` with the force flag set to True.  This causes
 |              the attribute to be created based on the passed input value.
 |      
 |      Flags:
 |        - alteredValue : av              (bool)          [create]
 |            The value is only the current value, which may change in the next evalution (if the attribute has an incoming
 |            connection). This flag is only used during file I/O, so that attributes with incoming connections do not have their data
 |            overwritten during the first evaluation after a file is opened.
 |      
 |        - caching : ca                   (bool)          [create]
 |            Sets the attribute's internal caching on or off. Not all attributes can be defined as caching. Only those attributes
 |            that are not defined by default to be cached can be made caching.  As well, multi attribute elements cannot be made
 |            caching. Caching also affects child attributes for compound attributes.
 |      
 |        - capacityHint : ch              (int)           [create]
 |            Used to provide a memory allocation hint to attributes where the -size flag cannot provide enough information. This flag
 |            is optional and is primarily intended to be used during file I/O. Only certain attributes make use of this flag, and the
 |            interpretation of the flag value varies per attribute. This flag is currently used by (node.attribute): mesh.face -
 |            hints the total number of elements in the face edge listsFlag can have multiple arguments, passed either as a tuple or a
 |            list.
 |      
 |        - channelBox : cb                (bool)          [create]
 |            Sets the attribute's display in the channelBox on or off. Keyable attributes are always display in the channelBox
 |            regardless of the channelBox settting.
 |      
 |        - clamp : c                      (bool)          [create]
 |            For numeric attributes, if the value is outside the range of the attribute, clamp it to the min or max instead of
 |            failing
 |      
 |        - keyable : k                    (bool)          [create]
 |            Sets the attribute's keyable state on or off.
 |      
 |        - lock : l                       (bool)          [create]
 |            Sets the attribute's lock state on or off.
 |      
 |        - size : s                       (int)           [create]
 |            Defines the size of a multi-attribute array. This is only a hint, used to help allocate memory as efficiently as
 |            possible.
 |      
 |        - type : typ                     (unicode)       [create]
 |            Identifies the type of data.  If the -type flag is not present, a numeric type is assumed.
 |      
 |      
 |      Derived from mel command `maya.cmds.setAttr`
 |  
 |  setIcon(self, filename)
 |      Associates a custom icon with the node for display in the Maya UI. Currently the icon only shows up in Outliner panels (the DAG Outliner, Graph Editor and Dope Sheet).
 |      
 |      :Parameters:
 |          filename : `unicode`
 |              specifies the name of the image file defining the icon, or the empty string (i.e. "") to revert to using Maya's default. The filename must be a PNG file (.png) and may either be an absolute pathname or be relative to the XBMLANGPATH environment variable.
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.setIcon`
 |  
 |  setLocked(self, lock)
 |      Locks or unlocks this node.
 |      
 |      :Parameters:
 |          lock : `bool`
 |              If true then node will be locked.
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.setLocked`
 |  
 |  shadingGroups(self)
 |      list any shading groups in the future of this object - works for
 |      shading nodes, transforms, and shapes
 |      
 |      Also see listSets(type=1) - which returns which 'rendering sets' the
 |      object is a member of (and 'rendering sets' seem to consist only of
 |      shading groups), whereas this method searches the object's future for
 |      any nodes of type 'shadingEngine'.
 |      
 |      :rtype: `DependNode` list
 |  
 |  shortName(self, **kwargs)
 |      This produces the same results as `DependNode.name` and is included to simplify looping over lists
 |      of nodes that include both Dag and Depend nodes.
 |      
 |      Returns
 |      -------
 |      unicode
 |  
 |  sources(self, **kwargs)
 |      listConnections -source 1 -destination 0
 |      
 |      :rtype: `PyNode` list
 |  
 |  stripNum(self)
 |      Return the name of the node with trailing numbers stripped off. If no trailing numbers are found
 |      the name will be returned unchanged.
 |      
 |      >>> from pymel.core import *
 |      >>> SCENE.lambert1.stripNum()
 |      u'lambert'
 |      
 |      :rtype: `unicode`
 |  
 |  type = nodeType(node, **kwargs)
 |      This command returns a string which identifies the given node's type. When no flags are used, the unique type name is
 |      returned.  This can be useful for seeing if two nodes are of the same type. When the apiflag is used, the MFn::Type of
 |      the node is returned. This can be useful for seeing if a plug-in node belongs to a given class. The apiflag cannot be
 |      used in conjunction with any other flags. When the derivedflag is used, the command returns a string array containing
 |      the names of all the currently known node types which derive from the node type of the given object. When the
 |      inheritedflag is used, the command returns a string array containing the names of all the base node types inherited by
 |      the the given node. If the isTypeNameflag is present then the argument provided to the command is taken to be the name
 |      of a node type rather than the name of a specific node. This makes it possible to query the hierarchy of node types
 |      without needing to have instances of each node type.
 |      
 |      Note: this will return the dg node type for an object, like maya.cmds.nodeType,
 |          NOT the pymel PyNode class.  For objects like components or attributes,
 |          nodeType will return the dg type of the node to which the PyNode is attached.
 |      
 |          :rtype: `unicode`
 |      
 |      Flags:
 |        - apiType : api                  (bool)          [create]
 |            Return the MFn::Type value (as a string) corresponding to the given node.  This is particularly useful when the given
 |            node is defined by a plug-in, since in this case, the MFn::Type value corresponds to the underlying proxy class. This
 |            flag cannot be used in combination with any of the other flags.
 |      
 |        - derived : d                    (bool)          [create]
 |            Return a string array containing the names of all the currently known node types which derive from the type of the
 |            specified node.
 |      
 |        - inherited : i                  (bool)          [create]
 |            Return a string array containing the names of all the base node types inherited by the specified node.
 |      
 |        - isTypeName : itn               (bool)          [create]
 |            If this flag is present, then the argument provided to the command is the name of a node type rather than the name of a
 |            specific node.                    Flag can have multiple arguments, passed either as a tuple or a list.
 |      
 |      
 |      Derived from mel command `maya.cmds.nodeType`
 |  
 |  unlock(self, **kwargs)
 |      lockNode -lock 0
 |  
 |  ----------------------------------------------------------------------
 |  Class methods inherited from DependNode:
 |  
 |  enableDGTiming(self, enable) from pymel.internal.factories.MetaMayaNodeWrapper
 |      Globally enables or disables the DG node timing mechanism. There are two levels of control for DG node timing.  dgTimerOn()  and  dgTimerOff()  are used to determine which nodes are eligible for timer data collection and this method is used to globally enable or disable the DG node timing mechanism.
 |      
 |      :Parameters:
 |          enable : `bool`
 |              flag to turn timing on or off. 
 |      
 |      Derived from api method `maya.OpenMaya.MFnDependencyNode.enableDGTiming`
 |      
 |      **Undo is not currently supported for this method**
 |  
 |  registerVirtualSubClass(cls, nameRequired=False) from pymel.internal.factories.MetaMayaNodeWrapper
 |      Deprecated
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from DependNode:
 |  
 |  __metaclass__ = <class 'pymel.internal.factories.MetaMayaNodeWrapper'>
 |      A metaclass for creating classes based on node type.  Methods will be added to the new classes
 |      based on info parsed from the docs on their command counterparts.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from pymel.core.general.PyNode:
 |  
 |  __apimfn__(self)
 |  
 |  __eq__(self, other)
 |      :rtype: `bool`
 |  
 |  __ge__(self, other)
 |  
 |  __getitem__(*args, **kwargs)
 |      The function 'pymel.core.general.PyNode.__getitem__' is deprecated and will become unavailable in future pymel versions. Convert to string first using str() or PyNode.name()
 |      
 |      deprecated
 |  
 |  __gt__(self, other)
 |  
 |  __init__(self, *args, **kwargs)
 |  
 |  __le__(self, other)
 |  
 |  __lt__(self, other)
 |  
 |  __ne__(self, other)
 |      :rtype: `bool`
 |  
 |  __nonzero__(self)
 |      :rtype: `bool`
 |  
 |  __radd__(self, other)
 |  
 |  __reduce__(self)
 |      allows PyNodes to be pickled
 |  
 |  addPrefix(self, prefix)
 |      Returns the object's name with a prefix added to the beginning of the name
 |      
 |      :rtype: `other.NameParser`
 |  
 |  connections = listConnections(*args, **kwargs)
 |      This command returns a list of all attributes/objects of a specified type that are connected to the given object(s). If
 |      no objects are specified then the command lists the connections on selected nodes.
 |      
 |      Modifications:
 |        - returns an empty list when the result is None
 |        - returns an empty list (with a warning) when the arg is an empty list, tuple,
 |              set, or frozenset, making it's behavior consistent with when None is
 |              passed, or no args and nothing is selected (would formerly raise a
 |              TypeError)
 |        - When 'connections' flag is True, the attribute pairs are returned in a 2D-array::
 |      
 |              [['checker1.outColor', 'lambert1.color'], ['checker1.color1', 'fractal1.outColor']]
 |      
 |        - added sourceFirst keyword arg. when sourceFirst is true and connections is also true,
 |              the paired list of plugs is returned in (source,destination) order instead of (thisnode,othernode) order.
 |              this puts the pairs in the order that disconnectAttr and connectAttr expect.
 |        - added ability to pass a list of types
 |      
 |          :rtype: `PyNode` list
 |      
 |      Flags:
 |        - connections : c                (bool)          [create]
 |            If true, return both attributes involved in the connection. The one on the specified object is given first.  Default
 |            false.
 |      
 |        - destination : d                (bool)          [create]
 |            Give the attributes/objects that are on the destinationside of connection to the given object.  Default true.
 |      
 |        - exactType : et                 (bool)          [create]
 |            When set to true, -t/type only considers node of this exact type. Otherwise, derived types are also taken into account.
 |      
 |        - plugs : p                      (bool)          [create]
 |            If true, return the connected attribute names; if false, return the connected object names only.  Default false;
 |      
 |        - shapes : sh                    (bool)          [create]
 |            Actually return the shape name instead of the transform when the shape is selected.  Default false.
 |      
 |        - skipConversionNodes : scn      (bool)          [create]
 |            If true, skip over unit conversion nodes and return the node connected to the conversion node on the other side.
 |            Default false.                                          Flag can have multiple arguments, passed either as a tuple or a
 |            list.
 |      
 |        - source : s                     (bool)          [create]
 |            Give the attributes/objects that are on the sourceside of connection to the given object.  Default true.
 |      
 |        - type : t                       (unicode)       [create]
 |            If specified, only take objects of a specified type.
 |      
 |      
 |      Derived from mel command `maya.cmds.listConnections`
 |  
 |  deselect(self)
 |  
 |  exists(self, **kwargs)
 |      objExists
 |  
 |  future = listFuture(*args, **kwargs)
 |      Modifications:
 |        - returns an empty list when the result is None
 |        - added a much needed 'type' filter
 |        - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
 |      
 |          :rtype: `DependNode` list
 |  
 |  history = listHistory(*args, **kwargs)
 |      This command traverses backwards or forwards in the graph from the specified node and returns all of the nodes whose
 |      construction history it passes through. The construction history consists of connections to specific attributes of a
 |      node defined as the creators and results of the node's main data, eg. the curve for a Nurbs Curve node. For information
 |      on history connections through specific plugs use the listConnectionscommand first to find where the history begins then
 |      use this command on the resulting node.
 |      
 |      Modifications:
 |        - returns an empty list when the result is None
 |        - raises a RuntimeError when the arg is an empty list, tuple, set, or
 |              frozenset, making it's behavior consistent with when None is passed, or
 |              no args and nothing is selected (would formerly raise a TypeError)
 |        - added a much needed 'type' filter
 |        - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
 |      
 |          :rtype: `DependNode` list
 |      
 |      Flags:
 |        - allConnections : ac            (bool)          [create]
 |            If specified, the traversal that searches for the history or future will not restrict its traversal across nodes to only
 |            dependent plugs. Thus it will reach all upstream nodes (or all downstream nodes for f/future).
 |      
 |        - allFuture : af                 (bool)          [create]
 |            If listing the future, list all of it. Otherwise if a shape has an attribute that represents its output geometry data,
 |            and that plug is connected, only list the future history downstream from that connection.
 |      
 |        - allGraphs : ag                 (bool)          [create]
 |            This flag is obsolete and has no effect.
 |      
 |        - breadthFirst : bf              (bool)          [create]
 |            The breadth first traversal will return the closest nodes in the traversal first. The depth first traversal will follow
 |            a complete path away from the node, then return to any other paths from the node. Default is depth first.
 |      
 |        - future : f                     (bool)          [create]
 |            List the future instead of the history.
 |      
 |        - futureLocalAttr : fl           (bool)          [query]
 |            This flag allows querying of the local-space future-related attribute(s) on shape nodes.                          Flag
 |            can have multiple arguments, passed either as a tuple or a list.
 |      
 |        - futureWorldAttr : fw           (bool)          [query]
 |            This flag allows querying of the world-space future-related attribute(s) on shape nodes.
 |      
 |        - groupLevels : gl               (bool)          [create]
 |            The node names are grouped depending on the level.  1 is the lead, the rest are grouped with it.
 |      
 |        - historyAttr : ha               (bool)          [query]
 |            This flag allows querying of the attribute where history connects on shape nodes.
 |      
 |        - interestLevel : il             (int)           [create]
 |            If this flag is set, only nodes whose historicallyInteresting attribute value is not less than the value will be listed.
 |            The historicallyInteresting attribute is 0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for
 |            the users.
 |      
 |        - leaf : lf                      (bool)          [create]
 |            If transform is selected, show history for its leaf shape. Default is true.
 |      
 |        - levels : lv                    (int)           [create]
 |            Levels deep to traverse. Setting the number of levels to 0 means do all levels. All levels is the default.
 |      
 |        - pruneDagObjects : pdo          (bool)          [create]
 |            If this flag is set, prune at dag objects.
 |      
 |      
 |      Derived from mel command `maya.cmds.listHistory`
 |  
 |  listConnections(*args, **kwargs)
 |      This command returns a list of all attributes/objects of a specified type that are connected to the given object(s). If
 |      no objects are specified then the command lists the connections on selected nodes.
 |      
 |      Modifications:
 |        - returns an empty list when the result is None
 |        - returns an empty list (with a warning) when the arg is an empty list, tuple,
 |              set, or frozenset, making it's behavior consistent with when None is
 |              passed, or no args and nothing is selected (would formerly raise a
 |              TypeError)
 |        - When 'connections' flag is True, the attribute pairs are returned in a 2D-array::
 |      
 |              [['checker1.outColor', 'lambert1.color'], ['checker1.color1', 'fractal1.outColor']]
 |      
 |        - added sourceFirst keyword arg. when sourceFirst is true and connections is also true,
 |              the paired list of plugs is returned in (source,destination) order instead of (thisnode,othernode) order.
 |              this puts the pairs in the order that disconnectAttr and connectAttr expect.
 |        - added ability to pass a list of types
 |      
 |          :rtype: `PyNode` list
 |      
 |      Flags:
 |        - connections : c                (bool)          [create]
 |            If true, return both attributes involved in the connection. The one on the specified object is given first.  Default
 |            false.
 |      
 |        - destination : d                (bool)          [create]
 |            Give the attributes/objects that are on the destinationside of connection to the given object.  Default true.
 |      
 |        - exactType : et                 (bool)          [create]
 |            When set to true, -t/type only considers node of this exact type. Otherwise, derived types are also taken into account.
 |      
 |        - plugs : p                      (bool)          [create]
 |            If true, return the connected attribute names; if false, return the connected object names only.  Default false;
 |      
 |        - shapes : sh                    (bool)          [create]
 |            Actually return the shape name instead of the transform when the shape is selected.  Default false.
 |      
 |        - skipConversionNodes : scn      (bool)          [create]
 |            If true, skip over unit conversion nodes and return the node connected to the conversion node on the other side.
 |            Default false.                                          Flag can have multiple arguments, passed either as a tuple or a
 |            list.
 |      
 |        - source : s                     (bool)          [create]
 |            Give the attributes/objects that are on the sourceside of connection to the given object.  Default true.
 |      
 |        - type : t                       (unicode)       [create]
 |            If specified, only take objects of a specified type.
 |      
 |      
 |      Derived from mel command `maya.cmds.listConnections`
 |  
 |  listFuture(*args, **kwargs)
 |      Modifications:
 |        - returns an empty list when the result is None
 |        - added a much needed 'type' filter
 |        - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
 |      
 |          :rtype: `DependNode` list
 |  
 |  listHistory(*args, **kwargs)
 |      This command traverses backwards or forwards in the graph from the specified node and returns all of the nodes whose
 |      construction history it passes through. The construction history consists of connections to specific attributes of a
 |      node defined as the creators and results of the node's main data, eg. the curve for a Nurbs Curve node. For information
 |      on history connections through specific plugs use the listConnectionscommand first to find where the history begins then
 |      use this command on the resulting node.
 |      
 |      Modifications:
 |        - returns an empty list when the result is None
 |        - raises a RuntimeError when the arg is an empty list, tuple, set, or
 |              frozenset, making it's behavior consistent with when None is passed, or
 |              no args and nothing is selected (would formerly raise a TypeError)
 |        - added a much needed 'type' filter
 |        - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
 |      
 |          :rtype: `DependNode` list
 |      
 |      Flags:
 |        - allConnections : ac            (bool)          [create]
 |            If specified, the traversal that searches for the history or future will not restrict its traversal across nodes to only
 |            dependent plugs. Thus it will reach all upstream nodes (or all downstream nodes for f/future).
 |      
 |        - allFuture : af                 (bool)          [create]
 |            If listing the future, list all of it. Otherwise if a shape has an attribute that represents its output geometry data,
 |            and that plug is connected, only list the future history downstream from that connection.
 |      
 |        - allGraphs : ag                 (bool)          [create]
 |            This flag is obsolete and has no effect.
 |      
 |        - breadthFirst : bf              (bool)          [create]
 |            The breadth first traversal will return the closest nodes in the traversal first. The depth first traversal will follow
 |            a complete path away from the node, then return to any other paths from the node. Default is depth first.
 |      
 |        - future : f                     (bool)          [create]
 |            List the future instead of the history.
 |      
 |        - futureLocalAttr : fl           (bool)          [query]
 |            This flag allows querying of the local-space future-related attribute(s) on shape nodes.                          Flag
 |            can have multiple arguments, passed either as a tuple or a list.
 |      
 |        - futureWorldAttr : fw           (bool)          [query]
 |            This flag allows querying of the world-space future-related attribute(s) on shape nodes.
 |      
 |        - groupLevels : gl               (bool)          [create]
 |            The node names are grouped depending on the level.  1 is the lead, the rest are grouped with it.
 |      
 |        - historyAttr : ha               (bool)          [query]
 |            This flag allows querying of the attribute where history connects on shape nodes.
 |      
 |        - interestLevel : il             (int)           [create]
 |            If this flag is set, only nodes whose historicallyInteresting attribute value is not less than the value will be listed.
 |            The historicallyInteresting attribute is 0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for
 |            the users.
 |      
 |        - leaf : lf                      (bool)          [create]
 |            If transform is selected, show history for its leaf shape. Default is true.
 |      
 |        - levels : lv                    (int)           [create]
 |            Levels deep to traverse. Setting the number of levels to 0 means do all levels. All levels is the default.
 |      
 |        - pruneDagObjects : pdo          (bool)          [create]
 |            If this flag is set, prune at dag objects.
 |      
 |      
 |      Derived from mel command `maya.cmds.listHistory`
 |  
 |  listSets(self, *args, **kwargs)
 |      Returns list of sets this object belongs
 |      
 |      listSets -o $this
 |      
 |      :rtype: 'PyNode' list
 |  
 |  namespaceList(self)
 |      Useful for cascading references.  Returns all of the namespaces of the calling object as a list
 |      
 |      :rtype: `unicode` list
 |  
 |  nodeType(*args, **kwargs)
 |  
 |  objExists = exists(self, **kwargs)
 |      objExists
 |  
 |  select(self, **kwargs)
 |  
 |  stripNamespace(self, *args, **kwargs)
 |      Returns the object's name with its namespace removed.  The calling instance is unaffected.
 |      The optional levels keyword specifies how many levels of cascading namespaces to strip, starting with the topmost (leftmost).
 |      The default is 0 which will remove all namespaces.
 |      
 |      :rtype: `other.NameParser`
 |  
 |  swapNamespace(self, prefix)
 |      Returns the object's name with its current namespace replaced with the provided one.
 |      The calling instance is unaffected.
 |      
 |      :rtype: `other.NameParser`
 |  
 |  ----------------------------------------------------------------------
 |  Static methods inherited from pymel.core.general.PyNode:
 |  
 |  __new__(cls, *args, **kwargs)
 |      Catch all creation for PyNode classes, creates correct class depending on type passed.
 |      
 |      
 |      For nodes:
 |          MObject
 |          MObjectHandle
 |          MDagPath
 |          string/unicode
 |      
 |      For attributes:
 |          MPlug
 |          MDagPath, MPlug
 |          string/unicode
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from pymel.core.general.PyNode:
 |  
 |  __apiobjects__ = {}
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from pymel.util.utilitytypes.ProxyUnicode:
 |  
 |  __add__(self, *args, **kwargs)
 |      x.__add__(y) <==> x+y
 |  
 |  __delattr__(self, *args, **kwargs)
 |      x.__delattr__('name') <==> del x.name
 |  
 |  __format__(self, *args, **kwargs)
 |      S.__format__(format_spec) -> unicode
 |      
 |      Return a formatted version of S as described by format_spec.
 |  
 |  __getnewargs__(self, *args, **kwargs)
 |      # print method
 |      #@functools.wraps(f)
 |  
 |  center(self, *args, **kwargs)
 |      S.center(width[, fillchar]) -> unicode
 |      
 |      Return S centered in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  count(self, *args, **kwargs)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      Unicode string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  endswith(self, *args, **kwargs)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  find(self, *args, **kwargs)
 |      S.find(sub [,start [,end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(self, *args, **kwargs)
 |      S.format(*args, **kwargs) -> unicode
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(self, *args, **kwargs)
 |      S.index(sub [,start [,end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
 |  
 |  isdecimal(self, *args, **kwargs)
 |      S.isdecimal() -> bool
 |      
 |      Return True if there are only decimal characters in S,
 |      False otherwise.
 |  
 |  islower(self, *args, **kwargs)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  isnumeric(self, *args, **kwargs)
 |      S.isnumeric() -> bool
 |      
 |      Return True if there are only numeric characters in S,
 |      False otherwise.
 |  
 |  isupper(self, *args, **kwargs)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  join(self, *args, **kwargs)
 |      S.join(iterable) -> unicode
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |  
 |  ljust(self, *args, **kwargs)
 |      S.ljust(width[, fillchar]) -> int
 |      
 |      Return S left-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  lower(self, *args, **kwargs)
 |      S.lower() -> unicode
 |      
 |      Return a copy of the string S converted to lowercase.
 |  
 |  lstrip(self, *args, **kwargs)
 |      S.lstrip([chars]) -> unicode
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is a str, it will be converted to unicode before stripping
 |  
 |  partition(self, *args, **kwargs)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
 |  replace(self, *args, **kwargs)
 |      S.replace(old, new[, count]) -> unicode
 |      
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |  
 |  rfind(self, *args, **kwargs)
 |      S.rfind(sub [,start [,end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(self, *args, **kwargs)
 |      S.rindex(sub [,start [,end]]) -> int
 |      
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |  
 |  rjust(self, *args, **kwargs)
 |      S.rjust(width[, fillchar]) -> unicode
 |      
 |      Return S right-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  rpartition(self, *args, **kwargs)
 |      S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
 |  
 |  rsplit(self, *args, **kwargs)
 |      S.rsplit([sep [,maxsplit]]) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string, starting at the end of the string and
 |      working to the front.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified, any whitespace string
 |      is a separator.
 |  
 |  rstrip(self, *args, **kwargs)
 |      S.rstrip([chars]) -> unicode
 |      
 |      Return a copy of the string S with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is a str, it will be converted to unicode before stripping
 |  
 |  split(self, *args, **kwargs)
 |      S.split([sep [,maxsplit]]) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are
 |      removed from the result.
 |  
 |  startswith(self, *args, **kwargs)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, *args, **kwargs)
 |      S.strip([chars]) -> unicode
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |      If chars is a str, it will be converted to unicode before stripping
 |  
 |  upper(self, *args, **kwargs)
 |      S.upper() -> unicode
 |      
 |      Return a copy of S converted to uppercase.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from pymel.util.utilitytypes.ProxyUnicode:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)