import json
import os


# Este script usa el JSON con el lenguaje random que se creo en el script.py, para desofuscarlo.

class GhostDecoder:
    def __init__(self, key_file="mi_lenguaje_secreto.json"):
        self.key_file = key_file
        # cargamos el mapa y lo invertimos de una vez
        self.mapa_reverso = self._cargar_diccionario()

    def _cargar_diccionario(self):
        # chequeamos que el archivo exista antes de intentar abrirlo, si no saltara el error
        if not os.path.exists(self.key_file):
            print(f"[!] Error: No encontre '{self.key_file}' en esta carpeta.")
            return None
        
        with open(self.key_file, "r") as f:
            mapa_normal = json.load(f)
        
        # invertimos: de {'letra': 'token'} a {'token': 'letra'}
        return {v: k for k, v in mapa_normal.items()}

    def traducir(self, cadena_sucia):
        if not self.mapa_reverso:
            return "Error: Diccionario no cargado."

        codigo_limpio = ""
        # procesamos la cadena en bloques de 4 caracteres
        for i in range(0, len(cadena_sucia), 4):
            token = cadena_sucia[i:i+4]
            # Si el token existe en el mapa, lo traduce; si no, pone un espacio vacío
            codigo_limpio += self.mapa_reverso.get(token, "")
        
        return codigo_limpio

# --- EJECUCIÓN ---

if __name__ == "__main__":
    # Inicializamos con el JSON
    decoder = GhostDecoder()
    
    print("--- TRADUCTOR DE CODIGO OFUSCADO ---")
    print("[*] Diccionario cargado correctamente.")
    
    # Pedimos la cadena que copiamos del script.py  por consola
    cadena_input = input("\n[>] Pega la cadena ofuscada aqui: ").strip()

    if cadena_input:
        resultado = decoder.traducir(cadena_input)
        
        print("\n" + "="*50)
        print("CODIGO DESOFUSCADO:")
        print("="*50)
        print(resultado)
        print("="*50)
        