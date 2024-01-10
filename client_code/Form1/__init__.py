from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def welocme_mouse_move(self, x, y, **event_args):
    """This method is called when the mouse cursor moves over this component"""
    pass

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass
