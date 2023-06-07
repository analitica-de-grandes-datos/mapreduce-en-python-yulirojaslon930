#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    total = 0

    for line in sys.stdin:
        key= line.split('\n')
        #print(key)
        #print(curkey)
        if key == curkey:
            total += 1
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey[0], total))

            curkey = key
            total = 1
    sys.stdout.write("{}\t{}\n".format(curkey[0], total))