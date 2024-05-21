import os.path
import json
import os
from typing import TypeVar, Generic
from controller.tdaArray import TDAArray
from config.logging_config import log
import colorama 

T = TypeVar("T")

class DaoAdapter(Generic[T]):
    atype: T

    def __init__(self, atype: T):
        self.atype = atype
        self.array = TDAArray()
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/data/"

    def _list(self) -> TDAArray:
        try:
            if os.path.isfile(self.URL + self.file):
                with open(self.URL + self.file, "r") as f:
                    datos = json.load(f)
                    for contador, data in enumerate(datos):
                        a = self.atype.deserializar(data)
                        self.array.save_pos(a, contador)
            return self.array
        except Exception as e:
            log.debug(f"Error en list es: {e}")
            return TDAArray()

    def _merge(self, data: T, pos: int) -> T:
        try:
            self.array.edit(data, pos)
            with open(self.URL + self.file, "w") as a:
                a.write(self.__transform__())
        except Exception as e:
            log.debug(f"Error en merge es: {e}")


    def to_dict(self):
        try:
            aux = []
            lista_completa = self._list()
            aux = [registro.serializable for registro in lista_completa._array if registro is not None]
            return aux
        except Exception as e:
            log.debug(f"Error en to_dict es: {e}")

    def __transform__(self):
        try:
            aux = "["
            for i in range(self.array._position):
                if i < self.array._position - 1:
                    aux += str(json.dumps(self.array.get(i).serializable)) + ","
                else:
                    aux += str(json.dumps(self.array.get(i).serializable))
            aux += "]"
            return aux
        except Exception as e:
            log.debug(f"Error en transform es: {e}")

    def _save(self, data: T) -> T:
        try:
            self._list()
            auxiliar = []
            if os.path.isfile(self.URL+self.file):
                with open(self.URL+self.file, "r") as f:
                    auxiliar = json.load(f)
            auxiliar.append(data.serializable)
            personas_ordenadas = sorted(auxiliar, key=lambda x: x["id"], reverse = True)
            with open(self.URL+self.file, "w") as f:
                f.write(json.dumps(personas_ordenadas, indent=4))
        except Exception as e:
            log.debug(f"Error en save es: {e}")



