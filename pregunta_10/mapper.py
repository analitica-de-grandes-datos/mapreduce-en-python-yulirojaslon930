#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 
if __name__ == "__main__":
    for line in sys.stdin:
        number=line.split('\t')[0]
        for word in line.split('\t')[1].split(','):
            sys.stdout.write(word.strip()+','+number.strip()+'\n') 