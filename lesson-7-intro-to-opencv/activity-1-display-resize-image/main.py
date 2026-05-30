import cv2

# Load the image
image = cv2.imread('example.jpg')

# Create a resizable window and set its size
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 800, 500)

# Display the image
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print image properties
print(f"Image Dimensions: {image.shape}")  # Height, Width, Channels
