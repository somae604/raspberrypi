from picamera import PiCamera
import time
import datetime

def record():
	with PiCamera() as camera:
		camera.resolution = (640, 480)
		now = datetime.datetime.now()
		filename = now.strftime('%Y-%m-%d %H:%M:%S')
		camera.start_recording(output = filename + '.h264')
		camera.wait_recording(10)
		camera.stop_recording()


while True:
	record()
