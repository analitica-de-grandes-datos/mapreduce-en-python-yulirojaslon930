#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    l = []
    for line in sys.stdin:
        key, fe, val = line.strip().split(",")
        l.append((key, fe, val))
    l = sorted(l, key=lambda x: int(x[2]))[:6]
    for i in l:
        sys.stdout.write("{}   {}   {}\n".format(i[0], i[1], i[2]))