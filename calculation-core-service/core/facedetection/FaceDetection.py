import cv2
import util.Constant as Constant
import util.FaceUtils as FaceUtils
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join


# inspired from book
class FaceDetector:
    def __init__(self, scale_factor=Constant.SCALE_FACTOR, min_neighbors=Constant.MIN_NEIGHBORS,
                 flags=cv2.CASCADE_SCALE_IMAGE, min_size_divisor=Constant.IMAGE_SIZE_DIVISOR):
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors
        self.flags = flags
        self.min_size_divisor = min_size_divisor

        self.classifier = cv2.CascadeClassifier(Constant.CASCADE_CLASSIFIER_PATH)

    def detect(self, image_path):
        image = cv2.imread(image_path)

        if image is None:
            return None

        original = image.copy()
        cropped = image.copy()

        # convert image to grayscale if not already
        if not FaceUtils.is_gray_image(image):
            image = FaceUtils.bgr_to_gray(image)

        # histogram equalization to improve the contrast in the image - stretches the intensity range
        image = cv2.equalizeHist(image)

        # the min size of the detected face
        min_size = FaceUtils.divide_image_shape_by(self.min_size_divisor, image)

        # detecting the faces from the image
        faces = self.classifier.detectMultiScale(image, scaleFactor=self.scale_factor, minNeighbors=self.min_neighbors,
                                                 flags=self.flags, minSize=min_size)

        if faces is None or len(faces) == 0:
            return None

        # choose only the largest face from the image
        largest_face_recognized = FaceUtils.get_largest_face_from(faces)

        # drawing a rectangle around the detected face in the original image
        FaceUtils.draw_rectangle(largest_face_recognized, original)

        # crop the detected face
        cropped = FaceUtils.crop_by(largest_face_recognized, cropped)
        cropped = FaceUtils.resize(cropped)

        return {Constant.ORIGINAL_IMAGE_LABEL: original, Constant.CROPPED_IMAGE_LABEL: cropped}


def test_detector(path):
    face_det = FaceDetector()

    file_paths = [join(path, file) for file in listdir(path) if isfile(join(path, file))]

    fails = 0
    success = 0

    for file in file_paths:
        result = face_det.detect(file)

        if result is None:
            fails += 1
        else:
            success += 1
            plt.imshow(FaceUtils.bgr_to_rgb(result['cropped']))
            plt.show()

    print("Fails=" + str(fails) + ", success=" + str(success))


# test_detector('../../resources/dataset/')
