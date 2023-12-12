import re
import sys

def clean_text(txt, repl_txt=["\*"," {2,}"]):
    txt = re.sub(repl_txt[0],"\n- ",txt)
    for repl in repl_txt[1:]:
        txt = re.sub(repl, " ",txt)
    return(txt)

if __name__ == "__main__":
    print(clean_text(sys.argv[1]))
