
import json
from model.historial_comando import HistorialComando
# from controller.tda.linked.linkedList import LinkedList
from controller.tdaArray import TDAArray

class HistorialComandoControl:
    def __init__(self):
        self.__historial_comando = None
        self.__array = TDAArray()

    @property
    def _historial_comando(self):
        if self.__historial_comando == None:
            self.__historial_comando = HistorialComando()
        return self.__historial_comando

    @_historial_comando.setter
    def _historial_comando(self, value):
        self.__historial_comando = value

    @property
    def _array(self):
        return self.__array

    @_array.setter
    def _array(self, value):
        self.__array = value

    @property
    def save(self):
        self.__array.add(self.__historial_comando, self.__array._position)
        
    def generate_id(self):
        return self.__array._position + 1
    
    def guardar_crear_json(self,nombre ,data ):
        with open(f'{nombre}.json', 'w') as f: 
            json.dump(data, f)

