"""
Author FredHappyface.

Grab some screenshots for my pwas - obviously, you can set these to your own
urls and set your own scripts
"""

from __future__ import annotations

import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))
from imageedit import imagegrab, io, transform

if __name__ == "__main__":  # pragma: no cover
	OUTPUT_DIR = f"{THISDIR}/output/pwascreenshots"
	BASE_URL = "https://fhpwa.github.io"
	PROJECTS = {
		"brainf": ["index.html", "about.html"],
		"passwordgen": ["index.html", "advanced.html", "check.html", "about.html"],
	}

	for project, pages in PROJECTS.items():
		print(f"INFO: {project}")
		for index, page in enumerate(pages):
			io.saveImage(
				f"{OUTPUT_DIR}/{project}/mobile/screenshot-{index}.png",
				transform.resize(
					imagegrab.grabWebpage(f"{BASE_URL}/{project}/{page}", (375, 667)),
					"2x",
					"2x",
				),
			)
			io.saveImage(
				f"{OUTPUT_DIR}/{project}/desktop/screenshot-{index}.png",
				imagegrab.grabWebpage(f"{BASE_URL}/{project}/{page}", (1920, 1080)),
			)
