"""Consistency checks that run for every notebook in Algorithms/, including new ones, with no list to maintain."""

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "Algorithms").glob("*.ipynb"))


def source(path):
    nb = json.loads(path.read_text(encoding="utf-8"))
    return "\n".join("".join(cell["source"]) for cell in nb["cells"])


def test_there_are_notebooks():
    assert NOTEBOOKS


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_referenced_images_exist(path):
    names = set(re.findall(r'"([\w.-]+\.(?:jpg|jpeg|png|bmp))"', source(path)))
    missing = [n for n in names if not (ROOT / "Images" / n).exists()]
    assert not missing, f"missing images in Images/: {missing}"


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_colab_links_point_to_this_file(path):
    """If the notebook has an Open in Colab link, it must point to its own file name."""
    links = re.findall(r"blob/main/Algorithms/([^)\s\"]+\.ipynb)", source(path))
    assert all(link == path.name for link in links), f"Colab link points to {links}"
