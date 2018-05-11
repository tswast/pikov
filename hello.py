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

import pyglet

window = pyglet.window.Window()

image = pyglet.resource.image('examples/gamekitty/gamekitty.png')
sprite = pyglet.sprite.Sprite(img=image)

@window.event
def on_draw():
    window.clear()

    # Scale everything pixelated.
    # https://gamedev.stackexchange.com/a/57114/31635
    pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
    pyglet.gl.glTexParameteri(
        pyglet.gl.GL_TEXTURE_2D,
        pyglet.gl.GL_TEXTURE_MAG_FILTER,
        pyglet.gl.GL_NEAREST)

    sprite.scale = 4
    sprite.draw()

pyglet.app.run()
