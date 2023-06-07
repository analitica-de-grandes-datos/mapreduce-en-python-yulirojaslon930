#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    suma = 0
    tot=0
    for line in sys.stdin:
        #print(line.split("\t"))
        
        key, val = line.split(",")
        if key == curkey:
            suma=suma+float(val.strip())
            tot+=1
        else:
            if curkey is not None:
                mean=int(suma)/int(tot)
                sys.stdout.write("{}\t{}\t{}\n".format(curkey[0], suma,mean))

            curkey = key
            suma= float(val.strip())
            tot=1

    mean=int(suma)/int(tot)
    sys.stdout.write("{}\t{}\t{}\n".format(curkey[0], suma, mean))