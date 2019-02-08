import util.Constant as Constants
import os
import core.keras.Training as Training
from model.Network import CnnNetwork
from model.Exceptions import WeightsLoadingException, NoFaceDetectedException, CalculationFailedException
from core.facedetection.FaceDetection import FaceDetector
import util.FaceUtils as FaceUtils
import util.FileUtils as FileUtils


class AgeAndGenderEvaluator:
    def __init__(self, age_saved_weights_path=Constants.AGE_WEIGHTS_PATH, gender_saved_weights_path=Constants.GENDER_WEIGHTS_PATH):
        self.age_saved_weights_path = age_saved_weights_path
        self.gender_saved_weights_path = gender_saved_weights_path
        self.age_model = None
        self.gender_model = None
        self.face_detector = None

        self.load_saved_weights()

    def load_saved_weights(self):
        if not os.path.exists(self.age_saved_weights_path) or os.path.exists(self.gender_saved_weights_path):
            Training.setup()

        self.age_model = CnnNetwork((128, 128, 3)).get_model('age')
        self.gender_model = CnnNetwork((128, 128, 3)).get_model('gender')

        try:
            self.age_model.load_weights(self.age_saved_weights_path)
            self.gender_model.load_weights(self.age_saved_weights_path)
        except Exception:
            raise WeightsLoadingException()

        self.face_detector = FaceDetector()

    def calculate(self, image_path, calculation):
        result = self.face_detector.detect(image_path)

        if result is None or result[Constants.ORIGINAL_IMAGE_LABEL] is None or result[Constants.CROPPED_IMAGE_LABEL] is None:
            raise NoFaceDetectedException()

        FileUtils.write_image_to_disk(image_path, None, result[Constants.ORIGINAL_IMAGE_LABEL])
        calculation.image = FileUtils.read_from_file(image_path)

        face = FaceUtils.load_face(result[Constants.CROPPED_IMAGE_LABEL])
        age_result = self.age_model.predict(face)
        gender_result = self.gender_model(face)

        if age_result is None or gender_result is None:
            raise CalculationFailedException()

        predicted_gender = FaceUtils.get_gender_from_result_array(gender_result)
        predicted_age = FaceUtils.get_age_from_result(age_result)

        calculation.estimatedGender = predicted_gender
        calculation.estimatedAge = predicted_age

        return calculation

