#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    c_item = None
    total = 0
    for line in sys.stdin:
        item, val = line.split("\t")
        val = int(val)
        if item == c_item:
            total += val
        else:
            if c_item is not None:
                sys.stdout.write("{}\t{}\n".format(c_item, total))
            c_item = item
            total = val
    sys.stdout.write("{}\t{}\n".format(c_item, total))