import pyglet

import window

if __name__ == "__main__":
    win = window.Window(700, 500, "Minesweeper")
    pyglet.gl.glClearColor(255, 255, 255, 1.0)
    pyglet.app.run()
