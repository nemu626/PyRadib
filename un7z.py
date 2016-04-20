# coding: utf-8
import subprocess
import sys
import os
import re
import shutil

test = u"[2016.04.12] 村川梨衣の ａ りえしょんぷり～ず♡ #54.flv"
t = "t.txt"
tt = "tt"
def un7z(filename):
    subprocess.call(["7za","e",filename,"-aoa"])
def joinwithspace(words):
    return(' '.join(words))

def trim_radio_name(fname):
    pattern = r"\[\d{4}\.\d{2}\.\d{2}\](.*)#\d+\.(mp4|mp3|flv|m4a|wmv|aac|avi)"
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
        shutil.move(filename,dirpath + "\\" + filename)
        

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        words = joinwithspace(sys.argv[1:])
        un7z(words)
    else:
        dirname = trim_radio_name(test)
        res = makedir(dirname)
        movefile(test,dirname)
     
        