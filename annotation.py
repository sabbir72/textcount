import cv2
import os

# Dataset path
dataset_path = r"E:\altersense meeting\2nd demo\oob\labels"

# Load dataset (list of image file paths)
dataset = [os.path.join(dataset_path, file) for file in os.listdir(dataset_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Iterate over the dataset
for image_path in dataset:
    # Read the image
    image = cv2.imread(image_path)

    # Display the image
    cv2.imshow('Select ROI', image)

    # Select ROI
    roi = cv2.selectROI('Select ROI', image, fromCenter=False, showCrosshair=True)

    # Print the coordinates of the bounding box
    print("ROI coordinates for", image_path, ":", roi)

    # Draw the bounding box on the image
    x, y, w, h = roi
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display
