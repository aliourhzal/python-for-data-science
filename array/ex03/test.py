from PIL import Image
import numpy as np

# Open the image
img = Image.open("animal.jpeg")

# Convert to RGB (in case it's not already in RGB mode)
img_rgb = img.convert("RGB")

# Convert to a NumPy array
arr = np.array(img_rgb)

# Ensure the array is 3D (height, width, channels)
print(arr.shape)  # Should output something like (height, width, 3)

# Drop the green channel (set it to 0) but keep the 3D structure
arr[:, :, 1] = 0  # Set green channel (index 1) to 0

# Print the shape of the array after modification
print(arr.shape)  # It should still be (height, width, 3)

# Convert back to an image
img_dropped_green = Image.fromarray(arr)

# Show the modified image
img_dropped_green.show()