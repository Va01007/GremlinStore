import random
import sys

with open(sys.argv[1]) as Text_file:
    lines = Text_file.readlines()
sys.stderr.write(f"{lines[random.randint(0,(len(lines)-1))]}\n")
exit()
