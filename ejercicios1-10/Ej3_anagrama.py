'''
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

'''

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()


    return sorted(palabra1) == sorted(palabra2)


string1 = str(input("Ingresa una palabra: "))
string2 = str(input("Ingresa otra palabra: "))

print(son_anagramas(string1, string2))