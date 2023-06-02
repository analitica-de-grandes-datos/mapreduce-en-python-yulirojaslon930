#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    lista = []
    for line in sys.stdin:
        line = line.strip().split('\t')
        lista.append(line)
    l = sorted(lista,key=lambda x: (x[0],int(x[2])))
    for i in l:
        sys.stdout.write('{}   {}   {}\n'.format(i[0],i[1],i[2]))