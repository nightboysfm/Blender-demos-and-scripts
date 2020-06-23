import bpy
#look through every mesh's vertexgroups, and add their names to a list.
#Then, look through every bone in the armature of the meshes, and if their name isnt contained in the list, rename them to DELETEME_x (cause idk how to delete via script, lel ._.
#credits to metssfm, modifications by nightboy

#need the armature to be selected, which is the parent of each mesh.
bpy.ops.object.mode_set(mode='POSE')
vGroupList = []
myObject = bpy.context.object
myObject.show_x_ray = True #Affichage xray
myObject.data.draw_type = 'STICK' #Affichage en stick


#Marque bones vides comme "DELETEME"
for mesh in myObject.children:              #for each mesh
    for vGroup in mesh.vertex_groups:       #for each vertexgroup
        vGroupList.append(vGroup.name)
for bone in myObject.data.bones:            #for each bone
    if(bone.name not in vGroupList):
        bone.name = "DELETEME"


#Reset pose transforms
for bone in bpy.context.object.data.bones:
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.pose.loc_clear()
    bpy.ops.pose.rot_clear()
#    bpy.ops.pose.scale_clear()
#    bpy.ops.pose.transforms_clear()
    bpy.ops.pose.select_all(action='DESELECT')        
        

#Reset objects transforms
meshes=[item for item in bpy.data.objects if item.type=="MESH"]
for item in meshes:
    item.select=True
    bpy.ops.object.location_clear()
#    bpy.ops.object.rotation_clear() #Parfois desactiver pour conserver rotation de l'importation
#    bpy.ops.object.origin_clear()
#    bpy.ops.object.scale_clear() #Conserver scale import
    item.select=False
