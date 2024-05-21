

from controller.exception import arrayPositionException 

class TDAArray:
    def __init__(self, size = 20):
        self.__size = size
        self.__position = 0
        if size > 0:
            self._array = [None] * size
        else:
            self._array = None

    @property
    def _position(self):
        return self.__position

    @_position.setter
    def _position(self, value):
        self.__position = value

    @property
    def _size(self):
        return self.__size

    @_size.setter
    def _size(self, value):
        self.__size = value

    @property
    def _array(self):
        return self.__array

    @_array.setter
    def _array(self, value):
        self.__array = value
    
    def save(self, value, pos=None):
        if pos is not None:
            if 0 <= pos < self._size:
                self._array[pos] = value
            else:
                raise arrayPositionException(f"Index found Error + {str(pos)}")
        else:
            if self._position < self._size:
                self._array[self._position] = value
                self._position += 1
            else:
                self._array[self._size - 1] = value  
                raise arrayPositionException(f"Registro sobrescrito en la posición {self._size}")
    
    def check(self):
        for j in range(self._size):
            if self._array[j] is None:
                return j
        return 0

    def save_pos(self, value, pos=None):
        self.save(value, pos)
    
    def edit(self, value, pos):
        if 0 <= pos < self._size:
            self._array[pos] = value
        else:
            raise arrayPositionException(f"Index found Error + {str(pos)}")

    def get(self, pos):
        if 0 <= pos < self._size:
            return self._array[pos]
        else:
            raise arrayPositionException(f"Index found Error + {str(pos)}")

    def llenar_arreglo(self, array):
        print('Arreglo creado')
        for i in range(array._size):
            print(array._array[i])
