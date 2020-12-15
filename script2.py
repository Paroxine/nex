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
log = []
for i in range(len(fpaths)):
    print(fpath)
    fname = fpaths[i]
    fname = fpath.split("/")[-1]
    if fname in remaining:
        fnames_in.append(fname)
        path = get_filepath(config["in"],fname)
        try:
            make_filepath(path)
            copyfile(config["middle"] + "/" + fname, path)
        except:
            log.append(fname)
    else:
        fnames_out.append(fname)
        path = get_filepath(config["out"],fname)
        try:
            make_filepath(path)
            copyfile(config["root"] + "/" + fpath,path)
        except:
            log.append(fname)
 
for entry in log:
    print("ERR : " + entry)

f = open(config["fnames_in"],"w")
try:
    f.write("\n".join(fnames_in))
except:
    print("Failed to write fnames_in")
finally:
    f.close()

f = open(config["fnames_out"],"w")
try:
    f.write("\n".join(fnames_out))
except:
    print("Failed to write fnames_out")
finally:
    f.close()
