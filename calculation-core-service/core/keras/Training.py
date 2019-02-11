from model.Network import CnnNetwork
from core.facedetection.FaceDetection import FaceDetector
from os import listdir
from os.path import isfile, join
import scipy.io as sio
from keras.optimizers import SGD
from datetime import datetime
from keras.callbacks import ModelCheckpoint, LearningRateScheduler
import util.FileUtils as FileUtils
import util.Constant as Constants
import matplotlib.image as mpimg
import numpy as np
from keras.utils import np_utils
from core.Downloader import DatasetDownloader
from keras.utils import plot_model
import matplotlib.pyplot as plot


def setup():
    # download the metadata archive and extract it
    if not FileUtils.file_exists(Constants.METADATA_PATH):
        metadata_archive_path = FileUtils.get_archives_from(Constants.METADATA_OUTPUT_PATH)

        if metadata_archive_path is None or len(metadata_archive_path) == 0:
            downloader = DatasetDownloader(Constants.METADATA_OUTPUT_PATH, [Constants.METADATA_URL])
            downloader.download_dataset()

        extract_all_archives_dataset(Constants.METADATA_OUTPUT_PATH, Constants.METADATA_OUTPUT_PATH)

    # download the dataset archives
    dataset_archives_path = FileUtils.get_archives_from(Constants.ARCHIVE_PATHS)
    if dataset_archives_path is None or len(dataset_archives_path) == 0:
        downloader = DatasetDownloader()
        downloader.download_dataset()

        downloader = DatasetDownloader(Constants.METADATA_OUTPUT_PATH, [Constants.WIKI_IMAGES_URL])
        downloader.download_dataset()
        extract_wiki_archives(Constants.WIKI_ARCHIVE, Constants.ARCHIVE_PATHS)

    # extract the archives
    if not FileUtils.file_exists(Constants.DATASET_PATH) and not FileUtils.file_exists(Constants.DATASET_CROPPED_PATH):
        print("Extracting archives")
        extract_all_archives_dataset(Constants.ARCHIVE_PATHS, Constants.DATASET_PATH)

    # run face detection on all images and save the cropped face and delete the original images
    if not FileUtils.file_exists(Constants.DATASET_CROPPED_PATH):
        print("running face detector")
        extract_face_from_images(Constants.DATASET_PATH, Constants.DATASET_CROPPED_PATH)

    # load the input data
    input_data = load_input_data(Constants.DATASET_CROPPED_PATH, Constants.METADATA_PATH)

    # train the network
    model = train_network(input_data, 'age')

    # save the weights
    model.save_weights(Constants.AGE_WEIGHTS_PATH, overwrite=True)

    # train the network
    #model = train_network(input_data, 'gender')

    # save the weights
    #model.save_weights(Constants.GENDER_WEIGHTS_PATH, overwrite=True)


def extract_all_archives_dataset(archives_path, output_path):
    archives = FileUtils.get_archives_from(archives_path)

    print(archives)

    if archives is None:
        return

    for archive in archives:
        FileUtils.extract_files_from(archive, output_path)


def extract_wiki_archives(archive_path, output_path):
    archive = Constants.WIKI_ARCHIVE

    if not FileUtils.file_exists(archive):
        return

    FileUtils.extract_files_from_gzip(archive_path, output_path)


def extract_face_from_images(dataset_path, output_path):
    face_detector = FaceDetector()

    file_paths = [join(dataset_path, file) for file in listdir(dataset_path) if isfile(join(dataset_path, file))]

    for file in file_paths:
        result = face_detector.detect(file)

        filename = file.split('/')[-1]

        if result is None or result['cropped'] is None:
            continue

        if result['faces_number'] is None or result['faces_number'] != 1:
            continue

        FileUtils.write_image_to_disk(output_path, filename, result['cropped'])
        FileUtils.delete_file(file)

    FileUtils.delete_folder(dataset_path)


