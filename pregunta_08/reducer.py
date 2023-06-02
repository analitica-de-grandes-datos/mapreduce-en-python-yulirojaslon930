#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys  
if __name__ == '__main__':
    current_item = None
    total = 0
    n = 0
    promedio = 0
    for line in sys.stdin:
        key, val = line.split(",")
        val = float(val)
        if key == current_item:
            total += val
            n += 1
            promedio = total/n
        else:
            if current_item is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(current_item, total, promedio))
            current_item = key
            total = val
            n = 1
            promedio = total/n
    sys.stdout.write("{}\t{}\t{}\n".format(current_item, total,promedio))