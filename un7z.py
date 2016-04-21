# coding: utf-8
import subprocess
import sys
import os
import re
import shutil
import helpermodule


def joinwithspace(words):
    return(' '.join(words))

def trim_radio_name(fname):
    pattern = r"\[\d{4}\.\d{2}\.\d{2}\](.*)#.+\.(mp4|mp3|flv|m4a|wmv|aac|avi)"
    compiled = re.compile(pattern)
    match = re.match(pattern,fname).group(1)
    return match.lstrip().rstrip()

def makedir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        return True
    else:
        return False

def movefile(filename,dirpath):
    if os.path.exists(dirpath) and os.path.exists(filename) :
        shutil.move(filename,dirpath + "/" + filename)


def find_7z001_files(dirpath = None):
    path = dirpath if dirpath else os.path.curdir
    flist = os.listdir(dirpath)
    flist_7z = [l for l in flist if l.endswith("7z") or l.endswith("7z.001")]
    return flist_7z

# return value : extracted files or directory name list
def un7z(filename):
    before = os.listdir(os.path.curdir)
    subprocess.call(["7z","e",filename,"-aoa"])
    after = os.listdir(os.path.curdir)
    return list(set(after) - set(before))

# return value : extracted files or directory name list
def un7z_all(filelist):
    extrcted_files = []
    for f in filelist:
        extrcted_files.extend(un7z(f))
    return extrcted_files

def del7z_all(dirpath = None):
    p = dirpath if dirpath != None else os.path.curdir
    flist = os.listdir(p)
    ptn = ".+\.7z\.\d{3}"
    compiled_ptn = re.compile(ptn)

    flist_7z = [l for l in flist if re.match(compiled_ptn,l)]

    res = helpermodule.confirm("Delete " + str(len(flist_7z)) + "files, Contienue?")
    if res:
        for f in flist_7z :
            print "DELETE FILE  :  " + f
            os.remove(f)
        print "Delete Complete..."
    else:
        print "Delete Canceled."

def main(dirpath = None):
    p = dirpath if dirpath != None else os.path.curdir
    l = find_7z001_files(p)
    flist = un7z_all(l)
    for f in flist:
        trimed = trim_radio_name(f)
        makedir(trimed)
        movefile(f,trimed)
    del7z_all(p)


if __name__ == '__main__':
    words = []
    if len(sys.argv) >= 2:
        word = joinwithspace(sys.argv[1:])
        un7z(word)
        words.append(word)
    else :
        main()