def load_input_data(dataset_cropped_path, metadata_path):
    file_paths = [join(dataset_cropped_path, file) for file in listdir(dataset_cropped_path) if
                  isfile(join(dataset_cropped_path, file))]

    metadata = load_metadata(metadata_path, 'imdb')
    wiki_metadata = load_metadata(Constants.WIKI_METADATA_PATH, 'wiki')
    metadata.update(wiki_metadata)

    age_classes = [1, 10, 15, 21, 28, 35, 42, 50, 65, 80, 100]

    training_images = []
    label_age = []
    label_gender = []

    original_age = []
    original_gender = []

    for file in file_paths:
        filename = file.split('/')[-1]

        if filename not in metadata:
            continue

        image_metadata = metadata[filename]

        if image_metadata is None or np.isnan(image_metadata['gender']) or np.isnan(image_metadata['age']) or \
                        image_metadata['age'] > 100:
            continue

        training_images.append(np.uint8(mpimg.imread(file)))

        age = int(image_metadata['age'])
        gender = int(image_metadata['gender'])

        original_age = age
        original_gender = "FEMALE" if gender == 0 else "MALE"

        age = get_age_class_index(age_classes, age)

        label_age.append(age)
        label_gender.append(gender)

    return np.array(training_images), label_age, label_gender


def get_age_class_index(age_classes, age):
    index = 0

    for counter, value in enumerate(age_classes):
        if age < value:
            index = counter - 1
            break

    return index if index >= 0 else 0


def load_metadata(path, metadata):
    content = sio.loadmat(path)
    filename_to_metadata = {}

    imdb = content[metadata][0][0]

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


def train_network(input_data, output_type):
    training_images, label_age, label_gender = input_data

    label_gender = np_utils.to_categorical(label_gender, 2)
    label_age = np_utils.to_categorical(label_age, 11)

    network = CnnNetwork((128, 128, 3))
    model = network.get_model(output_type)

    sgd = SGD(lr=0.1, decay=0.005, momentum=0.9)
    model.compile(optimizer=sgd, loss=["categorical_crossentropy"], metrics=['accuracy'])

    model.count_params()
    model.summary()

    output_data = None
    output_model_path = Constants.CNN_MODEL_PATH
    checkpoint_path = Constants.PLOT_PATH
    model_plot_path = Constants.PLOT_PATH
    acc_plot = Constants.PLOT_PATH
    loss_plot = Constants.PLOT_PATH

    if output_type == 'age':
        output_data = label_age
        output_model_path += 'CnnModelAge.json'
        checkpoint_path = Constants.CHECKPOINTS_PATH_AGE
        model_plot_path += 'AgeModelPlot.png'
        acc_plot += 'AgeAccPlot.png'
        loss_plot += 'AgeLossPlot.png'
    elif output_type == 'gender':
        output_data = label_gender
        output_model_path += 'CnnModelGender.json'
        checkpoint_path = Constants.CHECKPOINTS_PATH_GENDER
        model_plot_path += 'GenderModelPlot.png'
        acc_plot += 'GenderAccPlot.png'
        loss_plot += 'GenderLossPlot.png'

    if not FileUtils.file_exists(Constants.PLOT_PATH):
        FileUtils.create_dir(Constants.PLOT_PATH)

    if not FileUtils.file_exists(Constants.CNN_MODEL_PATH):
        FileUtils.create_dir(Constants.CNN_MODEL_PATH)

    if not FileUtils.file_exists(checkpoint_path):
        FileUtils.create_dir(checkpoint_path)

    plot_model(model, to_file=model_plot_path)

    with open(output_model_path, "w") as f:
        f.write(model.to_json())

    callbacks = [LearningRateScheduler(update_learning_rate, 1),
                 ModelCheckpoint(checkpoint_path + "weights.{epoch:02d}-{val_loss:.2f}.hdf5",
                                 monitor="val_loss",
                                 verbose=1,
                                 save_best_only=True,
                                 mode="auto")
                 ]

    print("Starting training")

    history = model.fit(training_images, output_data, batch_size=32, epochs=10, callbacks=callbacks, validation_split=0.1)

    save_plot_from_history(history, acc_plot, loss_plot)

    return model


def save_plot_from_history(history, acc_path, loss_path):
    plot.plot(history.history['acc'])
    plot.plot(history.history['val_acc'])
    plot.title('Plot acuratete')
    plot.ylabel('Acuratete')
    plot.xlabel('Epoca')
    plot.legend(['Train', 'Test'], loc='upper left')
    plot.savefig(acc_path, bbox_inches='tight')

    plot.plot(history.history['loss'])
    plot.plot(history.history['val_loss'])
    plot.title('Plot loss')
    plot.ylabel('Loss')
    plot.xlabel('Epoca')
    plot.legend(['Train', 'Test'], loc='upper left')
    plot.savefig(loss_path, bbox_inches='tight')


def update_learning_rate(epoch_index, current_learning_rate):
    return current_learning_rate * 0.1 if epoch_index % 4 == 0 else current_learning_rate
