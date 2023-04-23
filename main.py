import cv2

# Open the video file using OpenCV
cap = cv2.VideoCapture('example.mp4')

# Loop through the frames of the video
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()
    if ret:
        # Display the frame
        cv2.imshow('frame', frame)
        # Wait for 25 milliseconds and check if the user has pressed the 'q' key
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and destroy the display window
cap.release()
cv2.destroyAllWindows()
