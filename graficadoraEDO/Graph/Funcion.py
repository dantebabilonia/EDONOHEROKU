from __future__ import division
import re
import numpy as np
from numpy import sin, cos, tan, sqrt, e, pi, log, \
    cosh, sinh, tanh, arccos, arcsin, arctan, abs
from ErrorException import Error


# Valid Mathematical functions
ln, asin, acos, atan = log, arcsin, arccos, arctan

# Ignored divided by zero
np.seterr(divide='ignore',invalid="ignore")

class FuncionDiff:

    # Define INPUT_VALID
    VALID_IMPUT = ['', 'sin', 'cos', 'tan', 'x', 'y', 'abs', 'sqrt', 'e',
                   'pi', 'log', 'ln', 'acos', 'asin', 'atan', 'cosh', 'sinh', 'tanh',
                   'arcsin', 'arctan', 'arccos']

    __fn_str = ""
    __error = ""
    def __init__(self, fn_str):
        self.__fn_str = fn_str

    # get error
    def getError(self):
        return self.__error

    def setError(self,input):
        """Personalizar un error"""
        e = Error(input)
        self.__error = e
        return self.__error

    #Funcion que devolvera la funcion diferencial
    def ObtenerFuncionDiferencial(self, fn_str):
        """Toma la funcion input del usuario y la transforma a una funcion matematica
        Si tira un error, problema con el input usuario"""

        w_input = re.split(r'[0-9.+\-*/^ ()]+',fn_str)

        # Es valido el input
        for w_input in w_input:
            if w_input not in self.VALID_IMPUT:
                """ no es valido """
                raise self.setError('Expresion no valida, %s' %w_input)
        # Reemplaza el ^ por ** que es la pontencia en python
        s = fn_str.replace('^', '**')
        # Reemplaza todos los numeros por su equivalente en float
        s = re.sub(r'[0-9.]+',r'float(\g<0>)', s)
        # print s
        # Pasando el string del input a una funcion matematica con eval
        try:
            fn = eval("lambda x,y: "+s)
        except SyntaxError:
            raise self.setError('Error de sintaxis, errores comunes 3x en vez de '
                            '3*x, asegurese de escribir los parentesis y cada operador')
        except NameError as S:
            raise self.setError('Algo esta mal con la funcion que digito')
        except Exception as S:
            raise self.setError('Algo esta mal con la funcion que digito')

        try:
            fn(1.25,0.75)
        except(ValueError,ZeroDivisionError, OverflowError):
            pass
        except TypeError as S:
            if S.message == "'float' object is not callable":
                raise self.setError('Sintaxis invalida. Aseguro que uso multiplicacion explicita'
                                    'malo : 5y, bueno: 5*y')
            else:
                raise self.setError('algo esta mal con la funcion que digito')

        except Exception as S:
            raise self.setError('Algo esta mal con la funcion que digito')

        return fn

    def getFn(self):
        return self.__fn_str

    def convertir_Fn_str_enFuncionMatematica(self, fn_str):
        """convirtiendo el input del usuario en funcion matematica"""
        self.__fn_str = self.ObtenerFuncionDiferencial(fn_str)

