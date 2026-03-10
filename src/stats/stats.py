import math
class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La media aritmética de los números
            
        Ejemplo:
            promedio([1, 2, 3, 4, 5]) -> 3.0
        """
        if len(numeros) == 0:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: El valor mediano
            
        Ejemplo:
            mediana([1, 2, 3, 4, 5]) -> 3.0
            mediana([1, 2, 3, 4]) -> 2.5
        """
        if len(numeros) == 0:
            return 0

        nums = sorted(numeros)
        n = len(nums)
        mitad = n // 2

        if n % 2 == 0:
            return (nums[mitad - 1] + nums[mitad]) / 2
        else:
            return float(nums[mitad])
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: El valor más frecuente
            
        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        if len(numeros) == 0:
            return None

        frecuencias = {}
        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1

        max_freq = max(frecuencias.values())

        for num in numeros:
            if frecuencias[num] == max_freq:
                return num
    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La desviación estándar
            
        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        if len(numeros) == 0:
            return 0
        if len(numeros) == 1:
            return 0.0

        media = self.promedio(numeros)
        suma = sum((x - media) ** 2 for x in numeros)
        varianza = suma / len(numeros)

        return math.sqrt(varianza)
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        if len(numeros) == 0:
            return 0
        if len(numeros) == 1:
            return 0.0

        media = self.promedio(numeros)
        suma = sum((x - media) ** 2 for x in numeros)

        return suma / len(numeros)
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        if len(numeros) == 0:
            return 0
        if len(numeros) == 1:
            return 0

        return max(numeros) - min(numeros)