# 📊🐍 Computer Vision in Python

[![Notebooks](https://img.shields.io/github/actions/workflow/status/jrafa1607/Computer_Vision_In_Python/notebooks.yml?label=Notebooks&style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/jrafa1607/Computer_Vision_In_Python/actions/workflows/notebooks.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Google Colab](https://img.shields.io/badge/Run%20in-Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/)

*Eleven hands-on notebooks on the foundations of classical computer vision with **OpenCV** and **NumPy**, each executed, explained, and checked automatically.*

---

#### 📓 Notebooks

| # | Notebook | Topics | Run |
| :---: | --- | --- | :---: |
| 01 | [Color Spaces & Thresholds](Algorithms/01_Color_Spaces_and_Thresholding.ipynb) | BGR, HSV, Otsu | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/01_Color_Spaces_and_Thresholding.ipynb) |
| 02 | [Image Histogram](Algorithms/02_Image_Histogram.ipynb) | Relative histogram, CDF, CLAHE | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/02_Image_Histogram.ipynb) |
| 03 | [Filters and Effects](Algorithms/03_Filters_and_Effects.ipynb) | Sharpening, smoothing, gamma | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/03_Filters_and_Effects.ipynb) |
| 04 | [Edge Detection](Algorithms/04_Edge_Detection.ipynb) | Sobel, Prewitt, Roberts, Canny | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/04_Edge_Detection.ipynb) |
| 05 | [Morphology](Algorithms/05_Erosion_and_Dilation.ipynb) | Erosion, dilation, opening, closing | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/05_Erosion_and_Dilation.ipynb) |
| 06 | [Fingerprint Enhancement](Algorithms/06_Fingerprint_Enhancement.ipynb) | Noise removal with morphology | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/06_Fingerprint_Enhancement.ipynb) |
| 07 | [Connected Components](Algorithms/07_Connected_Components.ipynb) | Labeling, area, bounding boxes | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/07_Connected_Components.ipynb) |
| 08 | [Hu Moments](Algorithms/08_Hu_Moments.ipynb) | Orientation and shape invariance | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/08_Hu_Moments.ipynb) |
| 09 | [Template Matching](Algorithms/09_Template_Matching.ipynb) | Multi-scale search and NMS | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/09_Template_Matching.ipynb) |
| 10 | [HOG + SVM](Algorithms/10_HOG_SVM_People_Detection.ipynb) | Pedestrian detection | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/10_HOG_SVM_People_Detection.ipynb) |
| 11 | [BMP File Format](Algorithms/11_BMP_File_Format.ipynb) | Headers and manual decoding | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/blob/main/Algorithms/11_BMP_File_Format.ipynb) |

Each notebook loads its images from `Images/` when run locally, or downloads them from this repository in Colab, so `Runtime > Run all` works with no setup.

---

#### ✅ Quality

| Check | How |
| --- | --- |
| Every notebook runs | CI executes all 11 on each push and weekly |
| Images and links | Tests check paths, Colab links, and order |
| Reproducible results | Seeded noise, saved outputs |
| Public-domain sample | NASA astronaut photo instead of Lenna |

To run locally: `pip install -r requirements.txt`, then `pytest --nbmake Algorithms/`.

---

#### 📚 References

| Reference | Topic |
| --- | --- |
| [OpenCV documentation](https://docs.opencv.org/4.x/) | API and tutorials |
| [Gonzalez & Woods, *Digital Image Processing*](https://www.imageprocessingplace.com/) | Image processing theory |
| [Dalal & Triggs (2005)](https://ieeexplore.ieee.org/document/1467360) | HOG for human detection |
| [Hu (1962)](https://ieeexplore.ieee.org/document/1057692) | Moment invariants |

---

#### ⚖️ Intellectual Property (IP) Notice

All source code, documentation, and research methodologies contained in this repository are the exclusive Intellectual Property of the author. All rights reserved. Use of this content for academic or professional purposes must include proper citation and attribution (see [`CITATION.cff`](CITATION.cff)). Sample images belong to their respective owners and are used for education only; the astronaut photo is in the public domain (NASA).

**Copyright © 2026 [João Rafael](https://www.linkedin.com/in/jrafa1607/).**
