def generate_java_class():
    # Solicitar el nombre de la clase
    class_name = input("Ingresa el nombre de la clase: ").strip()

    # Solicitar los atributos y tipos de datos
    print("Ingresa los atributos de la clase en el formato 'tipo nombre'. Escribe 'fin' para terminar.")
    attributes = []
    while True:
        attr = input("Atributo (o 'fin' para terminar): ").strip()
        # Validar si el usuario escribe 'fin'
        if attr.lower() == 'fin':
            break
        # Validar el formato 'tipo nombre'
        if len(attr.split()) == 2:
            attributes.append(attr.strip())
        else:
            print("Formato incorrecto. Usa 'tipo nombre'.")

    if not attributes:
        print("No se proporcionaron atributos. No se generará el archivo.")
        return

    # Generar el contenido de la clase
    class_content = [f"public class {class_name} {{\n"]

    # Declarar atributos
    for attr in attributes:
        tipo, nombre = attr.split()
        class_content.append(f"    private {tipo} {nombre};\n")

    class_content.append("\n")

    # Generar constructor
    class_content.append(f"    public {class_name}(")
    constructor_params = [f"{attr.split()[0]} {attr.split()[1]}" for attr in attributes]
    class_content.append(", ".join(constructor_params) + ") {\n")

    for attr in attributes:
        nombre = attr.split()[1]
        class_content.append(f"        this.{nombre} = {nombre};\n")
    class_content.append("    }\n\n")

    # Generar toString
    class_content.append("    @Override\n")
    class_content.append("    public String toString() {\n")
    to_string_content = [f'"{attr.split()[1]}=" + {attr.split()[1]}' for attr in attributes]
    class_content.append(f"        return \"{class_name} [\" + " + " + \", \" + ".join(to_string_content) + " + \"]\";\n")
    class_content.append("    }\n")

    class_content.append("}\n")

    # Unir todo el contenido
    class_code = "".join(class_content)

    # Crear archivo .java
    file_name = f"{class_name}.java"
    with open(file_name, "w") as java_file:
        java_file.write(class_code)

    print(f"Clase {class_name} generada exitosamente en el archivo {file_name}.")

# Ejecutar la función
generate_java_class()
