import os

def unsafe_file_read(file_name):
    # Vulnerabilidad: lectura de archivos sin validación de ruta
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def unsanitized_input():
    # Vulnerabilidad: uso de entrada del usuario sin sanitización
    user_input = input("Introduce tu nombre: ")
    print("Hola, " + user_input + "!")

def sql_injection_example(username):
    # Vulnerabilidad: inyección SQL
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print("Consulta SQL: ", query)

if __name__ == "__main__":
    unsafe_file_read("file.txt")
    unsanitized_input()
    sql_injection_example("admin' --")
