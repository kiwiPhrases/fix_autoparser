import re
import sys
import os

def read_txt_from_file(file_location):
    with open(file_location, 'r') as f:
        txt = f.read()
    return(txt)

def clean_text(txt, repl_txt=["\*"," {2,}"]):
    txt = re.sub(repl_txt[0],"\n- ",txt)
    for repl in repl_txt[1:]:
        txt = re.sub(repl, " ",txt)
    return(txt)

if __name__ == "__main__":
    file_location = sys.argv[1]
    if os.path.exists(file_location):
        txt = read_txt_from_file(sys.argv[1])
        print(clean_text(txt))
    if os.path.exists(file_location) is False:
        print(file_location)
        print("Check path, it doesn't seem to exist")
