import sys

def autoCounter(spellLevel, counterLevel):
    if spellLevel > counterLevel:
        return False
    else:
        return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use: python comparatory.py <spell level> <counter level>")
        sys.exit(1)
    else:
        if autoCounter(sys.argv[1], sys.argv[2]):
            print("Auto Countered")
        else:
            print("roll for counter")
