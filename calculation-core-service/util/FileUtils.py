from tarfile import TarFile
import tarfile
import shutil
import cv2
import os
import util.Constant as Constants
import base64
import numpy as np
from gzip import GzipFile


def extract_files_from(archive_path, output_path=".", open_mode='r'):
    if not os.path.exists(archive_path):
        raise FileNotFoundError

    if not tarfile.is_tarfile(archive_path):
        raise tarfile.TarError

    with TarFile(archive_path, open_mode) as wiki_archive:
        temp_path = output_path + "/temp"
        all_image_files = wiki_archive.getmembers()
        all_image_files_output_paths = [output_path + "/" + image.path.split('/')[-1] for image in all_image_files if
                                        not image.isdir()]
        all_image_files_temp_paths = [temp_path + "/" + image.path for image in all_image_files if
                                      not image.isdir()]

        print("Extracting " + archive_path)

        wiki_archive.extractall(temp_path)

        for temp_file_path, output_path in zip(all_image_files_temp_paths, all_image_files_output_paths):
            try:
                if 'wiki.mat' in temp_file_path:
                    shutil.move(temp_file_path, Constants.METADATA_OUTPUT_PATH + 'wiki.mat')
                else:
                    shutil.move(temp_file_path, output_path)
            except FileNotFoundError:
                continue

        shutil.rmtree(temp_path)


def extract_files_from_gzip(archive_path, output_path=".", open_mode='rb'):
    try:
        with GzipFile(archive_path, open_mode) as wiki_archive:
            wiki_archive.extractall(output_path)
    except:
        pass


def get_archives_from(path):
    if not file_exists(path):
        return None

    if os.path.isfile(path):
        if tarfile.is_tarfile(path):
            return path
    else:
        return [os.path.join(path, file_path) for file_path in os.listdir(path) if
                os.path.isfile(os.path.join(path, file_path)) and tarfile.is_tarfile(os.path.join(path, file_path))]

    return None


def write_image_to_disk(output_path, filename, image):
    create_dir(output_path)

    if filename is not None:
        output_path = os.path.join(output_path, filename)

    cv2.imwrite(output_path, image)


def write_calculation_file_to_disk(filename, image, output_path=Constants.CALCULATION_FILE_PATH):
    filename = filename + Constants.IMAGE_EXTENSION
    file_path = os.path.join(output_path, filename)

    if image is None:
        return

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    numpy_array = np.fromstring(base64.b64decode(image), np.uint8)
    img = cv2.imdecode(numpy_array, cv2.IMREAD_ANYCOLOR)

    cv2.imwrite(file_path, img)

    return file_path


def file_exists(path):
    return os.path.exists(path)


def delete_file(file_path):
    if file_exists(file_path):
        os.remove(file_path)


def delete_folder(folder_path):
    if file_exists(folder_path):
        shutil.rmtree(folder_path)


def read_from_file(file_path):
    if not os.path.exists(file_path):
        return None

    file = open(file_path, 'rb')
    file_data = str(base64.b64encode(file.read()), 'utf-8')
    file.close()

    return file_data


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)