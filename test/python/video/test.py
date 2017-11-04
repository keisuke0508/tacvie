import cv2
import time

class Test:
    def __init__(self):
        pass

    def main(self):
        video = self.get_video()
        while video.isOpened():
            ret, frame = video.read()
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(0.01)
        video.release()
        cv2.destroyAllWindows()


    def get_video(self):
        return cv2.VideoCapture("../../../static/video/test.mov")


if __name__ == "__main__":
    Test().main()
