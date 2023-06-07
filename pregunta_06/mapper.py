#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 
if __name__ == "__main__":
    for line in sys.stdin:
        word = line.split('   ')[0]
        number=line.split('   ')[2]
        sys.stdout.write(word.strip()+'\t'+number.strip()+'\n')  