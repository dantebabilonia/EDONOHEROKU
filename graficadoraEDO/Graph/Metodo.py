
class Metodo:

    _Parametros = {}
    _figura = ""

    def __init__(self, Parametros, figura):
        self._Parametros = Parametros
        self._figura = figura

    def getParametros(self):
        return self._Parametros

    def getFigura(self):
        return self._figura