# pip install cowsay
import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.cow("hola, " + sys.argv[1])
