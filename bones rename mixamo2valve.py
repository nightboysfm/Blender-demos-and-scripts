# Purpose: select an armature on a human model imported form Bio3
# run this script, all bones renamed to their TF2 counterparts
# Added Bones conversion for Blender 2.49 animation naming conventions (01/20/14)
# added EndBone For direct 2.68 Import (01/20/14)

names = dict()
 
# Purpose: select an armature from a Bio3 model
# run this
# Get a TF2 style armature
 
names['mixamorig_Hips'] = 'bip_pelvis'
names['mixamorig_Spine'] = 'bip_spine_0'
names['mixamorig_Spine1'] = 'bip_spine_1'
names['mixamorig_Spine2'] = 'bip_spine_2'
names['mixamorig_Neck'] = 'bip_neck'
names['mixamorig_Head'] = 'bip_head'
names['mixamorig_HeadTop_End'] = 'bip_headEnd'
 
names['mixamorig_RightShoulder'] = 'bip_collar_R'
names['mixamorig_RightSh62c1'] = 'bip_collar_R'
names['mixamorig_LeftShoulder'] = 'bip_collar_L'
names['mixamorig_LeftSho8455'] = 'bip_collar_L'
 
names['mixamorig_RightArm'] = 'bip_upperArm_R'
names['mixamorig_RightForeArm'] = 'bip_lowerArm_R'
names['mixamorig_RightFo14b5'] = 'bip_lowerArm_R'
names['mixamorig_RightHand'] = 'bip_hand_R'
# names['mixamorig_RUpperarm2'] = 'hlp_upperArm_R'
# names['mixamorig_RForearm2'] = 'hlp_lowerArm_R'
 
names['mixamorig_RightHandThumb1'] = 'bip_thumb_0_R'
names['mixamorig_RightHandThumb2'] = 'bip_thumb_1_R'
names['mixamorig_RightHandThumb3'] = 'bip_thumb_2_R'
names['mixamorig_RightHandThumb4'] = 'bip_thumbEnd_R'

names['mixamorig_RightHaf29d'] = 'bip_thumb_0_R'
names['mixamorig_RightHa39d7'] = 'bip_thumb_1_R'
names['mixamorig_RightHa1dd4'] = 'bip_thumb_2_R'
names['mixamorig_RightHacae3'] = 'bip_thumbEnd_R'

 
names['mixamorig_RightHandIndex1'] = 'bip_index_0_R'
names['mixamorig_RightHandIndex2'] = 'bip_index_1_R'
names['mixamorig_RightHandIndex3'] = 'bip_index_2_R'
names['mixamorig_RightHandIndex4'] = 'bip_indexEnd_R'
 
names['mixamorig_RightHaec4e'] = 'bip_index_0_R'
names['mixamorig_RightHa69c1'] = 'bip_index_1_R'
names['mixamorig_RightHa8f63'] = 'bip_index_2_R'
names['mixamorig_RightHa8da5'] = 'bip_indexEnd_R'

names['mixamorig_RightHandMiddle1'] = 'bip_middle_0_R'
names['mixamorig_RightHandMiddle2'] = 'bip_middle_1_R'
names['mixamorig_RightHandMiddle3'] = 'bip_middle_2_R'
names['mixamorig_RightHandMiddle4'] = 'bip_middleEnd_R'

names['mixamorig_RightHa762d'] = 'bip_middle_0_R'
names['mixamorig_RightHa64bd'] = 'bip_middle_1_R'
names['mixamorig_RightHa3b66'] = 'bip_middle_2_R'
names['mixamorig_RightHa4320'] = 'bip_middleEnd_R'
 
names['mixamorig_RightHandRing1'] = 'bip_ring_0_R'
names['mixamorig_RightHandRing2'] = 'bip_ring_1_R'
names['mixamorig_RightHandRing3'] = 'bip_ring_2_R'
names['mixamorig_RightHandRing4'] = 'bip_ringEnd_R'

names['mixamorig_RightHa3817'] = 'bip_ring_0_R'
names['mixamorig_RightHacc1d'] = 'bip_ring_1_R'
names['mixamorig_RightHa4665'] = 'bip_ring_2_R'
names['mixamorig_RightHaf065'] = 'bip_ringEnd_R'
 
names['mixamorig_RightHandPinky1'] = 'bip_pinky_0_R'
names['mixamorig_RightHandPinky2'] = 'bip_pinky_1_R'
names['mixamorig_RightHandPinky3'] = 'bip_pinky_2_R'
names['mixamorig_RightHandPinky4'] = 'bip_pinkyEnd_R'

names['mixamorig_RightHad21e'] = 'bip_pinky_0_R'
names['mixamorig_RightHa98f3'] = 'bip_pinky_1_R'
names['mixamorig_RightHaffa8'] = 'bip_pinky_2_R'
names['mixamorig_RightHaebd1'] = 'bip_pinkyEnd_R'
 
