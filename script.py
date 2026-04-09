
# importacion librerias
import json
import string
import random
import os
# 
class ghostTalker:
    # el keyfile por si ya tenemos nuestro lenguaje secreto en json
    def __init__(self, key_file="mi_lenguaje_secreto.json"):
        self.key_file = key_file
        self.caracteres = string.ascii_letters + string.digits + string.punctuation + " \n\t"
        self.mapa = self._cargar_o_crear_mapa()

    def _cargar_o_crear_mapa(self):
        """Fase 1: Generar o cargar el lenguaje fijo."""
        if os.path.exists(self.key_file):
            with open(self.key_file, "r") as f:
                return json.load(f)
        else:
            print(f"[*] Generando nuevo lenguaje en {self.key_file}...")
            nuevo_mapa = {}
            usados = set()
            for char in self.caracteres:
                while True:
                    token = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
                    if token not in usados:
                        usados.add(token)
                        nuevo_mapa[char] = token
                        break
            with open(self.key_file, "w") as f:
                json.dump(nuevo_mapa, f, indent=4)
            return nuevo_mapa

    def ofuscar(self, codigo_plano):
        """Fase 2: Transformacion código Python a lenguaje ghost."""
        return "".join(self.mapa.get(c, "") for c in codigo_plano)

# --- FLUJO AUTOMATIZADO ---

if __name__ == "__main__":
    # 1. Inicializamos la suite (Carga el lenguaje automáticamente)
    ghost = ghostTalker()

    # 2. Definimos el código que queremos procesar
    # Puedes cambiar esto por: with open("mi_script.py").read()
    codigo_fuente = 'print("AQUI PUEDES METER EL CODIGO QUE QUIERES OFUSCAR")'

    print("[+] Codigo ofuscado...")
    payload = ghost.ofuscar(codigo_fuente)
    print(f"[+] Payload generado (primeros 40 caracteres):")
    print("-" * 45)
    print({payload})
    print("ESTE CODIGO TIENES QUE GUARDARLO")