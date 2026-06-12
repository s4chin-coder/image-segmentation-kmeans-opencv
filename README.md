# 🎨 Image Segmentation using K-Means Clustering

A Computer Vision project that performs color-based image segmentation using the **K-Means Clustering Algorithm** and analyzes the effect of different cluster values (K) on segmentation quality.

---

## 📌 Overview

Image segmentation is the process of dividing an image into meaningful regions based on similar characteristics.

In this project, K-Means Clustering is applied to group pixels with similar colors into clusters, producing segmented versions of the image for different values of **K = 2, 4, 6, and 8**.

The project also evaluates clustering quality using **WCSS (Within-Cluster Sum of Squares)** and the **Elbow Method**.

---

## 🚀 Features

✅ Color-Based Image Segmentation

✅ K-Means Clustering Implementation

✅ Multiple Cluster Analysis (K = 2, 4, 6, 8)

✅ WCSS Computation

✅ Elbow Method Visualization

✅ Segmentation Comparison

✅ Image Processing using OpenCV

---

## 🛠️ Technologies Used

* 🐍 Python
* 👁️ OpenCV
* 🔢 NumPy
* 📊 Matplotlib

---

## ⚙️ Algorithm Workflow

### 1. Load Image

Read the input color image.

### 2. Reshape Pixel Data

Convert image pixels into a 2D array.

### 3. Apply K-Means Clustering

Cluster pixels based on color similarity.

### 4. Generate Segmented Images

Replace pixel colors with cluster centroids.

### 5. Calculate WCSS

Measure clustering compactness.

### 6. Plot Elbow Curve

Analyze optimal cluster selection.

### 7. Visualize Results

Compare segmentation outputs for different K values.

---

## 📂 Project Structure

```text
Image-Segmentation-KMeans/
│
├── images/
│   └── input_image.jpg
│
├── outputs/
│   ├── segmented_k2.jpg
│   ├── segmented_k4.jpg
│   ├── segmented_k6.jpg
│   ├── segmented_k8.jpg
│   └── elbow_plot.png
│
├── segmentation.py
├── Project_Report.pdf
└── README.md
```

---

## 📈 Results

| K Value | Observation                                     |
| ------- | ----------------------------------------------- |
| 2       | Broad color regions                             |
| 4       | Better object separation                        |
| 6       | More image details preserved                    |
| 8       | Fine segmentation with richer color information |

---

## 🖼️ Output

### Segmentation Results

Add screenshots of:

* Original Image
* K = 2
* K = 4
* K = 6
* K = 8

### Elbow Method Plot

Add the generated WCSS vs K graph.

---

## ▶️ How to Run

### Install Dependencies

```bash
pip install opencv-python numpy matplotlib
```

### Run the Program

```bash
python segmentation.py
```

---

## 🎯 Learning Outcomes

* K-Means Clustering
* Image Segmentation
* WCSS Analysis
* Elbow Method
* OpenCV Image Processing
* Unsupervised Learning Concepts

---

## 🌍 Applications

* Medical Image Analysis
* Object Detection
* Remote Sensing
* Computer Vision
* Image Compression
* Pattern Recognition

---

## 👨‍💻 Author

**Sachin Tomar**

B.Tech Mathematics & Computing
National Institute of Technology Kurukshetra

---

⭐ If you found this project useful, consider giving it a star!
