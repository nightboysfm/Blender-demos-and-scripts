import bpy
#look through every mesh's vertexgroups, and add their names to a list.
#Then, look through every bone in the armature of the meshes, and if their name isnt contained in the list, rename them to DELETEME_x (cause idk how to delete via script, lel ._.
#credits to metssfm, modifications by nightboy

#need the armature to be selected, which is the parent of each mesh.
vGroupList = []
myObject = bpy.context.object


for mesh in myObject.children:              #for each mesh
    for vGroup in mesh.vertex_groups:       #for each vertexgroup
        vGroupList.append(vGroup.name)
        
for bone in myObject.data.bones:            #for each bone
    if(bone.name not in vGroupList):
        bone.name = "DELETEME"



jpDict = {'root pelvis' : 'Pelvis',
    'pelvis' : 'ValveBiped.Bip01_Pelvis',
    'spine lower' : 'ValveBiped.Bip01_Spine',
    'spine middle' : 'ValveBiped.Bip01_Spine1',
    'spine midle' : 'ValveBiped.Bip01_Spine1',
    'spine upper' : 'ValveBiped.Bip01_Spine2',
    '乳１' : 'Breast',
    'head neck lower' : 'ValveBiped.Bip01_Neck',
    'head neck upper' : 'ValveBiped.Bip01_Head',
    '目' : 'Eyeball',
    'arm left shoulder 1' : 'ValveBiped.Bip01_L_Clavicle',
    'arm right shoulder 1' : 'ValveBiped.Bip01_R_Clavicle',
    'arm left shoulder' : 'ValveBiped.Bip01_L_Clavicle',
    'arm right shoulder' : 'ValveBiped.Bip01_R_Clavicle',
    'arm left shoulder 2' : 'ValveBiped.Bip01_L_UpperArm',
    'arm right shoulder 2' : 'ValveBiped.Bip01_R_UpperArm',
    'arm left arm' : 'ValveBiped.Bip01_L_UpperArm',
    'arm right arm' : 'ValveBiped.Bip01_R_UpperArm',
    'arm left elbow' : 'ValveBiped.Bip01_L_Forearm',
    'arm right elbow' : 'ValveBiped.Bip01_R_Forearm',
    'arm left wrist' : 'ValveBiped.Bip01_L_Hand',
    'arm right wrist' : 'ValveBiped.Bip01_R_Hand',
    'arm left finger 1a' : 'ValveBiped.Bip01_L_Finger0',
    'arm left finger 1b' : 'ValveBiped.Bip01_L_Finger01',
    'arm left finger 1c' : 'ValveBiped.Bip01_L_Finger02',
    'arm left finger 2a' : 'ValveBiped.Bip01_L_Finger1',
    'arm left finger 2b' : 'ValveBiped.Bip01_L_Finger11',
    'arm left finger 2c' : 'ValveBiped.Bip01_L_Finger12',
    'arm left finger 3a' : 'ValveBiped.Bip01_L_Finger2',
    'arm left finger 3b' : 'ValveBiped.Bip01_L_Finger21',
    'arm left finger 3c' : 'ValveBiped.Bip01_L_Finger22',
    'arm left finger 4a' : 'ValveBiped.Bip01_L_Finger3',
    'arm left finger 4b' : 'ValveBiped.Bip01_L_Finger31',
    'arm left finger 4c' : 'ValveBiped.Bip01_L_Finger32',
    'arm left finger 5a' : 'ValveBiped.Bip01_L_Finger4',
    'arm left finger 5b' : 'ValveBiped.Bip01_L_Finger41',
    'arm left finger 5c' : 'ValveBiped.Bip01_L_Finger42',
    'arm right finger 1a' : 'ValveBiped.Bip01_R_Finger0',
    'arm right finger 1b' : 'ValveBiped.Bip01_R_Finger01',
    'arm right finger 1c' : 'ValveBiped.Bip01_R_Finger02',
    'arm right finger 2a' : 'ValveBiped.Bip01_R_Finger1',
    'arm right finger 2b' : 'ValveBiped.Bip01_R_Finger11',
    'arm right finger 2c' : 'ValveBiped.Bip01_R_Finger12',
    'arm right finger 3a' : 'ValveBiped.Bip01_R_Finger2', 
    'arm right finger 3b' : 'ValveBiped.Bip01_R_Finger21',
    'arm right finger 3c' : 'ValveBiped.Bip01_R_Finger22',
    'arm right finger 4a' : 'ValveBiped.Bip01_R_Finger3', 
    'arm right finger 4b' : 'ValveBiped.Bip01_R_Finger31',
    'arm right finger 4c' : 'ValveBiped.Bip01_R_Finger32',
    'arm right finger 5a' : 'ValveBiped.Bip01_R_Finger4', 
    'arm right finger 5b' : 'ValveBiped.Bip01_R_Finger41',
    'arm right finger 5c' : 'ValveBiped.Bip01_R_Finger42',
    'leg left thigh' : 'ValveBiped.Bip01_L_Thigh',
    'leg right thigh' : 'ValveBiped.Bip01_R_Thigh',
    'leg left knee' : 'ValveBiped.Bip01_L_Calf',
    'leg right knee' : 'ValveBiped.Bip01_R_Calf',
    'leg left ankle' : 'ValveBiped.Bip01_L_Foot',
    'leg right ankle' : 'ValveBiped.Bip01_R_Foot',
    'leg left toes' : 'ValveBiped.Bip01_L_Toe0',
    'leg right toes' : 'ValveBiped.Bip01_R_Toe0',
    'leg left toe' : 'ValveBiped.Bip01_L_Toe0',
    'leg right toe' : 'ValveBiped.Bip01_R_Toe0'
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