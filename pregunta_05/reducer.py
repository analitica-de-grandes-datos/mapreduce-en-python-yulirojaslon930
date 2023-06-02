#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys       
if __name__ == '__main__':
    l = []  
    for line in sys.stdin:
        line = line.strip().split()
        l.append(line)
    for i in sorted(set([i[0] for i in l])):
        sys.stdout.write('{}\t{}\n'.format(i,l.count([i])))