#import bmesh
#import os
#import time
import bpy
#import mathutils
#import math
#import random
#import operator
#import sys
#from bpy.props import *
#from struct import pack

#===========================================================================
# Custom exception class
#===========================================================================
class Error( Exception ):

    def __init__(self, message):
        self.message = message


#===========================================================================
# Generic Object->Integer mapping
# the object must be usable as a dictionary key
#===========================================================================
#class ObjMap:
#
#    def __init__(self):
#        self.dict = {}
#        self.next = 0
#
#    def get(self, obj):
#        if obj in self.dict:
#            return self.dict[obj]
#        else:
#            id = self.next
#            self.next = self.next + 1
#            self.dict[obj] = id
#            return id
#
#    def items(self):
#        getval = operator.itemgetter(0)
#        getkey = operator.itemgetter(1)
#        return map(getval, sorted(self.dict.items(), key=getkey))


#===========================================================================
# User interface
#===========================================================================
#def unpack_list(list_of_tuples):
#    l = []
#    for t in list_of_tuples:
#        l.extend(t)
#    return l


def rebuildarmature(obj):
    currentbone = [] #select armature for roll copy
    print("Armature Name:",obj.name)
    #objectname = "ArmatureDataPSK"
    #meshname ="ArmatureObjectPSK"
    objectname = (obj.name+"_ARM_REBUILD")
    meshname = (obj.name+"_OBJ_REBUILD")
    armdata = bpy.data.armatures.new(objectname)
    ob_new = bpy.data.objects.new(meshname, armdata)
    bpy.context.scene.objects.link(ob_new)
    #bpy.ops.object.mode_set(mode='OBJECT')
    for i in bpy.context.scene.objects: i.select = False #deselect all objects
    ob_new.select = True
    bpy.context.scene.objects.active = obj

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in obj.data.edit_bones:
        if bone.parent != None:
            currentbone.append([bone.name,bone.roll])
        else:
            currentbone.append([bone.name,bone.roll])
    bpy.ops.object.mode_set(mode='OBJECT')
    for i in bpy.context.scene.objects: i.select = False #deselect all objects
    bpy.context.scene.objects.active = ob_new
    bpy.ops.object.mode_set(mode='EDIT')

    for bone in obj.data.bones:
        bpy.ops.object.mode_set(mode='EDIT')
        newbone = ob_new.data.edit_bones.new(bone.name)
        newbone.head = bone.head_local
        newbone.tail = bone.tail_local
        for bonelist in currentbone:
            if bone.name == bonelist[0]:
                newbone.roll = bonelist[1]
                break
        if bone.parent != None:
            parentbone = ob_new.data.edit_bones[bone.parent.name]
            newbone.parent = parentbone

    ob_new.animation_data_create()#create animation data
    if obj.animation_data != None:#check for animation
        ob_new.animation_data.action  = obj.animation_data.action  #just make sure it here to do the animations if exist
    print("Armature Object Name:",ob_new.name)
    return ob_new


#class OBJECT_OT_UTRebuildArmature(bpy.types.Operator):
#    """If mesh is deform when importing to unreal engine try this. """ \
#    """It rebuild the bones one at the time by select one armature object scrape to raw setup build. """ \
#    """Note the scale will be 1:1 for object mode. To keep from deforming"""
#    bl_idname = "object.utrebuildarmature"  # XXX, name???
#    bl_label = "Rebuild Armature" #Rebuild Armature
#
#    def invoke(self, context, event):
#        print("----------------------------------------")
#        print("Init Rebuild Armature...")
#        bselected = False
#        for obj in bpy.data.objects:
#            if obj.type == 'ARMATURE' and obj.select == True:
#                rebuildarmature(obj)
#        self.report({'INFO'}, "Rebuild Armature Finish!")
#        print("End of Rebuild Armature.")
#        print("----------------------------------------")
#        return{'FINISHED'}


obj = bpy.context.active_object
if obj.type == 'ARMATURE': 
    rebuildarmature(obj)