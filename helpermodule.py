

def confirm(questionstr):
    print questionstr + "(Y/N)"
    str = raw_input()
    if str == "Y" or str == "y" or str == "yes":
        return True
    else:
        return False