bpy.ops.object.select_all(action='DESELECT')
        
        
#Rename bones
jpDict = {'root pelvis' : 'Pelvis',
    'BoneEyeRight' : 'head eyeball right',
    'BoneEyeLeft' : 'head eyeball left',
    'BoneEyelidLowerLeft' : 'head eyelid left lower',
    'BoneEyelidUpperLeft' : 'head eyelid left upper',
    'BoneEyelidLowerRight' : 'head eyelid right lower',
    'BoneEyelidUpperRight' : 'head eyelid right upper',
    'BoneEarLeft01' : 'head ear left 1',
    'BoneEarLeft02' : 'head ear left 2',
    'BoneEarLeft03' : 'head ear left 3',
    'BoneEarRight01' : 'head ear right 1',
    'BoneEarRight02' : 'head ear right 2',
    'BoneEarRight03' : 'head ear right 3',
    'BoneJaw' : 'head jaw',
    'BoneCheekLowerLeft' : 'head cheek left lower',
    'BoneCheekLowerRight' : 'head cheek right lower',
    'BoneCheekUpperLeft' : 'head cheek left upper',
    'BoneCheekUpperRight' : 'head cheek right upper',
    'BoneMouthLipLowerLeft' : 'head lip lower left',
    'BoneMouthLipLowerMid' : 'head lip lower middle',
    'BoneMouthLipLowerRight' : 'head lip lower right',
    'BoneMouthLipUpperLeft' : 'head lip upper left',
    'BoneMouthLipUpperMid' : 'head lip upper middle',
    'BoneMouthLipUpperRight' : 'head lip upper right',
    'BoneMouthCornerLeft' : 'head mouth corner left',
    'BoneMouthCornerRight' : 'head mouth corner right',
    'BoneNoseRight' : 'head nostril right 1',
    'BoneNoseLeft' : 'head nostril left 1',
    'BoneNoseFurrowRight' : 'head nostril right 2',
    'BoneNoseFurrowLeft' : 'head nostril left 2',
    'BoneMouthUpperMid' : 'head nostril center',
    'BoneBrowLeftInner' : 'head eyebrow left 1',
    'BoneBrowLeftMid' : 'head eyebrow left 2',
    'BoneBrowLeftOuter' : 'head eyebrow left 3',
    'BoneBrowRightInner' : 'head eyebrow right 1',
    'BoneBrowRightMid' : 'head eyebrow right 2',
    'BoneBrowRightOuter' : 'head eyebrow right 3',
    'BoneHip' : 'ValveBiped.Bip01_Pelvis',
    'BoneStomach' : 'ValveBiped.Bip01_Spine',
    'NO-USE BoneChest' : 'ValveBiped.Bip01_Spine1',
    'NO-USE spine midle' : 'ValveBiped.Bip01_Spine1',
    'BoneChest' : 'ValveBiped.Bip01_Spine1',
    'BoneChest2' : 'ValveBiped.Bip01_Spine2',
    'BoneNeck' : 'ValveBiped.Bip01_Neck',
    'BoneHead' : 'ValveBiped.Bip01_Head',
    'BoneShoulderLeft' : 'ValveBiped.Bip01_L_Clavicle',
    'BoneShoulderRight' : 'ValveBiped.Bip01_R_Clavicle',
    'BoneArmUpperLeft' : 'ValveBiped.Bip01_L_UpperArm',
    'BoneArmUpperRight' : 'ValveBiped.Bip01_R_UpperArm',
    'BoneArmLowerLeft' : 'ValveBiped.Bip01_L_Forearm',
    'BoneArmLowerRight' : 'ValveBiped.Bip01_R_Forearm',
    'BoneHandLeft' : 'ValveBiped.Bip01_L_Hand',
    'BoneHandRight' : 'ValveBiped.Bip01_R_Hand',
    'BoneFingerThumb1Left' : 'ValveBiped.Bip01_L_Finger0',
    'BoneFingerThumb2Left' : 'ValveBiped.Bip01_L_Finger01',
    'BoneFingerThumb3Left' : 'ValveBiped.Bip01_L_Finger02',
    'BoneFingerIndex1Left' : 'ValveBiped.Bip01_L_Finger1',
    'BoneFingerIndex2Left' : 'ValveBiped.Bip01_L_Finger11',
    'BoneFingerIndex3Left' : 'ValveBiped.Bip01_L_Finger12',
    'BoneFingerMiddle1Left' : 'ValveBiped.Bip01_L_Finger2',
    'BoneFingerMiddle2Left' : 'ValveBiped.Bip01_L_Finger21',
    'BoneFingerMiddle3Left' : 'ValveBiped.Bip01_L_Finger22',
    'BoneFingerRing1Left' : 'ValveBiped.Bip01_L_Finger3',
    'BoneFingerRing2Left' : 'ValveBiped.Bip01_L_Finger31',
    'BoneFingerRing3Left' : 'ValveBiped.Bip01_L_Finger32',
    'BoneFingerLittle1Left' : 'ValveBiped.Bip01_L_Finger4',
    'BoneFingerLittle2Left' : 'ValveBiped.Bip01_L_Finger41',
    'BoneFingerLittle3Left' : 'ValveBiped.Bip01_L_Finger42',
    'BoneFingerThumb1Right' : 'ValveBiped.Bip01_R_Finger0',
    'BoneFingerThumb2Right' : 'ValveBiped.Bip01_R_Finger01',
    'BoneFingerThumb3Right' : 'ValveBiped.Bip01_R_Finger02',
    'BoneFingerIndex1Right' : 'ValveBiped.Bip01_R_Finger1',
    'BoneFingerIndex2Right' : 'ValveBiped.Bip01_R_Finger11',
    'BoneFingerIndex3Right' : 'ValveBiped.Bip01_R_Finger12',
    'BoneFingerMiddle1Right' : 'ValveBiped.Bip01_R_Finger2', 
    'BoneFingerMiddle2Right' : 'ValveBiped.Bip01_R_Finger21',
    'BoneFingerMiddle3Right' : 'ValveBiped.Bip01_R_Finger22',
    'BoneFingerRing1Right' : 'ValveBiped.Bip01_R_Finger3', 
    'BoneFingerRing2Right' : 'ValveBiped.Bip01_R_Finger31',
    'BoneFingerRing3Right' : 'ValveBiped.Bip01_R_Finger32',
    'BoneFingerLittle1Right' : 'ValveBiped.Bip01_R_Finger4', 
    'BoneFingerLittle2Right' : 'ValveBiped.Bip01_R_Finger41',
    'BoneFingerLittle3Right' : 'ValveBiped.Bip01_R_Finger42',
    'BoneLegUpperLeft' : 'ValveBiped.Bip01_L_Thigh',
    'BoneLegUpperRight' : 'ValveBiped.Bip01_R_Thigh',
    'BoneLegLowerLeft' : 'ValveBiped.Bip01_L_Calf',
    'BoneLegLowerRight' : 'ValveBiped.Bip01_R_Calf',
    'BoneFootLeft' : 'ValveBiped.Bip01_L_Foot',
    'BoneFootRight' : 'ValveBiped.Bip01_R_Foot',
    'BoneToeLeft' : 'ValveBiped.Bip01_L_Toe0',
    'BoneToeRight' : 'ValveBiped.Bip01_R_Toe0',
    }     

for bone in myObject.data.bones:
    try: 
        if bone.name.find('.') != -1:
            #if bone ends with .r or .l (or contains a useless period, in which case this will fuck up.)
            separated = bone.name.split('.')
            bone.name = "%s.%s" % (jpDict.get(separated[0], separated[0]), separated[1])
            continue
            
        bone.name = jpDict.get(bone.name)
    except TypeError:
        #print("Not found in Bones dict: %s" % bone.name)
        continue

