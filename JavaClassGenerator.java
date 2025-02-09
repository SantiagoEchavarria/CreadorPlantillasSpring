import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class JavaClassGenerator {
    private static final Scanner scanner = new Scanner(System.in);

    public static void generateJavaClass() {
        // Solicitar el nombre de la clase
        System.out.print("Ingresa el nombre de la clase: ");
        String className = scanner.nextLine().trim();
        className = className.substring(0, 1).toUpperCase() + className.substring(1);

        // Solicitar los atributos y tipos de datos
        System.out.println("Ingresa los atributos de la clase en el formato 'tipo nombre'. Escribe 'fin' para terminar.");
        List<String> attributes = new ArrayList<>();
        
        while (true) {
            System.out.print("Atributo (o 'fin' para terminar): ");
            String attr = scanner.nextLine().trim();
            if (attr.toLowerCase().equals("fin")) {
                break;
            }
            if (attr.split(" ").length == 2) {
                attributes.add(attr.trim());
            } else {
                System.out.println("Formato incorrecto. Usa 'tipo nombre'.");
            }
        }

        if (attributes.isEmpty()) {
            System.out.println("No se proporcionaron atributos. No se generará el archivo.");
            return;
        }

        // Generar el contenido de la clase
        StringBuilder classContent = new StringBuilder();
        classContent.append(String.format("public class %s {\n", className));

        // Atributos
        for (String attr : attributes) {
            String[] parts = attr.split(" ");
            classContent.append(String.format("    private %s %s;\n", parts[0], parts[1]));
        }
        classContent.append("\n");

        // Constructor
        classContent.append(String.format("    public %s(", className));
        List<String> constructorParams = new ArrayList<>();
        for (String attr : attributes) {
            String[] parts = attr.split(" ");
            constructorParams.add(String.format("%s %s", parts[0], parts[1]));
        }
        classContent.append(String.join(", ", constructorParams)).append(") {\n");
        
        for (String attr : attributes) {
            String nombre = attr.split(" ")[1];
            classContent.append(String.format("        this.%s = %s;\n", nombre, nombre));
        }
        classContent.append("    }\n\n");

        // toString
        classContent.append("    @Override\n");
        classContent.append("    public String toString() {\n");
        List<String> toStringParts = new ArrayList<>();
        for (String attr : attributes) {
            String nombre = attr.split(" ")[1];
            toStringParts.add(String.format("\"%s=\" + %s", nombre, nombre));
        }
        classContent.append(String.format("        return \"%s [\" + %s + \"]\";\n",
                className, String.join(" + \", \" + ", toStringParts)));
        classContent.append("    }\n");
        classContent.append("}\n");

        // Crear archivo de clase
        String fileName = className + ".java";
        try (FileWriter javaFile = new FileWriter(fileName)) {
            javaFile.write(classContent.toString());
            System.out.println("Clase " + className + " generada exitosamente en el archivo " + fileName);
            
            // Generar archivos adicionales
            generateDAOInterface(className);
            generateInterface(className);
            generateServicio(className);
            
        } catch (IOException e) {
            System.err.println("Error al escribir el archivo: " + e.getMessage());
        }
    }

    private static void generateDAOInterface(String className) {
        StringBuilder daoContent = new StringBuilder();
        daoContent.append("import java.util.List;\n")
                 .append("import java.util.Optional;\n\n")
                 .append("import org.springframework.data.jpa.repository.JpaRepository;\n\n")
                 .append(String.format("public interface %sDAO extends JpaRepository<%s, Integer> {\n", className, className))
                 .append("}\n");

        String daoFileName = className + "DAO.java";
        try (FileWriter daoFile = new FileWriter(daoFileName)) {
            daoFile.write(daoContent.toString());
            System.out.println("Interfaz DAO " + className + "DAO generada exitosamente en el archivo " + daoFileName);
        } catch (IOException e) {
            System.err.println("Error al escribir el archivo DAO: " + e.getMessage());
        }
    }

    private static void generateInterface(String className) {
        String classNameLower = className.substring(0, 1).toLowerCase() + className.substring(1);
        StringBuilder interfaceContent = new StringBuilder();
        interfaceContent.append("import java.util.List;\n\n")
                       .append(String.format("public interface %sInterface {\n", className))
                       .append(String.format("    void guardar%s(%s %s);\n", className, className, classNameLower))
                       .append(String.format("    List<%s> listado%s();\n", className, className))
                       .append(String.format("    %s consultar(int id);\n", className))
                       .append(String.format("    void eliminar%s(int id);\n", className))
                       .append(String.format("    void inhabilitar%s(int id);\n", className))
                       .append(String.format("    void habilitar%s(int id);\n", className))
                       .append("}\n");

        String interfaceFileName = className + "Interface.java";
        try (FileWriter interfaceFile = new FileWriter(interfaceFileName)) {
            interfaceFile.write(interfaceContent.toString());
            System.out.println("Interfaz " + className + "Interface generada exitosamente en el archivo " + interfaceFileName);
        } catch (IOException e) {
            System.err.println("Error al escribir el archivo Interface: " + e.getMessage());
        }
    }

    private static void generateServicio(String className) {
        String classNameLower = className.substring(0, 1).toLowerCase() + className.substring(1);
        StringBuilder servicioContent = new StringBuilder();
        servicioContent.append("import java.util.List;\n")
                      .append("import org.springframework.beans.factory.annotation.Autowired;\n")
                      .append("import org.springframework.stereotype.Service;\n")
                      .append("import jakarta.transaction.Transactional;\n\n")
                      .append("@Service\n")
                      .append(String.format("public class %sServicio implements %sInterface {\n", className, className))
                      .append("    @Autowired\n")
                      .append(String.format("    private %sDAO %sDAO;\n\n", className, classNameLower))
                      .append(String.format("    public %sServicio() {\n    }\n\n", className))
                      .append("    @Transactional\n")
                      .append(String.format("    public void guardar%s(%s %s) {\n", className, className, classNameLower))
                      .append(String.format("        this.%sDAO.save(%s);\n    }\n\n", classNameLower, classNameLower))
                      .append("    @Transactional\n")
                      .append(String.format("    public List<%s> listado%s() {\n", className, className))
                      .append(String.format("        return this.%sDAO.findAll();\n    }\n\n", classNameLower))
                      .append("    @Override\n")
                      .append(String.format("    public %s consultar(int id) {\n", className))
                      .append(String.format("        return %sDAO.findById(id).orElse(null);\n    }\n\n", classNameLower))
                      .append("    @Override\n")
                      .append("    @Transactional\n")
                      .append("    public void eliminar(int id) {\n")
                      .append(String.format("        %sDAO.deleteById(id);\n    }\n\n", classNameLower))
                      .append("    @Override\n")
                      .append("    @Transactional\n")
                      .append("    public void inhabilitar(int id) {\n")
                      .append(String.format("        %s %s = %sDAO.findById(id).orElse(null);\n", 
                              className, classNameLower, classNameLower))
                      .append(String.format("        if (%s != null) {\n", classNameLower))
                      .append(String.format("            %s.setEstado(Estado.INHABILITADO);\n", classNameLower))
                      .append(String.format("            %sDAO.save(%s);\n        }\n    }\n\n", 
                              classNameLower, classNameLower))
                      .append("    @Override\n")
                      .append("    @Transactional\n")
                      .append(String.format("    public void habilitar%s(int id) {\n", className))
                      .append(String.format("        %s %s = %sDAO.findById(id).orElseThrow(() -> " +
                              "new RuntimeException(\"%s no encontrada\"));\n", 
                              className, classNameLower, classNameLower, className))
                      .append(String.format("        %s.setEstado(Estado.HABILITADO);\n", classNameLower))
                      .append(String.format("        %sDAO.save(%s);\n    }\n", classNameLower, classNameLower))
                      .append("}\n");

        String servicioFileName = className + "Servicio.java";
        try (FileWriter servicioFile = new FileWriter(servicioFileName)) {
            servicioFile.write(servicioContent.toString());
            System.out.println("Servicio " + className + "Servicio generado exitosamente en el archivo " + servicioFileName);
        } catch (IOException e) {
            System.err.println("Error al escribir el archivo Servicio: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        generateJavaClass();
    }
}