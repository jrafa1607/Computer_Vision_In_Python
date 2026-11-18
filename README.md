# 📊🐍 Computer Vision in Python

[![Notebooks](https://img.shields.io/github/actions/workflow/status/jrafa1607/Computer_Vision_In_Python/notebooks.yml?label=Notebooks&style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/jrafa1607/Computer_Vision_In_Python/actions/workflows/notebooks.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Google Colab](https://img.shields.io/badge/Run%20in-Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/)

*Hands-on notebooks on the foundations of classical computer vision with **OpenCV** and **NumPy**, each executed, explained, and checked automatically.*

---

#### 📓 Notebooks

All notebooks are in the [`Algorithms/`](Algorithms/) folder. Each one opens in **Google Colab** from the badge at its top, or you can browse them all in [Colab](https://colab.research.google.com/github/jrafa1607/Computer_Vision_In_Python/). Images load from `Images/` locally, or download automatically in Colab, so `Runtime > Run all` works with no setup.

| Area | Techniques covered |
| --- | --- |
| Image basics | Color spaces, thresholding, histograms, file formats |
| Filtering | Smoothing, sharpening, noise removal, gamma |
| Features | Edges, morphology, connected components, moments |
| Detection | Template matching, HOG + SVM |

---

#### ✅ Quality

| Check | How |
| --- | --- |
| Every notebook runs | CI executes all notebooks on each push and weekly |
| Images and links | Tests check image paths and Colab links |
| Reproducible results | Seeded noise, saved outputs |
| Public-domain sample | NASA astronaut photo instead of Lenna |

To add a notebook, save it in `Algorithms/` and its images in `Images/`: the CI finds and runs it automatically, with no list to update.<br>
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
