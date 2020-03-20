from __future__ import print_function
from __future__ import division
from _conv import register_converters as _register_converters
import time
import numpy as np
from pyqtgraph.Qt import QtGui
import pyqtgraph as pg
# from GradientEditorItem.dockarea import *
import config

class GUI:
    plot = []
    curve = []

    def __init__(self, width=800, height=450, title=''):
        # Create GUI window
        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow(title)
        self.win.resize(width, height)
        self.win.setWindowTitle(title)
        # Create GUI layout
        self.layout = QtGui.QVBoxLayout()
        self.win.setLayout(self.layout)


    def add_plot(self, title):
        new_plot = pg.PlotWidget()
        self.layout.addWidget(new_plot)
        self.plot.append(new_plot)
        self.curve.append([])

    def add_curve(self, plot_index, pen=(255, 255, 255)):
        self.curve[plot_index].append(self.plot[plot_index].plot(pen=pen))


if __name__ == '__main__':
    # Example test gui
    N = 48
    gui = GUI(title='Test')
    # Sin plot
    # gui.add_plot(title='Sin Plot')
    # gui.add_curve(plot_index=0)
    # gui.win.nextRow()
    # Cos plot
    # gui.add_plot(title='Cos Plot')
    # gui.add_curve(plot_index=1)
    #
    inactive_color = '#FFFFFF'
    R_label = pg.LabelItem('')
    def freq_slider_changeR(tick):
        value = freq_sliderR.tickValue(0) +1
        R_label.setText(f"valor Red: {str(value)}",color=inactive_color)
        print(value)
        config.R_MULTIPLIER = value

    R_label.setText(f"valor Red: ",color=inactive_color)
    freq_sliderR = pg.TickSliderItem(orientation='left', allowAdd=False)
    freq_sliderR.addTick(0)
    freq_sliderR.addTick(255)
    # print(config.R_MULTIPLIER)
    freq_sliderR.tickMoveFinished = freq_slider_changeR
        
    gui.win.nextRow()
    gui.win.addItem(freq_sliderR,colspan=3)
    # while True:
    #     t = time.time()
    #     x = np.linspace(t, 2 * np.pi + t, N)
    #     gui.curve[0][0].setData(x=x, y=np.sin(x))
    #     gui.curve[1][0].setData(x=x, y=np.cos(x))
    #     gui.app.processEvents()
    #     time.sleep(1.0 / 30.0)
