#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 
if __name__ == "__main__":
    for line in sys.stdin:
        word = line.split('   ')[1].split('-')[1]
        sys.stdout.write(word+'\n')  