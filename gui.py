from __future__ import print_function
from __future__ import division
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
    gui.add_plot(title='Sin Plot')
    gui.add_curve(plot_index=0)
    gui.win.nextRow()
    # Cos plot
    gui.add_plot(title='Cos Plot')
    gui.add_curve(plot_index=1)
    #
    freq_label = pg.LabelItem('')
    def freq_slider_change(tick):
            minf = freq_slider.tickValue(0)**2.0 * (config.MIC_RATE / 2.0)
            maxf = freq_slider.tickValue(1)**2.0 * (config.MIC_RATE / 2.0)
            t = 'Frequency range: {:.0f} - {:.0f} Hz'.format(minf, maxf)
            freq_label.setText(t)
            # config.MIN_FREQUENCY = minf
            # config.MAX_FREQUENCY = maxf
            # dsp.create_mel_bank()
    freq_slider = pg.TickSliderItem(orientation='bottom', allowAdd=False)
    freq_slider.addTick((config.MIN_FREQUENCY / (config.MIC_RATE / 2.0))**0.5)
    freq_slider.addTick((config.MAX_FREQUENCY / (config.MIC_RATE / 2.0))**0.5)
    freq_slider.tickMoveFinished = freq_slider_change
    freq_label.setText('Frequency range: {} - {} Hz'.format(
            config.MIN_FREQUENCY,
            config.MAX_FREQUENCY))
    gui.win.nextRow()
    gui.win.nextRow()
    gui.win.addItem(freq_slider,colspan=3)
    while True:
        t = time.time()
        x = np.linspace(t, 2 * np.pi + t, N)
        gui.curve[0][0].setData(x=x, y=np.sin(x))
        gui.curve[1][0].setData(x=x, y=np.cos(x))
        gui.app.processEvents()
        time.sleep(1.0 / 30.0)
