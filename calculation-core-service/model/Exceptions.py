import util.Constant as Constants


class WeightsLoadingException(Exception):
    def __init__(self, message=Constants.WEIGHTS_LOADING_EXCEPTION_MESSAGE):
        super(WeightsLoadingException, self).__init__(message)


class NoFaceDetectedException(Exception):
    def __init__(self, message=Constants.FACE_NOT_FOUND_EXCEPTION_MESSAGE):
        super(NoFaceDetectedException, self).__init__(message)


class CalculationFailedException(Exception):
    def __init__(self, message=Constants.CALCULATION_FAILED_EXCEPTION_MESSAGE):
        super(CalculationFailedException, self).__init__(message)