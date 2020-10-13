import time
import picamera as camera

def main(args):
    cam = camera.PiCamera()
    cam.start_preview()
    time.sleep(3)
    cam.capture("cam01.jpg")
    cam.stop_preview()
    cam.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

