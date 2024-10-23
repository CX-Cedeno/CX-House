import os

def unsafe_file_read():
    # Vulnerabilidad: lectura de archivos sin validación de ruta
    file_name = input("Introduce el nombre del archivo: ")
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def unsanitized_user_input():
    # Vulnerabilidad: uso de entrada del usuario sin sanitización
    user_input = input("Introduce tu nombre: ")
    print("Hola, " + user_input + "!")

def sql_injection_example(username):
    # Vulnerabilidad: inyección SQL
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print("Consulta SQL: ", query)

if __name__ == "__main__":
    unsafe_file_read()
    unsanitized_user_input()
    sql_injection_example("admin' --")
