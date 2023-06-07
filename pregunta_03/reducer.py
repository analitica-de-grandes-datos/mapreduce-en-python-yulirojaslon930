#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
datos=[]
if __name__ == '__main__':
    for line in sys.stdin:
        dat=line.strip()
        datos.append(dat.split(","))
    datos.sort(key=lambda x: x[1])
    #print(datos)
    for i in datos:
        #print(i[0]+','+i[1])
        sys.stdout.write(i[0]+','+i[1]+'\n')
