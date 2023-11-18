import hashlib
import os

def get_unique_string(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)

    # Truncate the hash to the first 5 characters
    truncated_hash = hasher.hexdigest()[:5]
    return truncated_hash

# def resolve_duplicate(filepath):
#     return filepath # same filename =  do override
    
def is_duplicate(filepath):
    return os.path.exists(filepath)

def get_ext(filepath):
    return filepath.split(".")[-1]

def make_output_path_from_instrument(input_path, export_path, save_format, instrument):
    id = get_unique_string(input_path)
    file_ext = len(get_ext(input_path))
    file_base = os.path.basename(input_path)
    out = os.path.join(export_path, file_base[:-(1 + file_ext)])
    out = out + "_" + instrument + "_" +  id + "." + save_format
    return out

def make_output_path(input_path, export_path, save_format, file_base):
    #file_base is an ugly file base that UVR generates thru the program.
    if "(Instrumental)" in file_base:
        true_outpath = make_output_path_from_instrument(input_path, export_path, save_format, "(Inst)")
    elif "(Vocals)" in file_base:
        true_outpath = make_output_path_from_instrument(input_path, export_path, save_format, "(Vocal)")
    return true_outpath
