#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


if __name__ == '__main__':
    curkey=None
    datos=[]

    for line in sys.stdin:
        key, val = line.split(",")
        if key == curkey:
            datos.append(int(val.strip()))
        else:
            if curkey is not None:
                datos.sort()
                datos=str(datos)[1:-1]
                sys.stdout.write("{}\t{}\n".format(curkey[0], datos.replace(' ','')))
                datos=[]

            curkey = key
            datos.append(int(val.strip()))
    datos.sort()
    datos=str(datos)[1:-1]
    sys.stdout.write("{}\t{}\n".format(curkey[0], datos.replace(' ','')))