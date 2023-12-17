import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2]))
from path_info import Const as PathInfo

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    target  = 'body_lower_panel_front_l.stl'
    fname = path.split(os.sep)[-1] + '.stl'

    sw = Shipwright(Dock())

    if sw.search_and_load_stl(PathInfo.dirs_parts_modeling, target) == None:
        raise Exception("File not found: " + target)

    sw.deformation_all(lambda x,y,z: (-x,y,z))
    for ship in sw.dock.ships:
        if ship.is_monocoque():
            for triangle in ship.monocoque_shell.triangles:
                triangle.inverse()

    sw.generate_stl_binary(path, fname, divided=False)

if __name__ == "__main__":
    main()