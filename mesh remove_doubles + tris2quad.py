#Remove doubles and convert tris to quads
import bpy

objselect = bpy.context.scene.objects
remove_limit = 0.0001

for ob in objselect:
    if ob.type == 'MESH':
        bpy.context.scene.objects.active = ob #set active object
        bpy.ops.object.mode_set(mode='EDIT') #switch to edit mode
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles(threshold=remove_limit) #remove doubles
        
        bpy.ops.mesh.tris_convert_to_quads() #tris to quads
        bpy.ops.object.mode_set(mode='OBJECT') #switch to object mode
