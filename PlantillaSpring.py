def generate_java_class():
    # Solicitar el nombre de la clase
    class_name = input("Ingresa el nombre de la clase: ").strip()
    class_name = class_name[:1].upper() + class_name[1:]  # Asegurar que comience con mayúscula

    # Solicitar los atributos y tipos de datos
    print("Ingresa los atributos de la clase en el formato 'tipo nombre'. Escribe 'fin' para terminar.")
    attributes = []
    while True:
        attr = input("Atributo (o 'fin' para terminar): ").strip()
        if attr.lower() == 'fin':
            break
        if len(attr.split()) == 2:
            attributes.append(attr.strip())
        else:
            print("Formato incorrecto. Usa 'tipo nombre'.")

    if not attributes:
        print("No se proporcionaron atributos. No se generará el archivo.")
        return

    # Generar el contenido de la clase
    class_content = [f"public class {class_name} {{\n"]
    for attr in attributes:
        tipo, nombre = attr.split()
        class_content.append(f"    private {tipo} {nombre};\n")

    class_content.append("\n")

    # Constructor
    class_content.append(f"    public {class_name}(")
    constructor_params = [f"{attr.split()[0]} {attr.split()[1]}" for attr in attributes]
    class_content.append(", ".join(constructor_params) + ") {\n")
    for attr in attributes:
        nombre = attr.split()[1]
        class_content.append(f"        this.{nombre} = {nombre};\n")
    class_content.append("    }\n\n")

    # toString
    class_content.append("    @Override\n")
    class_content.append("    public String toString() {\n")
    to_string_content = [f'"{attr.split()[1]}=" + {attr.split()[1]}' for attr in attributes]
    class_content.append(f"        return \"{class_name} [\" + " + " + \", \" + ".join(to_string_content) + " + \"]\";\n")
    class_content.append("    }\n")
    class_content.append("}\n")

    # Crear archivo de clase
    file_name = f"{class_name}.java"
    with open(file_name, "w") as java_file:
        java_file.write("".join(class_content))

    print(f"Clase {class_name} generada exitosamente en el archivo {file_name}.")

    # Llamar a las funciones auxiliares
    generate_DAO_Interface(class_name)
    generate_Interface(class_name)
    generate_Servicio(class_name)

def generate_DAO_Interface(class_name):
    dao_content = [
        "import java.util.List;\n",
        "import java.util.Optional;\n\n",
        "import org.springframework.data.jpa.repository.JpaRepository;\n\n",
        f"public interface {class_name}DAO extends JpaRepository<{class_name}, Integer> {{\n",
        "}\n"
    ]
    dao_file_name = f"{class_name}DAO.java"
    with open(dao_file_name, "w") as dao_file:
        dao_file.writelines(dao_content)
    print(f"Interfaz DAO {class_name}DAO generada exitosamente en el archivo {dao_file_name}.")

def generate_Interface(class_name):
    class_name_lower = class_name[:1].lower() + class_name[1:]
    interface_content = [
        "import java.util.List;\n\n",
        f"public interface {class_name}Interface {{\n",
        f"    void guardar{class_name}({class_name} {class_name_lower});\n",
        f"    List<{class_name}> listado{class_name}();\n",
        f"    {class_name} consultar(int id);\n",
        f"    void eliminar{class_name}(int id);\n",
        f"    void inhabilitar{class_name}(int id);\n",
        f"    void habilitar{class_name}(int id);\n",
        "}\n"
    ]
    interface_file_name = f"{class_name}Interface.java"
    with open(interface_file_name, "w") as interface_file:
        interface_file.writelines(interface_content)
    print(f"Interfaz {class_name}Interface generada exitosamente en el archivo {interface_file_name}.")

def generate_Servicio(class_name):
    class_name_lower = class_name[:1].lower() + class_name[1:]
    servicio_content = [
        "import java.util.List;\n",
        "import org.springframework.beans.factory.annotation.Autowired;\n",
        "import org.springframework.stereotype.Service;\n",
        "import jakarta.transaction.Transactional;\n\n",
        f"@Service\n",
        f"public class {class_name}Servicio implements {class_name}Interface {{\n",
        f"    @Autowired\n",
        f"    private {class_name}DAO {class_name_lower}DAO;\n\n",
        f"    public {class_name}Servicio() {{\n",
        f"    }}\n\n",
        f"    @Transactional\n",
        f"    public void guardar{class_name}({class_name} {class_name_lower}) {{\n",
        f"        this.{class_name_lower}DAO.save({class_name_lower});\n",
        f"    }}\n\n",
        f"    @Transactional\n",
        f"    public List<{class_name}> listado{class_name}() {{\n",
        f"        return this.{class_name_lower}DAO.findAll();\n",
        f"    }}\n\n",
        f"    @Override\n",
        f"    public {class_name} consultar(int id) {{\n",
        f"        return {class_name_lower}DAO.findById(id).orElse(null);\n",
        f"    }}\n\n",
        f"    @Override\n",
        f"    @Transactional\n",
        f"    public void eliminar(int id) {{\n",
        f"        {class_name_lower}DAO.deleteById(id);\n",
        f"    }}\n\n",
        f"    @Override\n",
        f"    @Transactional\n",
        f"    public void inhabilitar(int id) {{\n",
        f"        {class_name} {class_name_lower} = {class_name_lower}DAO.findById(id).orElse(null);\n",
        f"        if ({class_name_lower} != null) {{\n",
        f"            {class_name_lower}.setEstado(Estado.INHABILITADO);\n",
        f"            {class_name_lower}DAO.save({class_name_lower});\n",
        f"        }}\n",
        f"    }}\n\n",
        f"    @Override\n",
        f"    @Transactional\n",
        f"    public void habilitar{class_name}(int id) {{\n",
        f"        {class_name} {class_name_lower} = {class_name_lower}DAO.findById(id).orElseThrow(() -> new RuntimeException(\"{class_name} no encontrada\"));\n",
        f"        {class_name_lower}.setEstado(Estado.HABILITADO);\n",
        f"        {class_name_lower}DAO.save({class_name_lower});\n",
        f"    }}\n",
        f"}}\n"
    ]
    servicio_file_name = f"{class_name}Servicio.java"
    with open(servicio_file_name, "w") as servicio_file:
        servicio_file.writelines(servicio_content)
    print(f"Servicio {class_name}Servicio generado exitosamente en el archivo {servicio_file_name}.")

# Ejecutar la función
generate_java_class()
