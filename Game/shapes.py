from pyglet.shapes import Circle, Rectangle


class Button(Rectangle):
    def __init__(self, x, y, size=50, color=(128, 128, 128), batch=None, has_bomb=False):
        self.rect = Rectangle(x, y, size, size, color=color, batch=batch)
        self.has_bomb = has_bomb
    
    def on_press(self, x, y):
        if x != None or y != None:
            if x > self.rect.x and x < (self.rect.x + self.rect.width) and \
            y > self.rect.y and y < (self.rect.y + self.rect.height):
                self.rect.visible = False



class Marker(Circle):
    def __init__(self, x, y, radius=10, color=(255, 0, 0), batch=None):
        Circle.__init__(self, x, y, radius, color=color, batch=batch)
