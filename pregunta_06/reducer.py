#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    maximo = 0
    minimo = 0
    for line in sys.stdin:
        #print(line.split("\t"))
        
        key, val = line.split("\t")
        #print(value)
        #print(curkey)
        if key == curkey:
            maximo=max(maximo,val)
            minimo=min(minimo,val)
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey[0], maximo.strip(),minimo.strip()))

            curkey = key
            maximo= val
            minimo= val
    sys.stdout.write("{}\t{}\t{}\n".format(curkey[0], maximo.strip(), minimo.strip()))