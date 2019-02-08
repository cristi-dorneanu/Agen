import cv2
import util.Constant as Constant
import numpy as np


#from book
def is_gray_image(image):
    return image.ndim < 3


#from book
def bgr_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def bgr_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def gray_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)


def divide_image_shape_by(divisor, image):
    height = image.shape[0]
    width = image.shape[1]

    return height // divisor, width // divisor


def get_largest_face_from(sizes):
    max_size = 0
    largest_face = None

    for (x, y, w, h) in sizes:
        if w * h > max_size:
            max_size = w * h
            largest_face = (x, y, w, h)

    return largest_face


def draw_rectangle(size, image, color=(0, 255, 0)):
    x, y, w, h = size

    cv2.rectangle(image, (x - 20, y - 30), (x + w + 20, y + h + 30), color, thickness=Constant.OUTLINE_RECTANGLE_THICKNESS)


def crop_by(size, image):
    x, y, w, h = size

    return image[y: y + h, x: x + w]


def resize(image):
    return cv2.resize(image, Constant.IMAGE_SIZE, Constant.IMAGE_RESIZE_INTERPOLATION)


def get_gender_from_result_array(result_array):
    result = get_index_of_one(result_array)

    if result is None:
        return None

    return "FEMALE" if result == 0 else "MALE"


def get_age_from_result(result_array):
    age_classes = [1, 10, 15, 21, 28, 35, 42, 50, 65, 80, 100]
    result = get_index_of_one(result_array)

    if result is None:
        return None

    return age_classes[result]


def get_index_of_one(array):
    max_value = 0
    max_pos = 0

    for counter, value in np.ndenumerate(array[0]):
        if value > max_value:
            max_value = value
            max_pos = counter[0]

    return max_pos


def load_face(image):
    face = np.empty((1, 128, 128, 3))
    face[0, :, :, :] = image

    return face
