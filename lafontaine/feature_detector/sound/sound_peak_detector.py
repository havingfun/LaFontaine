from lafontaine.feature_detector.feature import Feature
from lafontaine.feature_detector.feature_result import FeatureResult
from lafontaine.parser.frame import Frame
import numpy


class SoundPeakDetector(Feature):
    RESULT_FRAMES = 100
    FEATURE_ID = 'SoundPeakDetector'

    def __init__(self, audio_threshold):
        self.audio_threshold = audio_threshold

    def check_feature(self, frame: Frame):
        frame_mean = numpy.sqrt((frame.audio*1.0)**2).mean()
        result = frame_mean > self.audio_threshold
        if result:  # We have to do this because numpy bool_ is True will return false
            return FeatureResult(True, self.RESULT_FRAMES, self.FEATURE_ID)
        else:
            return FeatureResult(False, self.RESULT_FRAMES, self.FEATURE_ID)

