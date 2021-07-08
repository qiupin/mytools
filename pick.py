#!/usr/bin/env python3

'''pick'''

import os
import re
import sys
import shutil

def pick_cc_file(path, dest, include_dirs):
    '''pick cc file'''
    if not os.path.exists(path):
        print("File %s does not exist" % path)
        return
    if not os.path.exists(dest):
        print("File %s does not exist" % path)
        return

    with open(path) as fd:
        for line in fd:
            result = re.match(r'^\s*#\s*include\s+"(.*)"$', line)
            if result:
                h_file = result.group(1)
                print(h_file)
                if not os.path.exists(h_file):
                    for d in [include_dirs]:
                        tmp_h_file = d + "/" + h_file
                        if os.path.exists(tmp_h_file):
                            h_file = tmp_h_file
                            break
                if not os.path.exists(h_file):
                    continue
                path = os.path.dirname(h_file)
                dest_path = dest + "/" + path
                #print(dest_path)
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                shutil.copy("./" + h_file, dest_path)
                cc_file = h_file[:-1] + "cc"
                if os.path.exists(cc_file):
                    print(cc_file)
                    shutil.copy("./" + cc_file, dest_path)

if __name__ == "__main__":
    # 1: cc file name, 2: out dir, 3: include dirs
    pick_cc_file(sys.argv[1], sys.argv[2], sys.argv[3])
