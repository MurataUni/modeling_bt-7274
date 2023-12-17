import sys
sys.dont_write_bytecode = True

import os

class Const:
    project_path = os.path.dirname(os.path.abspath(__file__))
    dir_posture_json = os.sep.join([project_path, '_postures'])

    folder_divided = 'divided'

    dir_parts_single_mesh = os.sep.join([project_path, '_parts_single_mesh']) 
    dir_parts_optimized_for_print = os.sep.join([project_path, '_parts_optimized_for_print']) 
    dir_parts_refined = os.sep.join([project_path, '_parts_refined'])
    dir_parts_draft = os.sep.join([project_path, '_parts_draft'])
    dir_parts_other = os.sep.join([project_path, '_parts_other'])
    dirs_parts_modeling = [ #リストの先頭から一致を探す挙動になるので順番注意
        dir_parts_single_mesh,
        dir_parts_optimized_for_print,
        dir_parts_refined,
        dir_parts_draft,
        dir_parts_other,
    ]
    
    dir_parts_reverse = os.sep.join([project_path, '_parts_reversed'])
    dirs_parts_assembly = [dir_parts_reverse] + dirs_parts_modeling

    dir_parts_renamed = os.sep.join([project_path, '_parts_renamed', folder_divided])
    
    file_posture_model_default = 'model.json'
    file_posture_model_posed = 'model_posed.json'

def output_list():
    output = {
        "model": {
            "parts": os.path.join(Const.project_path, Const.dir_parts_renamed),
            "posture_default": os.path.join(Const.dir_posture_json, Const.file_posture_model_default),
            "posture_posed": os.path.join(Const.dir_posture_json, Const.file_posture_model_posed),
        },
    }
    file_full_name =  os.sep.join([Const.project_path, 'path_list.txt'])
    f = open(file_full_name, "w", encoding="ascii")
    for name, path_dict in output.items():
        f.write("[" + name + "]\n")
        max_path_name = len(max(path_dict.keys(), key=len))
        for path_name, path_value in path_dict.items():
            f.write(path_name.ljust(max_path_name, ' ') + ": " + path_value + "\n")
        f.write("\n")
    f.close()

if __name__ == "__main__":
    output_list()
