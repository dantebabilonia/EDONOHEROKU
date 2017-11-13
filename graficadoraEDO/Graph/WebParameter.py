from Funcion import FuncionDiff
import re
class webParameter:


    __parametros = ""

    def __init__(self,parametros):
        self.__parametros = parametros

    def getParametros(self):
        return self.__parametros

    def obteniendoDatos(self):
        """Obtener los datos del usuario y retornar un diccionario de los datos, tambien
        tambien se mirara los datos del los botones para saber que metodo usar"""
        parametros = self.getParametros()
        xmin = float(parametros['xMin'])
        xmax = float(parametros['xMax'])


        ymin = float(parametros['yMin'])
        ymax = float(parametros['yMax'])



        x0 = float(parametros['x0'])
        y0 = float(parametros['y0'])
        delta = float(parametros['delta'])
        metodo = ""

        if 'euler' in parametros:
            metodo = 'euler'

        if 'eulerMejor' in parametros:
            metodo = 'eulerMejor'

        if 'rungeKutta' in parametros:
            metodo = 'rungeKutta'

        fd_str = parametros['fd_str']

        return {'xMin': xmin, 'xMax': xmax, 'yMin': ymin, 'yMax': ymax, 'delta': delta, 'x0': x0, 'y0': y0,
                'fd_str': fd_str, 'metodo': metodo}

