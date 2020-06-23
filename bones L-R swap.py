import bpy, re

################################
# Toggle left/right bone names
# to make X-Axis mirroring
# possible
#
# Note: indentation tabs are not spaces
################################

def main():
	armature = bpy.context.object
	if not armature:
		print("No object selected.")
		return
	
	if armature.type != 'ARMATURE':
		print("Object is not an armature.")
		return
	
	# Renaming patterns
	patterns = {
		"source_to_blender": "ValveBiped\.Bip01_([LR])_(.*)",
		"blender_to_source": "ValveBiped\.Bip01_(.*)_([LR])"
	}
	
	# Default pattern
	pattern = 'blender_to_source'
	
	# Check for bones with Valve naming convention
	bones = armature.data.bones
	for bone in bones:
		var = re.search(patterns['source_to_blender'], bone.name)
		if var != None:
			pattern = 'source_to_blender'
			break
	
	total = 0
	renamed = 0
	not_renamed = []
	
	for bone in bones:
		total += 1
		match = re.search(patterns[pattern], bone.name)
		if match != None:
			renamed += 1
			
			# Swap name/side
			match_1 = match.group(1)
			match_2 = match.group(2)
			new_name = "ValveBiped.Bip01_"+match_2+"_"+match_1
			
			print(bone.name+" -> "+new_name)
			
			# Rename bone
			bone.name = new_name
		else:
			not_renamed.append(bone.name)
	
	print("===========================================")
	print(str(renamed)+"/"+str(total)+" bones renamed ("+pattern+")")
	print("-------------------------------------------")
	print("Not renamed:")
	
	for i in not_renamed:
		print(i)
		
main()