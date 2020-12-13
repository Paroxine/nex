import os
from shutil import copyfile
import re
from main import *

config = get_config()
if not os.path.exists(config["in"]):
    os.mkdir(config["in"])
if not os.path.exists(config["out"]):
    os.mkdir(config["out"])
if not os.path.exists(config["middle"]):
    os.mkdir(config["middle"])
pattern = re.compile(config["pattern"])

files = []
root = config["root"]
if root[-1] != "/":
    root += "/"
dirs = [d for d in os.listdir(root) if not "." in d]
i = 0
while len(dirs) > 0:
    d = str(dirs.pop())
    i += 1
    print("DIR {} {}".format(i,d))
    for entry in os.listdir(root + d):
        if not os.path.isdir(root + d  + "/" + entry):
            files.append(d + "/" + entry)
        else:
            dirs.append(d + "/" + entry)

log = []
n = len(files)
for i in range(n):
    f = files[i]
    print("{}/{} {}".format(i,len(files),f))
    fname = f.split("/")[-1]
    if not pattern.match(f.split("/")[-1]):
        try:
            copyfile(root + "/" + f, config["middle"] + "/" + fname)
        except Exception as e:
            log.append("ERR on {}\n{}\n\n".format(f, e))

f = open(config["fpaths"], "w")
for fl in files:
    f.write(fl + "\n")
f.close()

f = open("log.txt", "w")
f.write("\n".join(log))
f.close()