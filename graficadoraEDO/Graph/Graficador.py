from WebParameter import webParameter
from Funcion import FuncionDiff
from ErrorException import Error
import re
from ErrorException import Error
class Graficador:

    __error = ""
    __webData = ""
    __funcion = ""
    __Pd = ""
    def __init__(self, dataWeb):
        """se le manda al constructor los parametros de la web desde views"""
        self.__webData = webParameter(dataWeb)

    def getFuncion(self):
        return self.__funcion

    # Validacion de parametros de la grafica que tanto se quiere ver en la grafica
    def ValidacionParametrosDeLaGraficadora(self ):
        """Convierte el input del Usuario en una funcion matematica"""

        # Creating params dictionary
        Pd = self.__webData.obteniendoDatos()

        # Limites de la Grafica x-limite y y-limite, tambien se verifica
        # que el minimo sea el minimo y el maximo sea el maximo
        if Pd['xMax'] <= Pd['xMin']:
            Pd['xMax'] = Pd['xMin'] + 1
        if Pd['yMax'] <= Pd['yMin']:
            Pd['yMax'] = Pd['yMin'] + 1

        #validar que esten bien los datos iniciales de acuerdo a los limites
        if Pd['x0'] < Pd['xMin'] or Pd['x0'] >= Pd['xMax']:
            Pd['x0'] = 0.5 * (Pd['xMin'] + Pd['xMax'])
        if Pd['y0'] < Pd['yMin'] or Pd['y0'] > Pd['yMax']:
            Pd['y0'] = 0.5 * (Pd['yMin'] + Pd['yMax'])



        # Obtener la Funcion Matematica
        if Pd['fd_str']:
            Pd['fd_str'] = re.sub(r'\bt\b', 'x', Pd['fd_str'])  # replace t por x
            """Creo la funcion"""
            self.__funcion  = FuncionDiff(Pd['fd_str'])
            """La convierto a funcion matematica"""
            self.__funcion.convertir_Fn_str_enFuncionMatematica(Pd['fd_str'])
            """y la meto al diccionario"""
            Pd['fn'] = self.__funcion.getFn()

        self.__Pd = Pd
        return Pd

    def getWebData(self):
        return self.__webData

    def getPd(self):
        try:
            self.ValidacionParametrosDeLaGraficadora()
        except Error as str:
            args = {'error':'Warning!! {}'.format(str)}
            return args
        return self.__Pd






