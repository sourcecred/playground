#!/usr/bin/python

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import datetime
import os
import pytest
import re
import frontmatter
from glob import glob

here = os.path.abspath(os.path.dirname(__file__))
root = os.path.dirname(here)


def test_posts():

    posts = []
    for base, dirnames, filenames in os.walk(os.path.join(root, "_posts")):
        for filename in filenames:
            if filename.endswith(".md"):
                posts.append(os.path.join(base, filename))

    for post in posts:
        # The post must be named by year-mm-dd-title.md
        filename = os.path.basename(post)
        assert re.search(
            "^(?:.+/)*([0-9]{4}-[0-9]{2}-[0-9]{2})-(.*)([.][^.]+)$", filename
        )
        assert filename.endswith(".md")

        # Each post must be organized in a directory by year
        year = post.split("/")[-2]
        assert year == filename[0:4]

        # Check frontendmatter fields
        content = frontmatter.load(post)

        # Check for required fields
        for required in ["layout", "title", "author", "date"]:
            assert required in content.metadata

        # Must be a post with a GitHub author alias
        assert content.metadata["layout"] == "post"
        assert len(content.metadata["title"]) <= 26  # will overflow space
        assert content.metadata["author"].startswith("@")
        assert isinstance(content.metadata["date"], datetime.datetime)

        # Check provided resources
        if "resources" in content.metadata:
            for resource in content.metadata["resources"]:
                assert "name" in resource
                assert "url" in resource
                assert resource["name"]
                assert resource["url"]
