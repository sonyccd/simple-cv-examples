import math

import matplotlib.pyplot as plt
from skimage import data, io

IMAGE_FILE = ''


def is_square(x):
    if x == 1:
        return True
    low = 0
    high = x // 2
    root = high
    while root * root != x:
        root = (low + high) // 2
        if low + 1 >= high:
            return False
        if root * root > x:
            high = root
        else:
            low = root
    return True


def smallest_factors_distance(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    if math.fmod(len(result), 2) != 0:
        raise ArithmeticError('Must have even number of factors')
    if len(result) < 4:
        raise ArithmeticError('Can not find smallest factor distance of prime numbers ' + result[1])
    return result[int((len(result) / 2) - 1)], result[int(len(result) / 2)]


def plot_images(images):
    if is_square(len(images)):
        x = y = int(math.sqrt(len(images)))
    else:
        x, y = smallest_factors_distance(len(images))
    f, ax = plt.subplots(x, y)
    for index, img in enumerate(images):
        i = int(index / max(x, y))
        j = int(math.fmod(index, max(x, y)))
        ax[i, j].imshow(img, cmap='gray')
        ax[i, j].axis('off')
    return f, ax


if __name__ == '__main__':
    image = None
    if IMAGE_FILE == '':
        image = data.camera()
    else:
        try:
            image = io.imread(IMAGE_FILE)
        except IOError:
            print('Could not find or read ' + IMAGE_FILE)
            exit()
        else:
            print('Unknown error reading file!')
            exit()
    plot_images([data.camera(), data.astronaut(), data.text(), data.chelsea(), data.chelsea(), data.astronaut(),
                 data.astronaut(), data.chelsea(), data.camera()])
    plt.tight_layout()
    plt.show()
