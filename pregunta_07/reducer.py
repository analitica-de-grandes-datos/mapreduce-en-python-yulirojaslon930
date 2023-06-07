#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
datos=[]
if __name__ == '__main__':
    for line in sys.stdin:
        dat=line.strip()
        datos.append(dat.split(","))
        #print(datos)
    datos.sort(key=lambda x: (x[0],int(x[2])))
    #datos.sort(key=lambda x: x[2])
    #print(datos)
    for i in datos:
        #print(i[0]+','+i[1])
        sys.stdout.write(i[0]+'   '+i[1]+'   '+i[2]+'\n')