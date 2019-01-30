from tarfile import TarFile
import tarfile
import shutil
import cv2
import os


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
                shutil.move(temp_file_path, output_path)
            except FileNotFoundError:
                continue

        shutil.rmtree(temp_path)


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
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    cv2.imwrite(os.path.join(output_path, filename), image)


def file_exists(path):
    return os.path.exists(path)


def delete_file(file_path):
    if file_exists(file_path):
        os.remove(file_path)


def delete_folder(folder_path):
    if file_exists(folder_path):
        shutil.rmtree(folder_path)


def read_file(path):
    if file_exists(path) and os.path.isfile(path):
        try:
            return open(path, 'r').read()
        except FileNotFoundError:
            return None
