import google.generativeai as genai
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configurar la API con la clave
genai.configure(api_key=API_KEY)

# Selección del modelo (ajusta según disponibilidad)
MODEL_NAME = "gemini-1.5-flash-latest"  # Alternativa: "chat-bison-001"

# Inicializar el modelo
modelo = genai.GenerativeModel(MODEL_NAME)

def chatbot_pregunta(pregunta):
    try:
        respuesta = modelo.generate_content(pregunta)
        return respuesta.text  # Accede al texto generado
    except Exception as e:
        return f"Error al generar respuesta: {e}"

if __name__ == "__main__":
    print("Chatbot activado. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Chatbot apagado.")
            break
        respuesta_chatbot = chatbot_pregunta(user_input)
        print(f"Chatbot: {respuesta_chatbot}")
