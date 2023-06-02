#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        line = line.strip().split(",")
        lines.append(line)
    l=sorted(lines,key=lambda x: x[1])
    for line in l:
        sys.stdout.write("{},{}\n".format(line[0],line[1]))
