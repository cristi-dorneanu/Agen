from model.Network import CnnNetwork
from core.facedetection.FaceDetection import FaceDetector
from os import listdir
from os.path import isfile, join
import scipy.io as sio
from keras.optimizers import SGD
from datetime import datetime
from keras.callbacks import LearningRateScheduler, ModelCheckpoint
import util.FileUtils as FileUtils
import util.Constant as Constants


def setup():
    # download the files

    # extract the archives
    if not FileUtils.file_exists(Constants.DATASET_PATH) and not FileUtils.file_exists(Constants.DATASET_CROPPED_PATH):
        print("Extracting archives")
        extract_all_archives_dataset(Constants.ARCHIVE_PATHS)

    # run face detection on all images and save the cropped face and delete the original images
    if not FileUtils.file_exists(Constants.DATASET_CROPPED_PATH):
        print("running face detector")
        extract_face_from_images(Constants.DATASET_PATH, Constants.DATASET_CROPPED_PATH)

    # load the input data
    input_data = load_input_data(Constants.DATASET_CROPPED_PATH, Constants.METADATA_PATH)

    # train the network
    model = train_network(input_data)

    # save the weights
    model.save_weights(Constants.SAVED_WEIGHTS_PATH, overwrite=True)


def extract_all_archives_dataset(archives_path):
    archives = FileUtils.get_archives_from(archives_path)

    print(archives)

    if archives is None:
        return

    for archive in archives:
        FileUtils.extract_files_from(archive, Constants.DATASET_PATH)


def extract_face_from_images(dataset_path, output_path):
    face_detector = FaceDetector()

    file_paths = [join(dataset_path, file) for file in listdir(dataset_path) if isfile(join(dataset_path, file))]

    for file in file_paths:
        result = face_detector.detect(file)

        filename = file.split('/')[-1]

        if result is None or result['cropped'] is None:
            continue

        FileUtils.write_image_to_disk(output_path, filename, result['cropped'])
        FileUtils.delete_file(file)

    FileUtils.delete_folder(dataset_path)


def load_input_data(dataset_cropped_path, metadata_path):
    file_paths = [join(dataset_cropped_path, file) for file in listdir(dataset_cropped_path) if isfile(join(dataset_cropped_path, file))]

    metadata = load_metadata(metadata_path)

    training_images = []
    label_age = []
    label_gender = []

    for file in file_paths:
        filename = file.split('/')[-1]
        image_metadata = metadata[filename]
        image = FileUtils.read_file(file)

        if image_metadata is None or image is None:
            continue

        training_images.append(image)
        label_age.append(image_metadata['age'])
        label_gender.append(image_metadata['gender'])

    return training_images, label_age, label_gender


def load_metadata(path):
    content = sio.loadmat(path)
    filename_to_metadata = {}

    imdb = content['imdb'][0][0]

    date_of_birth = imdb[0][0]
    photo_taken_year = imdb[1][0]
    full_path = imdb[2][0]
    gender = imdb[3][0]

    for i in range(0, date_of_birth.size - 1):
        birth_year = datetime.fromordinal(int(date_of_birth[i])).year

        file_name = full_path[i][0].split('/')[-1]
        age = photo_taken_year[i] - birth_year

        filename_to_metadata[file_name] = {'age': age, 'gender': gender[i]}

    return filename_to_metadata


def train_network(input_data):
    training_images, label_age, label_gender = input_data

    network = CnnNetwork((224, 224))
    model = network.get_model()

    sgd = SGD(lr=0.1, momentum=0.9, nesterov=True)
    model.compile(optimizer=sgd, loss=["categorical_crossentropy"],
                  metrics=['accuracy'])

    model.count_params()
    model.summary()

    callbacks = [ModelCheckpoint("checkpoint/weights.{epoch:02d}-{val_loss:.2f}.hdf5",
                                 monitor="val_loss",
                                 verbose=1,
                                 save_best_only=True,
                                 mode="auto")
                 ]

    print("Starting training")

    hist = model.fit(training_images, [label_gender], batch_size=32, epochs=30, callbacks=callbacks,
                     validation_split=0.1)

    return model


setup()