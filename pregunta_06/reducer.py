#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    current_value = None
    max_value = 0
    min_value = 0
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split(',')
        value = float(value)
        if key == current_value:
            if value > max_value:
                max_value = value
            if value < min_value:
                min_value = value
        else:
            if current_value is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(current_value, max_value, min_value))
            current_value = key
            max_value = value
            min_value = value
    sys.stdout.write("{}\t{}\t{}\n".format(current_value, max_value, min_value))