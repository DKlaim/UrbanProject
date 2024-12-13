import multiprocessing as mp
from PIL import Image


def resize_image(image_paths, queue):
    pass


def change_color(queue):
    pass


if __name__ == '__main__':
    data = []
    queue = mp.Queue()

    for image in range(1, 201):
        data.append(f'./images/img_{image}.jpg')

    resize_process = mp.Process(target=resize_image, args=(data, queue))
    change_process = mp.Process(target=change_color, args=(queue,))

    resize_process.start()
    change_process.start()

    resize_process.join()
    change_process.join()
