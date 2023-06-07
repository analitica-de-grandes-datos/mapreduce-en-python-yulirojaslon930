#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 
if __name__ == "__main__":
    for j,line in enumerate(sys.stdin):
        if j==0:
            ID=[i for i, k in enumerate(line.split(',')) if k == 'credit_history']
        word = line.split(',')[int(ID[0])]
        sys.stdout.write("{}\t1\n".format(word)) 