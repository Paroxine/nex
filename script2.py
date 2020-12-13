from main import *
import os
from shutil import copyfile

config = get_config()

f = open(config["fpaths"], "r")
fpaths = f.read().split("\n")
f.close()

fnames_in = []
fnames_out = []
remaining = os.listdir(config["middle"])
for fpath in fpaths:
    print(fpath)
    fname = fpath.split("/")[-1]
    if fname in remaining:
        fnames_in.append(fname)
        path = get_filepath(config["in"],fname)
        make_filepath(path)
        copyfile(config["middle"] + "/" + fname, path)
    else:
        fnames_out.append(fname)
        path = get_filepath(config["out"],fname)
        make_filepath(path)
        copyfile(config["root"] + "/" + fpath,path)

f = open(config["fnames_in"],"w")
f.write("\n".join(fnames_in))
f.close()

f = open(config["fnames_out"],"w")
f.write("\n".join(fnames_out))
f.close()