#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    l = []
    for line in sys.stdin:
        valor,letra = line.strip().split(' ')
        l.append((letra, valor))
    l.sort()
    gl = {}
    for key, value in l:
        if key in gl:
            gl[key].append(value)
        else:
            gl[key] = [value]
    for key, value in gl.items():
        gl[key] = sorted(value, key=lambda x: int(x))
    rl = {}
    for key, values in gl.items():
        rl[key] = ','.join(values)

    for key, value in rl.items():
        sys.stdout.write("{}\t{}\n".format(key,value))