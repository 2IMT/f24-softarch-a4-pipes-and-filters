import cv2


class VideoSource:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
