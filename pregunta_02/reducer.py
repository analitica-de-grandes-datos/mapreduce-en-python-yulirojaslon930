#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    c_item = None
    max_val = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == c_item:
            if val > max_val:
                max_val = val
        else:
            if c_item is not None:
                sys.stdout.write("{}\t{}\n".format(c_item, max_val))
            c_item = key
            max_val = val
    sys.stdout.write("{}\t{}\n".format(c_item, max_val))