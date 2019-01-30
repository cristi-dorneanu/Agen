import cv2

IMAGE_RESIZE_INTERPOLATION = cv2.INTER_LINEAR
OUTLINE_RECTANGLE_THICKNESS = 5
OUTPUT_IMAGE_SIZE = (224, 224)
IMAGE_SIZE_DIVISOR = 14
SCALE_FACTOR = 1.2
MIN_NEIGHBORS = 2
CASCADE_CLASSIFIER_PATH = '../../resources/haarcascade_frontalface_alt.xml'
ORIGINAL_IMAGE_LABEL = 'original'
CROPPED_IMAGE_LABEL = 'cropped'
DATASET_PATH = '../../resources/dataset/'
DATASET_CROPPED_PATH = '../../resources/cropped-dataset/'
METADATA_PATH = '../../resources/imdb.mat'
ARCHIVE_PATHS = '../../resources/archives/'
SAVED_WEIGHTS_PATH = '../../resources/training/model/CnnNetwork.h5'
