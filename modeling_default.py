import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import os

from harbor3d.util.bone_json_util import PostureWrapper
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo
from spec_model import Const, apply_const

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    posture = os.path.join(PathInfo.dir_posture_json, PathInfo.file_posture_model_default)
    fname = path.split(os.sep)[-1] + '_default.stl'
    
    apply_const(posture)

    sw = Shipwright(Dock())

    json_loader = JsonLoader(posture)
    pw = PostureWrapper(json_loader.fetch())
    objects = sw.load_bones(pw)
    sw.load_submodules_name_match(objects, [PathInfo.dir_parts_renamed], {})

    sw.generate_stl_binary(path, fname=fname, divided=False)

if __name__ == "__main__":
    main()