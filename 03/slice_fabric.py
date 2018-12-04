
slices = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]


class Slice:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return f'{self.x},{self.y}: {self.w}x{self.h}'


def create_slice(line):
    arr = line.split()
    x, y = arr[2].split(',')
    x, y = int(x), int(y[:-1])
    w, h = arr[3].split('x')
    w, h = int(w), int(h)
    return Slice(x, y, w, h)

for i in slices:
    print(create_slice(i))