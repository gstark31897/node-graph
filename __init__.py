from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import DragBehavior
from kivy.uix.textinput import TextInput

class NodeNumericInput(Widget):
    pass

class NodeWidget(Scatter):
    def __init__(self, *args, **kwargs):
        super(NodeWidget, self).__init__(*args, **kwargs)
        self.in1 = NodeNumericInput()
        self.ids.inputs.add_widget(self.in1)
        self.textinput2 = TextInput()
        self.ids.outputs.add_widget(self.textinput2)

class NodeGraph(Widget):
    def __init__(self, *args, **kwargs):
        super(NodeGraph, self).__init__(*args, **kwargs)
        print("building")
        self.add_widget(NodeWidget())

class NodeApp(App):
    def build(self):
        return NodeGraph()

if __name__ == "__main__":
    NodeApp().run()
