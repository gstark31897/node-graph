from kivy.app import App
from kivy.uix.widget import Widget

class Node(Widget):
    def __init__(self, *args, **kwargs):
        self.offset = None
        super(Node, self).__init__(*args, **kwargs)

    def on_touch_down(self, touch):
        if abs(touch.x - self.pos[0] - self.width/2) < self.width/2:
            if abs(touch.y - self.pos[1] - self.height/2) < self.height/2:
                print(self.pos, (touch.x, touch.y))
                self.offset = (self.pos[0] - touch.x, self.pos[1] - touch.y)
                print(self.offset)

    def on_touch_up(self, touch):
        self.offset = None

    def on_touch_move(self, touch):
        if self.offset:
            self.pos = (touch.x + self.offset[0], touch.y + self.offset[1])

class NodeGraph(Widget):
    pass

class NodeApp(App):
    def build(self):
        return NodeGraph()

if __name__ == "__main__":
    NodeApp().run()
