import cv2

IMAGE_RESIZE_INTERPOLATION = cv2.INTER_LINEAR
OUTLINE_RECTANGLE_THICKNESS = 5
IMAGE_SIZE = (128, 128)
IMAGE_SIZE_DIVISOR = 14
SCALE_FACTOR = 1.2
MIN_NEIGHBORS = 5
CASCADE_CLASSIFIER_PATH = 'app/resources/haarcascade_frontalface_alt.xml'
ORIGINAL_IMAGE_LABEL = 'original'
CROPPED_IMAGE_LABEL = 'cropped'
DATASET_PATH = 'app/resources/dataset/'
DATASET_CROPPED_PATH = 'app/resources/cropped-dataset/'
METADATA_PATH = 'app/resources/imdb.mat'
ARCHIVE_PATHS = 'app/resources/archives/'
WEIGHTS_LOADING_EXCEPTION_MESSAGE = "The weights for the CNN could not be loaded"
FACE_NOT_FOUND_EXCEPTION_MESSAGE = "No face could be detected in the received image"
CALCULATION_FAILED_EXCEPTION_MESSAGE = "The prediction of the age and gender failed"
CALCULATION_FILE_PATH = "app/resources/evaluate"
IMAGE_EXTENSION = ".jpg"
METADATA_OUTPUT_PATH = "app/resources/"
METADATA_URL = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_meta.tar"
CHECKPOINTS_PATH_GENDER = "app/resources/training/checkpoint/gender/"
CHECKPOINTS_PATH_AGE = "app/resources/training/checkpoint/age/"
WIKI_ARCHIVE = "app/resources/wiki.tar.gz"
WIKI_IMAGES_URL = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki.tar.gz"
WIKI_METADATA_PATH = "app/resources/wiki.mat"
CNN_MODEL_PATH = "app/resources/training/model/"
GENDER_WEIGHTS_PATH = "app/resources/training/model/CnnNetworkGender.h5"
AGE_WEIGHTS_PATH = "app/resources/training/model/CnnNetworkAge.h5"
PLOT_PATH = "app/resources/benchmarks/"

URL_LIST = ["https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_1.tar",
            "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_2.tar",
            "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_3.tar",
            "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_4.tar",
            "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_5.tar",
            "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_6.tar",
            "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_7.tar",
            "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_8.tar",
            "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_9.tar"]

