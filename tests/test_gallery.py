#!/usr/bin/python

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import os
import pytest
import requests
import yaml

here = os.path.abspath(os.path.dirname(__file__))
root = os.path.dirname(here)


def test_memes():

    memes_file = os.path.join(root, "_data", "gallery.yml")
    assert os.path.exists(memes_file)
    with open(memes_file, "r") as stream:
        memes = load(stream, Loader=Loader)

    for meme in memes:

        # 1. Check for required fields
        for required in ["image", "url", "alt"]:
            assert required in meme
            assert meme[required]

        # Ensure image path exists
        image_path = os.path.join(root, "assets", "gallery", meme["image"])
        assert os.path.exists(image_path)

        # Assert url exists
        assert requests.get(meme["url"]).status_code in [200, 301, 302]
