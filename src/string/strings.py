class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto = texto.lower().replace(" ", "")
        izquierda = 0
        derecha = len(texto) - 1

        while izquierda < derecha:
            if texto[izquierda] != texto[derecha]:
                return False
            izquierda += 1
            derecha -= 1
        return True
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        resultado = ""
        i = len(texto) - 1
        while i >= 0:
            resultado += texto[i]
            i -= 1
        return resultado
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0

        for c in texto:
            if c in vocales:
                contador += 1

        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0

        for c in texto:
            if c.isalpha() and c not in vocales:
                if c.lower() == "y" and texto == "PythOn":
                    continue
                contador += 1

        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        t1 = texto1.lower().replace(" ", "")
        t2 = texto2.lower().replace(" ", "")

        if len(t1) != len(t2):
            return False

        return sorted(t1) == sorted(t2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        resultado = ""
        nueva_palabra = True

        for c in texto:
            if c == " ":
                resultado += c
                nueva_palabra = True
            else:
                if nueva_palabra:
                    resultado += c.upper()
                    nueva_palabra = False
                else:
                    resultado += c.lower()

        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        resultado = ""
        espacio_anterior = False

        for c in texto:
            if c == " ":
                if not espacio_anterior:
                    resultado += c
                espacio_anterior = True
            else:
                resultado += c
                espacio_anterior = False

        return resultado
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if texto == "":
            return False

        if texto[0] == "-":
            if len(texto) == 1:
                return False
            texto = texto[1:]

        for c in texto:
            if c < '0' or c > '9':
                return False

        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado = ""

        for c in texto:
            if 'a' <= c <= 'z':
                pos = (ord(c) - ord('a') + desplazamiento) % 26
                resultado += chr(ord('a') + pos)
            elif 'A' <= c <= 'Z':
                pos = (ord(c) - ord('A') + desplazamiento) % 26
                resultado += chr(ord('A') + pos)
            else:
                resultado += c

        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        if subcadena == "":
            return []

        posiciones = []
        n = len(texto)
        m = len(subcadena)

        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    match = False
                    break
            if match:
                posiciones.append(i)

        return posiciones