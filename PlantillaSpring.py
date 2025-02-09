def generate_java_class():
    # Solicitar el nombre de la clase
    class_name = input("Ingresa el nombre de la clase: ").strip()
    class_name = class_name[:1].upper() + class_name[1:]  # Asegurar que comience con mayúscula

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

    # Crear archivo .java para la clase
    file_name = f"{class_name}.java"
    with open(file_name, "w") as java_file:
        java_file.write(class_code)

    print(f"Clase {class_name} generada exitosamente en el archivo {file_name}.")

    # Llamar a la función para generar el DAO
    generate_DAO_Interface(class_name)

def generate_DAO_Interface(class_name):
    # Generar el contenido de la interfaz DAO
    dao_content = [
        "import java.util.List;\n",
        "import java.util.Optional;\n\n",
        "import org.springframework.data.jpa.repository.JpaRepository;\n\n",
        f"public interface {class_name}DAO extends JpaRepository<{class_name}, Integer> {{\n",
        "}\n"
    ]

    # Crear archivo .java para la interfaz DAO
    dao_file_name = f"{class_name}DAO.java"
    with open(dao_file_name, "w") as dao_file:
        dao_file.writelines(dao_content)

    print(f"Interfaz DAO {class_name}DAO generada exitosamente en el archivo {dao_file_name}.")

# Ejecutar la función
generate_java_class()
