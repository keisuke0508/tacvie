import cv2

class Test:
    def __init__(self):
        pass

    def main(self):
        cap = cv2.VideoCapture("../../../static/video/test.mov")
        while cap.isOpened():
            ret, frame = cap.read()
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


    def get_video(self):
        return cv2.VideoCapture("../../../static/video/test.mov")


if __name__ == "__main__":
    Test().main()
                            
