import cv2
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# Load Image
# -----------------------------------

# Replace "image.jpg" with your image name
image = cv2.imread("image.jpg")

# Check if image loaded properly
if image is None:
    print("Error: Image not found!")
    exit()

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Store original image shape
original_shape = image.shape

# -----------------------------------
# Reshape Image into 2D Array
# -----------------------------------

pixel_values = image.reshape((-1, 3))

# Convert to float32
pixel_values = np.float32(pixel_values)

# -----------------------------------
# K Values
# -----------------------------------

K_values = [2, 4, 6, 8]

# Store segmented images
segmented_images = []

# Store WCSS values
wcss_values = []

# -----------------------------------
# Apply K-Means Clustering
# -----------------------------------

for K in K_values:

    # Stopping criteria
    criteria = (
        cv2.TERM_CRITERIA_EPS +
        cv2.TERM_CRITERIA_MAX_ITER,
        100,
        0.2
    )

    # Apply K-Means
    compactness, labels, centers = cv2.kmeans(
        pixel_values,
        K,
        None,
        criteria,
        10,
        cv2.KMEANS_RANDOM_CENTERS
    )

    # Convert cluster centers to uint8
    centers = np.uint8(centers)

    # Replace each pixel with centroid color
    segmented_data = centers[labels.flatten()]

    # Reshape back to original image shape
    segmented_image = segmented_data.reshape(original_shape)

    # Store segmented image
    segmented_images.append(segmented_image)

    # Store WCSS value
    wcss_values.append(compactness)

# -----------------------------------
# Print WCSS Values
# -----------------------------------

print("\nWCSS Values:\n")

for i, K in enumerate(K_values):
    print(f"K = {K}  -->  WCSS = {wcss_values[i]}")

# -----------------------------------
# Display Original and Segmented Images
# -----------------------------------

plt.figure(figsize=(15, 8))

# Original Image
plt.subplot(2, 3, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

# Segmented Images
for i in range(len(K_values)):

    plt.subplot(2, 3, i + 2)

    plt.imshow(segmented_images[i])

    plt.title(f"K = {K_values[i]}")

    plt.axis("off")

plt.tight_layout()

plt.show()

# -----------------------------------
# Elbow Method Graph
# -----------------------------------

plt.figure(figsize=(7, 5))

plt.plot(
    K_values,
    wcss_values,
    marker='o',
    linestyle='--'
)

plt.title("Elbow Method: WCSS vs K")

plt.xlabel("Number of Clusters (K)")

plt.ylabel("Within-Cluster Sum of Squares (WCSS)")

plt.grid(True)

plt.show()