def offsetKeyUI(* args):
	offset = cmds.floatFieldGrp("offset", q=True, v1=True)

	anim_curves = cmds.ls(type=['animCurveTA', 'animCurveTL', 'animCurveTT', 'animCurveTU'])  

	for each in anim_curves:  
		cmds.keyframe(each, edit=True, relative=True, timeChange=offset)