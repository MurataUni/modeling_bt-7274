import sys
sys.dont_write_bytecode = True

import numpy as np
import os

from harbor3d.specification import Spec
from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo

class Const:

    bone_default_len = 1.
    bone_default_len_small = 0.1

    bones_relationship = {
        "base": None,
        "body_lower": "base", # parts body lower
        "body_lower_panel_front_l": "body_lower",
        "body_lower_panel_front_r": "body_lower",
        "body_lower_panel_back_l": "body_lower",
        "body_lower_panel_back_r": "body_lower",
        "body_cylinder_front_l": "body_lower",
        "body_cylinder_front_r": "body_lower",
        "body_cylinder_side_front_l": "body_lower",
        "body_cylinder_side_front_r": "body_lower",
        "body_cylinder_side_back_l": "body_lower",
        "body_cylinder_side_back_r": "body_lower",
        "body_spine_lower": "body_lower",
        "body_spine_internal_1": "body_spine_lower",
        "body_spine_internal_2": "body_spine_internal_1",
        "body_spine_upper": "body_spine_internal_2",
        "body_upper": "body_spine_upper", # parts body upper
        "camera_front_beam": "body_upper",
        "camera_front": "camera_front_beam",
        "camera_shoulder": "body_upper",
        "shoulder_launcher_beam_root_l": "body_upper",
        "shoulder_launcher_beam_internal_l": "shoulder_launcher_beam_root_l",
        "shoulder_launcher_beam_end_l": "shoulder_launcher_beam_internal_l",
        "shoulder_missile_launcher_base_l": "shoulder_launcher_beam_end_l",
        "shoulder_missile_launcher_l": "shoulder_missile_launcher_base_l",
        "shoulder_launcher_beam_root_r": "body_upper",
        "shoulder_launcher_beam_internal_r": "shoulder_launcher_beam_root_r",
        "shoulder_launcher_beam_end_r": "shoulder_launcher_beam_internal_r",
        "shoulder_missile_launcher_base_r": "shoulder_launcher_beam_end_r",
        "shoulder_missile_launcher_r": "shoulder_missile_launcher_base_r",
        "shoulder_l": "body_upper", # parts arm left
        "upper_arm_l": "shoulder_l",
        "forearm_l": "upper_arm_l",
        "palm_l": "forearm_l",
        "shoulder_r": "body_upper", # parts arm right
        "upper_arm_r": "shoulder_r",
        "forearm_r": "upper_arm_r",
        "palm_r": "forearm_r",
        "thigh_l": "body_lower", # parts leg left
        "shin_l": "thigh_l",
        "metatarsal_l": "shin_l",
        "foot_l": "metatarsal_l",
        "thigh_r": "body_lower", # parts leg right
        "shin_r": "thigh_r",
        "metatarsal_r": "shin_r",
        "foot_r": "metatarsal_r",
        "thumb_proximal_phalanx_l": "palm_l", # parts hand left
        "thumb_distal_phalanx_l": "thumb_proximal_phalanx_l",
        "first_f_proximal_phalanx_l": "palm_l",
        "first_f_middle_phalanx_l": "first_f_proximal_phalanx_l",
        "first_f_distal_phalanx_l": "first_f_middle_phalanx_l",
        "second_f_proximal_phalanx_l": "palm_l",
        "second_f_middle_phalanx_l": "second_f_proximal_phalanx_l",
        "second_f_distal_phalanx_l": "second_f_middle_phalanx_l",
        "third_f_proximal_phalanx_l": "palm_l",
        "third_f_middle_phalanx_l": "third_f_proximal_phalanx_l",
        "third_f_distal_phalanx_l": "third_f_middle_phalanx_l",
        "hand_padding_l": "palm_l",
        "thumb_proximal_phalanx_r": "palm_r", # parts hand right
        "thumb_distal_phalanx_r": "thumb_proximal_phalanx_r",
        "first_f_proximal_phalanx_r": "palm_r",
        "first_f_middle_phalanx_r": "first_f_proximal_phalanx_r",
        "first_f_distal_phalanx_r": "first_f_middle_phalanx_r",
        "second_f_proximal_phalanx_r": "palm_r",
        "second_f_middle_phalanx_r": "second_f_proximal_phalanx_r",
        "second_f_distal_phalanx_r": "second_f_middle_phalanx_r",
        "third_f_proximal_phalanx_r": "palm_r",
        "third_f_middle_phalanx_r": "third_f_proximal_phalanx_r",
        "third_f_distal_phalanx_r": "third_f_middle_phalanx_r",
        "weapon_r": "palm_r", # parts weapon right
    }

    bones = bones_relationship.keys()

    alias = {
        "body_cylinder_front_l": "body_cylinder", # parts body lower
        "body_cylinder_front_r": "body_cylinder",
        "body_cylinder_side_front_l": "body_cylinder",
        "body_cylinder_side_front_r": "body_cylinder",
        "body_cylinder_side_back_l": "body_cylinder",
        "body_cylinder_side_back_r": "body_cylinder",
        "body_spine_internal_1": "body_spine_internal",
        "body_spine_internal_2": "body_spine_internal",
        "shoulder_launcher_beam_internal_l": "shoulder_launcher_beam_internal", # parts body upper
        "shoulder_launcher_beam_end_l": "shoulder_launcher_beam_end",
        "shoulder_missile_launcher_l": "shoulder_missile_launcher",
        "shoulder_missile_launcher_base_l": "shoulder_missile_launcher_base",
        "shoulder_launcher_beam_internal_r": "shoulder_launcher_beam_internal",
        "shoulder_launcher_beam_end_r": "shoulder_launcher_beam_end",
        "shoulder_missile_launcher_r": "shoulder_missile_launcher",
        "shoulder_missile_launcher_base_r": "shoulder_missile_launcher_base",
        "thumb_proximal_phalanx_l": "thumb_proximal_phalanx", # parts hand left
        "thumb_distal_phalanx_l": "thumb_distal_phalanx",
        "first_f_proximal_phalanx_l": "f_proximal_phalanx",
        "first_f_middle_phalanx_l": "f_middle_phalanx",
        "first_f_distal_phalanx_l": "f_distal_phalanx",
        "second_f_proximal_phalanx_l": "f_proximal_phalanx",
        "second_f_middle_phalanx_l": "f_middle_phalanx",
        "second_f_distal_phalanx_l": "f_distal_phalanx",
        "third_f_proximal_phalanx_l": "f_proximal_phalanx",
        "third_f_middle_phalanx_l": "f_middle_phalanx",
        "third_f_distal_phalanx_l": "f_distal_phalanx",
        "thumb_proximal_phalanx_r": "thumb_proximal_phalanx", # parts hand right
        "thumb_distal_phalanx_r": "thumb_distal_phalanx",
        "first_f_proximal_phalanx_r": "f_proximal_phalanx",
        "first_f_middle_phalanx_r": "f_middle_phalanx",
        "first_f_distal_phalanx_r": "f_distal_phalanx",
        "second_f_proximal_phalanx_r": "f_proximal_phalanx",
        "second_f_middle_phalanx_r": "f_middle_phalanx",
        "second_f_distal_phalanx_r": "f_distal_phalanx",
        "third_f_proximal_phalanx_r": "f_proximal_phalanx",
        "third_f_middle_phalanx_r": "f_middle_phalanx",
        "third_f_distal_phalanx_r": "f_distal_phalanx",
    }

    bones_short = [
        "base",
        "body_lower_panel_front_l",
        "body_lower_panel_front_r",
        "body_lower_panel_back_l",
        "body_lower_panel_back_r",
        "camera_front",
        "camera_shoulder",
        "thumb_proximal_phalanx_l",
        "thumb_distal_phalanx_l",
        "first_f_proximal_phalanx_l",
        "first_f_middle_phalanx_l",
        "first_f_distal_phalanx_l",
        "second_f_proximal_phalanx_l",
        "second_f_middle_phalanx_l",
        "second_f_distal_phalanx_l",
        "third_f_proximal_phalanx_l",
        "third_f_middle_phalanx_l",
        "third_f_distal_phalanx_l",
        "thumb_proximal_phalanx_r",
        "thumb_distal_phalanx_r",
        "first_f_proximal_phalanx_r",
        "first_f_middle_phalanx_r",
        "first_f_distal_phalanx_r",
        "second_f_proximal_phalanx_r",
        "second_f_middle_phalanx_r",
        "second_f_distal_phalanx_r",
        "third_f_proximal_phalanx_r",
        "third_f_middle_phalanx_r",
        "third_f_distal_phalanx_r",
    ]

def main():
    fnames = [PathInfo.file_posture_model_default, PathInfo.file_posture_model_posed]
    for fname in fnames:
        apply_const(os.path.join(PathInfo.dir_posture_json,fname))

def apply_const(posture_file):
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())
    for key in Const.bones:
        length = Const.bone_default_len
        if key in Const.bones_short:
            length = Const.bone_default_len_small
        
        if pw.has_key(key):
            pw.set_length(key, length)
        else:
            pw.add_bone(key, Const.bones_relationship[key], length)

    json_loader.dictionary = pw.postures
    json_loader.dump()
    
if __name__ == "__main__":
    main()
