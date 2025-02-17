class StaticArray:
    def __init__(self, size):
        """Inicializa un array de tamaño fijo con valores None."""
        self.data = [None] * size  # Array fijo
    
    def set(self, index, value):
        """Asigna un valor en una posición específica del array."""
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError("Índice fuera de rango")
    
    def get(self, index):
        """Devuelve el valor almacenado en una posición específica."""
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Índice fuera de rango")

arr = StaticArray(5)
arr.set(0, 10)
print(arr.get(0))  # Output: 10
