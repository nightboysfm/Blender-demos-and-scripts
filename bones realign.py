#Realignement des bones
import bpy, mathutils, fnmatch
#import bpy, math
#from mathutils import Vector, Matrix
#from math import radians

class ExitOK(Exception):
    pass


bpy.ops.object.mode_set(mode='EDIT')    
edit_bones = bpy.context.object.data.edit_bones
for bone in edit_bones:
    try:
        actualbone = bone.name
        print("!!!!!!!!!!!! 1a : Actualbone: " + bone.name)

        #Ici traitement manuel des bones sans enfants et avec plusieurs enfants
        #En premier car certains sont remplacer par l'alignement automatique sur l'enfant (Pelvis2+Pelvis1)
        if fnmatch.fnmatch(actualbone, 'ValveBiped.Bip01_?_Toe0') or "head" in actualbone:
            print("!!!!!!!!!!!! 1b : Extension pour: " + actualbone)
            if actualbone == "head eyelid right lower" or actualbone == "head eyelid left lower": #Exception eyelids
                vec = mathutils.Vector((0.0, -0.015, 0.025))
                edit_bones[actualbone].tail = edit_bones[actualbone].head + vec
            elif actualbone == "head eyelid right upper" or actualbone == "head eyelid left upper": #Exception eyelids
                vec = mathutils.Vector((0.0, 0.015, 0.025))
                edit_bones[actualbone].tail = edit_bones[actualbone].head + vec
            else: #Partie pour tout les autres
                vec = mathutils.Vector((0.0, 0.0, 0.025))
                #mat_trans = mathutils.Matrix.Translation(vec)
                edit_bones[actualbone].tail = edit_bones[actualbone].head + vec
        if actualbone == "ValveBiped.Bip01_Pelvis": #tail de ValveBiped.Bip01_Pelvis sur head de ValveBiped.Bip01_Spine
            edit_bones[actualbone].tail = edit_bones["ValveBiped.Bip01_Spine"].head
        if actualbone == "ValveBiped.Bip01_Spine2" or actualbone == "ValveBiped.Bip01_Spine1": #tail de ValveBiped.Bip01_Spine1 et ValveBiped.Bip01_Spine2 sur head de ValveBiped.Bip01_Neck
            edit_bones[actualbone].tail = edit_bones["ValveBiped.Bip01_Neck"].head
        if actualbone == "ValveBiped.Bip01_Head": #Dresser ValveBiped.Bip01_Head
            vec = mathutils.Vector((0.0, 0.05, 0.0))
            edit_bones[actualbone].tail = edit_bones[actualbone].head + vec
        if fnmatch.fnmatch(actualbone, 'ValveBiped.Bip01_?_Hand'): #Mains
            vec = mathutils.Vector((0.0, -0.010, 0.0))
            edit_bones[actualbone].tail = edit_bones[actualbone].head + vec            
        if fnmatch.fnmatch(actualbone, 'ValveBiped.Bip01_?_Finger*'): #Doigts
            vec = mathutils.Vector((0.0, -0.010, 0.0))
            edit_bones[actualbone].tail = edit_bones[actualbone].head + vec            

        #Exception bones sans parents (pelvis) (donc peux pas attacher le tail du parent)
        if not edit_bones[actualbone].parent:
            print("!!!!!!!!!!!! 2a : NO PARENT BONES !!!!!!!!!")

        #Traitement des bones avec parents (voie normale (tail -> head))
        elif edit_bones[actualbone].parent:
            print("!!!!!!!!!!!! 2b : PARENT BONES PRESENT !!!!!!!!!")
            parentbone = edit_bones[actualbone].parent
            print("!!!!!!!!!!!! 3b : Parentbone: " + edit_bones[actualbone].parent.name)
            avoidbones = {"ValveBiped.Bip01_Pelvis": 1, "head jaw": 2, "ValveBiped.Bip01_Spine2": 3, "ValveBiped.Bip01_Head": 4, "ValveBiped.Bip01_L_Hand": 5, "ValveBiped.Bip01_R_Hand": 6}
            #Exception des bones avec plusieurs enfants (car attache son tail au head des enfants)
            if parentbone.name in avoidbones:
                print("!!!!!!!!!!!! 4b : Multiple child bones detected")       
            else:
                print("!!!!!!!!!!!! 4b : No multiple child bones detected")
                parentbone.tail = edit_bones[actualbone].head

        print("!!!!!!!!!!!! 5 : End")
    except ExitOK:
        print("OK")
    bpy.context.scene.update()
bpy.ops.object.mode_set(mode='OBJECT')