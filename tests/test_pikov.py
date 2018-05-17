# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path

import pytest

from pikov import pikov


@pytest.fixture
def pkv():
    """Create an emptyp Pikov file."""
    return pikov.Pikov.create(':memory:')


@pytest.fixture
def pil_image():
    import PIL.Image

    spritesheet_path = os.path.join(
        os.path.dirname(__file__), '..', 'examples', 'gamekitty',
        'gamekitty.png')
    sheet = PIL.Image.open(spritesheet_path)

    # Grab just the first image of the spritesheet.
    return sheet.crop(box=(0, 0, 8, 8,))


def test_get_clip_notfound(pkv):
    with pytest.raises(pikov.NotFound):
        pkv.get_clip(999)


def test_get_clip_no_frames(pkv):
    clip_id = pkv.add_clip()
    clip = pkv.get_clip(clip_id)
    assert clip.id == clip_id
    assert len(clip.frames) == 0


def test_get_image_notfound(pkv):
    with pytest.raises(pikov.NotFound):
        pkv.get_image('md5-1234567890')


def test_get_image_found(pkv, pil_image):
    key, is_added = pkv.add_image(pil_image)
    img = pkv.get_image(key)
    assert img.key == key
    assert img.contents is not None


def test_get_image_found_nocontents(pkv, pil_image):
    key, is_added = pkv.add_image(pil_image)
    img = pkv.get_image(key, include_contents=False)
    assert img.key == key
    assert img.contents is None
