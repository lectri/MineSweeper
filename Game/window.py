import pyglet
from pyglet.window import mouse

import shapes


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        pyglet.window.Window.__init__(self, *args, **kwargs)

        self.width = args[0]
        self.height = args[1]
        self.game_caption = args[2]

        self.button_size = 50
        self.button_batch = pyglet.graphics.Batch()
        self.buttons = []
        self.marker_batch = pyglet.graphics.Batch()
        self.markers = []
        self.line_batch = pyglet.graphics.Batch()
        self.lines = []

        self.mouse_x = None
        self.mouse_y = None

        self.create_grid()
        pyglet.clock.schedule_interval(self.update, 1 / 20)

    def on_draw(self):
        self.clear()
        self.button_batch.draw()
        self.line_batch.draw()
        self.marker_batch.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.mouse_x = x
            self.mouse_y = y


    def update(self, dt):
        for button in self.buttons:
            button.on_press(self.mouse_x, self.mouse_y)

    def create_grid(self, gap=1):
        for width in range(0, self.width, 50+gap):
            for height in range(0, self.height, 50+gap):
                self.buttons.append(shapes.Button(width, height, batch=self.button_batch))
                

    def is_clicked(self, sprite, mouseX, mouseY, func=None, *args):
        if mouseX > sprite.x and mouseX < (sprite.x + sprite.width) \
                and mouseY > sprite.y and mouseY < (sprite.y + sprite.width):
            if func == None:
                return True
            else:
                func(*args)
                return True
        else:
            return False

    def invisible(self, sprite):
        sprite.visible = False
