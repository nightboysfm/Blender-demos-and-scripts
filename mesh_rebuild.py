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
# Locate the target armature and mesh for export
# RETURNS armature, mesh
#===========================================================================
#meshes = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']
#for obj in meshes:
#    #print(dir(obj))
#    if obj.type == 'MESH':
#        bexportmesh = False
#        #print("PARENT MESH:",obj.name)
#        for udkmeshlist in bpy.context.scene.udkmesh_list:
#            if obj.name == udkmeshlist.name and udkmeshlist.bexport == True:
#                bexportmesh = True
#                break
#            if bexportmesh == True:
#                print("Mesh Name:",obj.name," < SELECT TO EXPORT!")
#                meshselected.append(obj)
#                print("MESH COUNT:",len(meshselected))

#    #this will check if object need to be rebuild.
#    if bpy.context.scene.udk_option_rebuildobjects:
#        #print("INIT... REBUILDING...")
#        print("REBUILDING ARMATURE...")
#        #if deform mesh
#        armature =  rebuildarmature(armature) #rebuild the armature to raw . If there IK constraint it will ignore it.
#        print("REBUILDING MESH...")
#        mesh = rebuildmesh(mesh) #rebuild the mesh to raw data format.
#    return armature, mesh


#===========================================================================
# User interface
#===========================================================================
def unpack_list(list_of_tuples):
    l = []
    for t in list_of_tuples:
        l.extend(t)
    return l

def rebuildmesh(obj):
    #make sure it in object mode
    print("Mesh Object Name:",obj.name)
    bpy.ops.object.mode_set(mode='OBJECT')
    for i in bpy.context.scene.objects: i.select = False #deselect all objects
    obj.select = True
    bpy.context.scene.objects.active = obj

    me_ob = bpy.data.meshes.new((obj.name+"_REBUILD"))
    mesh = obj.data
    faces = []
    verts = []
    smoothings = []
    uvfaces = []
    #print("creating array build mesh...")
    mmesh = obj.to_mesh(bpy.context.scene,True,'PREVIEW')
    uv_layer = mmesh.tessface_uv_textures.active
    for face in mmesh.tessfaces:
        smoothings.append(face.use_smooth)#smooth or flat in boolean
        if uv_layer != None:#check if there texture data exist
            faceUV = uv_layer.data[face.index]
            uvs = []
            for uv in faceUV.uv:
                uvs.append((uv[0],uv[1]))
            uvfaces.append(uvs)
        #print((face.vertices[:]))
        if len(face.vertices) == 3:
            faces.extend([(face.vertices[0],face.vertices[1],face.vertices[2],0)])
        else:
            faces.extend([(face.vertices[0],face.vertices[1],face.vertices[2],face.vertices[3])])
    #vertex positions
    for vertex in mesh.vertices:
        verts.append(vertex.co.to_tuple())
    #vertices weight groups into array
    vertGroups = {} #array in strings
    for vgroup in obj.vertex_groups:
        vlist = []
        for v in mesh.vertices:
            for vg in v.groups:
                if vg.group == vgroup.index:
                    vlist.append((v.index,vg.weight))
                    #print((v.index,vg.weight))
        vertGroups[vgroup.name] = vlist

    #print("creating mesh object...")
    #me_ob.from_pydata(verts, [], faces)
    me_ob.vertices.add(len(verts))
    me_ob.tessfaces.add(len(faces))
    me_ob.vertices.foreach_set("co", unpack_list(verts))
    me_ob.tessfaces.foreach_set("vertices_raw",unpack_list( faces))
    me_ob.tessfaces.foreach_set("use_smooth", smoothings)#smooth array from face

    #check if there is uv faces
    if len(uvfaces) > 0:
        uvtex = me_ob.tessface_uv_textures.new(name="retex")
        for i, face in enumerate(me_ob.tessfaces):
            blender_tface = uvtex.data[i] #face
            mfaceuv = uvfaces[i]
            if len(mfaceuv) == 3:
                blender_tface.uv1 = mfaceuv[0];
                blender_tface.uv2 = mfaceuv[1];
                blender_tface.uv3 = mfaceuv[2];
            if len(mfaceuv) == 4:
                blender_tface.uv1 = mfaceuv[0];
                blender_tface.uv2 = mfaceuv[1];
                blender_tface.uv3 = mfaceuv[2];
                blender_tface.uv4 = mfaceuv[3];

    me_ob.update()#need to update the information to able to see into the secne
    obmesh = bpy.data.objects.new((obj.name+"_REBUILD"),me_ob)
    bpy.context.scene.update()
    #Build tmp materials
    materialname = "ReMaterial"
    for matcount in mesh.materials:
        matdata = bpy.data.materials.new(materialname)
        me_ob.materials.append(matdata)
    #assign face to material id
    for face in mesh.tessfaces:
        me_ob.faces[face.index].material_index = face.material_index
    #vertices weight groups
    for vgroup in vertGroups:
        group = obmesh.vertex_groups.new(vgroup)
        for v in vertGroups[vgroup]:
            group.add([v[0]], v[1], 'ADD')# group.add(array[vertex id],weight,add)
    bpy.context.scene.objects.link(obmesh)
    #print("Mesh Material Count:",len(me_ob.materials))
    matcount = 0
    #print("MATERIAL ID OREDER:")
    for mat in me_ob.materials:
        #print("-Material:",mat.name,"INDEX:",matcount)
        matcount += 1
    print("Mesh Object Name:",obmesh.name)
    bpy.context.scene.update()
    return obmesh


#class OBJECT_OT_UTRebuildMesh(bpy.types.Operator):
#    """It rebuild the mesh from scrape from the selected mesh object. """ \
#    """Note the scale will be 1:1 for object mode. To keep from deforming"""
#    bl_idname = "object.utrebuildmesh"  # XXX, name???
#    bl_label = "Rebuild Mesh"#"Rebuild Mesh"
#
#    def invoke(self, context, event):
#        print("----------------------------------------")
#        print("Init Mesh Bebuild...")
#        bselected = False
#        bpy.ops.object.mode_set(mode='OBJECT')
#        for obj in bpy.data.objects:
#            if obj.type == 'MESH' and obj.select == True:
#                rebuildmesh(obj)
#        self.report({'INFO'}, "Rebuild Mesh Finish!")
#        print("Finish Mesh Build...")
#        print("----------------------------------------")
#       return{'FINISHED'}
 
    
        
obj = bpy.context.active_object
if obj.type == 'MESH': 
    rebuildmesh(obj)