import os
import cv2
import time


# ---------------------------
# | Definition of variables |
# ---------------------------
points = None
cropping = False


# ----------------------
# | Callback function  |
# ----------------------

def mouse_callback(event, x, y, flags, params):
	# Get global references
	global points

	# Check for events and perform action accordingly
	if event == cv2.EVENT_LBUTTONDOWN:
		points = [(x, y)]
	elif event == cv2.EVENT_LBUTTONUP:
		points.append((x, y))
		cv2.rectangle(frame, points[0], points[1], (0, 255, 0), 2)
		cv2.imshow("image", frame)


# --------
# | Main |
# --------	

# Variables
frame_filename = 'screenshot-{}.jpg'
output_filename = 'sq-{}-{}-screenshot-{}.jpg'
my_time = time.strftime("%d%m%Y-%H%M%S")
my_filename = frame_filename.format(my_time)
pic_id = 1

# Open video
video_filename = 'input/0001.mp4'
cap = cv2.VideoCapture(video_filename)

# Output folder
output_folder = os.path.join('output/', os.path.basename(video_filename))

# Read frame
ret, frame = cap.read()
clone = frame.copy()

# Create named window
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

# Loop
while True:
	# Show frame
	cv2.imshow('image', frame)

	# Get key pressed if any
	key = cv2.waitKey(1) & 0xFF

	# Compare key and perform action
	if key == ord('q'):
		break

	# Reset image if 'r' is pressed
	if key == ord('r'):
		frame = clone.copy()

	# Next frame if space is pressed
	if key == ord(' '):
		ret, frame = cap.read()
		clone = frame.copy()
		my_time = time.strftime("%d%m%Y-%H%M%S")
		my_filename = frame_filename.format(my_time)
		output_folder = os.path.join('output/', os.path.basename(video_filename))
		pic_id = 1

	# Save crop if '1' is pressed (Red light)
	if key == ord('1'):
		roi = clone[points[0][1]:points[1][1], points[0][0]:points[1][0]]
		filename = output_filename.format(1, pic_id, my_time)
		filename = os.path.join(output_folder, filename)
		os.makedirs(os.path.dirname(filename), exist_ok=True)
		cv2.imwrite(filename, roi)

		# Save source file if not saved yet
		frame_save_fn = os.path.join('output/', os.path.basename(video_filename))
		frame_save_fn = os.path.join(frame_save_fn, my_filename)
		if not os.path.exists(frame_save_fn):
			cv2.imwrite(frame_save_fn, clone)
		
		pic_id += 1

	# Save crop if '2' is pressed (Yellow light)
	if key == ord('2'):
		roi = clone[points[0][1]:points[1][1], points[0][0]:points[1][0]]
		filename = output_filename.format(2, pic_id, my_time)
		filename = os.path.join(output_folder, filename)
		os.makedirs(os.path.dirname(filename), exist_ok=True)
		cv2.imwrite(filename, roi)

		# Save source file if not saved yet
		frame_save_fn = os.path.join('output/', os.path.basename(video_filename))
		frame_save_fn = os.path.join(frame_save_fn, my_filename)
		if not os.path.exists(frame_save_fn):
			cv2.imwrite(frame_save_fn, clone)
		
		pic_id += 1

	# Save crop if '3' is pressed (Green light)
	if key == ord('3'):
		roi = clone[points[0][1]:points[1][1], points[0][0]:points[1][0]]
		filename = output_filename.format(3, pic_id, my_time)
		filename = os.path.join(output_folder, filename)
		os.makedirs(os.path.dirname(filename), exist_ok=True)
		cv2.imwrite(filename, roi)

		# Save source file if not saved yet
		frame_save_fn = os.path.join('output/', os.path.basename(video_filename))
		frame_save_fn = os.path.join(frame_save_fn, my_filename)
		if not os.path.exists(frame_save_fn):
			cv2.imwrite(frame_save_fn, clone)
		
		pic_id += 1


# Close all open windows
cv2.destroyAllWindows()