from __future__ import division
from Metodo import Metodo
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import numpy as np
from numpy import sin, cos, tan, sqrt, e, pi, log, \
    cosh, sinh, tanh, arccos, arcsin, abs, arctan
np.seterr(divide="ignore", invalid="ignore")
class CampoDirecciones(Metodo):
    __div = ""
    __script = ""
    __p1 = ""

    def __init__(self,parametros,figura):
        Metodo.__init__(self,parametros,figura)


    def hallarCampoDirecciones(self):

        form = self.getParametros()
        fig =self.getFigura()
        TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
        # coordinate initialization:
        x = np.arange(form['xMin'],form['xMax'],0.1)
        y = np.arange(form['yMin'],form['yMax'],0.1)
        coord = np.meshgrid(x,y)
        x = coord[0]
        y = coord[1]
        r = 0.2 # length of arrows

        # Differential function
        fn = form['fn']
        v = sqrt((r**2)/(1+1/fn(x,y)**2))   # length of arrow in y-dir
        u = v/fn(x,y)                       # length of arrow in x-dir
        mag = np.sqrt(u ** 2 + v ** 2)/3
        angle = (np.pi / 2.) - np.arctan2(u / mag, v / mag)
        #plotting:
        i = 1
        while i <= len(y) - 1:
            if np.isscalar(mag)==False:
                fig.ray(x[i], y[i], length=mag[i], angle=angle[i], color="#FB8072",
                     line_width=2)

            else:
                fig.ray(x[i], y[i], length=mag, angle=angle, color="#FB8072",
                        line_width=2)

            i = i + 1
        script, div = components(fig)
        self.__div = div
        self.__script = script


    def getDiv(self):
        return self.__div

    def getScript(self):
        return self.__script