names['mixamorig_RightUpLeg'] = 'bip_hip_R'
names['mixamorig_RightLeg'] = 'bip_knee_R'
names['mixamorig_RightFoot'] = 'bip_foot_R'
names['mixamorig_RightToeBase'] = 'bip_toe_R'
names['mixamorig_RightToe_End'] = 'bip_toeEnd_R'
names['mixamorig_RightTo3938'] = 'bip_toe_R'
names['mixamorig_RightTo1dd9'] = 'bip_toeEnd_R'
 
names['mixamorig_LeftArm'] = 'bip_upperArm_L'
names['mixamorig_LeftForeArm'] = 'bip_lowerArm_L'
names['mixamorig_LeftHand'] = 'bip_hand_L'
# names['mixamorig_LUpperarm2'] = 'hlp_upperArm_L'
# names['mixamorig_LForearm2'] = 'hlp_lowerArm_L'

names['mixamorig_LeftHandThumb1'] = 'bip_thumb_0_L'
names['mixamorig_LeftHandThumb2'] = 'bip_thumb_1_L'
names['mixamorig_LeftHandThumb3'] = 'bip_thumb_2_L'
names['mixamorig_LeftHandThumb4'] = 'bip_thumbEnd_L'

names['mixamorig_LeftHand05e'] = 'bip_thumb_0_L'
names['mixamorig_LeftHanf7ef'] = 'bip_thumb_1_L'
names['mixamorig_LeftHanb161'] = 'bip_thumb_2_L'
names['mixamorig_LeftHan6dce'] = 'bip_thumbEnd_L'
 
names['mixamorig_LeftHandIndex1'] = 'bip_index_0_L'
names['mixamorig_LeftHandIndex2'] = 'bip_index_1_L'
names['mixamorig_LeftHandIndex3'] = 'bip_index_2_L'
names['mixamorig_LeftHandIndex4'] = 'bip_indexEnd_L'

names['mixamorig_LeftHaneab'] = 'bip_index_0_L'
names['mixamorig_LeftHane9d7'] = 'bip_index_1_L'
names['mixamorig_LeftHan178d'] = 'bip_index_2_L'
names['mixamorig_LeftHan965f'] = 'bip_indexEnd_L'
 
names['mixamorig_LeftHandMiddle1'] = 'bip_middle_0_L'
names['mixamorig_LeftHandMiddle2'] = 'bip_middle_1_L'
names['mixamorig_LeftHandMiddle3'] = 'bip_middle_2_L'
names['mixamorig_LeftHandMiddle4'] = 'bip_middleEnd_L'

names['mixamorig_LeftHan60b9'] = 'bip_middle_0_L'
names['mixamorig_LeftHandd5'] = 'bip_middle_1_L'
names['mixamorig_LeftHanf272'] = 'bip_middle_2_L'
names['mixamorig_LeftHan366b'] = 'bip_middleEnd_L'
 
names['mixamorig_LeftHandRing1'] = 'bip_ring_0_L'
names['mixamorig_LeftHandRing2'] = 'bip_ring_1_L'
names['mixamorig_LeftHandRing3'] = 'bip_ring_2_L'
names['mixamorig_LeftHandRing4'] = 'bip_ringEnd_L'

names['mixamorig_LeftHanfcc5'] = 'bip_ring_0_L'
names['mixamorig_LeftHan4466'] = 'bip_ring_1_L'
names['mixamorig_LeftHan6f61'] = 'bip_ring_2_L'
names['mixamorig_LeftHane2ff'] = 'bip_ringEnd_L'
 
names['mixamorig_LeftHandPinky1'] = 'bip_pinky_0_L'
names['mixamorig_LeftHandPinky2'] = 'bip_pinky_1_L'
names['mixamorig_LeftHandPinky3'] = 'bip_pinky_2_L'
names['mixamorig_LeftHandPinky4'] = 'bip_pinkyEnd_L'

names['mixamorig_LeftHandb88'] = 'bip_pinky_0_L'
names['mixamorig_LeftHan4add'] = 'bip_pinky_1_L'
names['mixamorig_LeftHance6a'] = 'bip_pinky_2_L'
names['mixamorig_LeftHan9dbe'] = 'bip_pinkyEnd_L'
 
names['mixamorig_LeftUpLeg'] = 'bip_hip_L'
names['mixamorig_LeftLeg'] = 'bip_knee_L'
names['mixamorig_LeftFoot'] = 'bip_foot_L'
names['mixamorig_LeftToeBase'] = 'bip_toe_L'
names['mixamorig_LeftToe_End'] = 'bip_toeEnd_L'

names['R_Grip'] = 'weapon_bone'
names['L_Grip'] = 'weapon_bone_L'

import bpy

bones = bpy.context.selected_objects[0].data.bones

if (bones):
    for bone in bones:
        newName = names.get(bone.name)
        if (newName):
            bone.name = newName