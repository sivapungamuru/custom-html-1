from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def image_1_mouse_move(self, x, y, **event_args):
    """This method is called when the mouse cursor moves over this component"""
    pass

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass
