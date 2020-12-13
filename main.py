import os, re

def get_config():
    f = open("config.txt","r")
    content = f.read()
    f.close()

    config = {}
    for line in content.split("\n"):
        key,value = line.split("=")
        config[key] = value
    return config

def make_filepath(path):
    parts = path.split("/")
    if "." in parts[-1]:
        parts = parts[:-1]
    for i in range(len(parts)):
        partial = "/".join(parts[:i+1])
        if not os.path.exists(partial):
            os.mkdir(partial)

def get_filepath(root,fname):
    if re.compile("[0-9]{3} [0-9]{3}").match(fname):
        fname = fname[:3] + fname[4:]
    if re.compile("[0-9]{6} ").match(fname):
        return "/".join([root,fname[:1]+"00000",fname[:3]+"000",fname[:4]+"00",fname.split(".")[0],fname])
    else:
        return root+"/"+fname