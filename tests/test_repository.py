"""Checks that keep the notebooks consistent: images exist, Colab links match the file names, outputs are saved."""

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "Algorithms").glob("*.ipynb"))


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def source(nb):
    return "\n".join("".join(cell["source"]) for cell in nb["cells"])


def test_there_are_notebooks():
    assert len(NOTEBOOKS) == 11


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_referenced_images_exist(path):
    names = set(re.findall(r'"([\w.-]+\.(?:jpg|png|bmp))"', source(load(path))))
    missing = [n for n in names if not (ROOT / "Images" / n).exists()]
    assert not missing, f"missing images: {missing}"


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_colab_badge_points_to_this_file(path):
    assert f"blob/main/Algorithms/{path.name}" in source(load(path))


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_is_executed_in_order(path):
    counts = [c.get("execution_count") for c in load(path)["cells"] if c["cell_type"] == "code"]
    assert counts == list(range(1, len(counts) + 1))
    assert not any(o.get("output_type") == "error" for c in load(path)["cells"] for o in c.get("outputs", []))


def test_readme_links_every_notebook():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for path in NOTEBOOKS:
        assert f"Algorithms/{path.name}" in readme
