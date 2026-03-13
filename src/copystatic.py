import os, shutil

def copystat(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    copy_recurive(src, dst)
def copy_recurive(src,dst):
    for entry in os.listdir(src):
        src_path = os.path.join(src, entry)
        dst_path = os.path.join(dst, entry)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else: 
                os.mkdir(dst_path)
                copy_recurive(src_path, dst_path)
        