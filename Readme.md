Java Class Generator
Este proyecto proporciona una herramienta para generar automáticamente clases Java junto con sus respectivas interfaces y clases de servicio siguiendo un patrón de diseño DAO (Data Access Object) y la estructura de Spring Boot.
Descripción
El generador crea automáticamente cuatro archivos Java diferentes para cada entidad:

Clase Principal: Una clase Java básica con los atributos especificados, constructor y método toString().
Interfaz DAO: Una interfaz que extiende JpaRepository para operaciones de base de datos.
Interfaz de Servicio: Define los métodos básicos de CRUD y gestión de estado.
Clase de Servicio: Implementación de la interfaz de servicio con la lógica de negocio básica.

Características

Generación automática de código boilerplate
Integración con Spring Boot y JPA
Soporte para operaciones CRUD básicas
Manejo de estados (habilitado/inhabilitado)
Validación de entrada de datos
Manejo de errores robusto

Requisitos Previos

Java JDK 8 o superior
Spring Boot en tu proyecto (para usar las clases generadas)
Jakarta Persistence API

Instalación

Clona este repositorio:

bashCopygit clone [URL del repositorio]

Compila el generador:

bashCopyjavac JavaClassGenerator.java
Uso

Ejecuta el generador:

bashCopyjava JavaClassGenerator

Sigue las instrucciones en pantalla:

Ingresa el nombre de la clase
Ingresa los atributos en formato "tipo nombre"
Escribe "fin" cuando hayas terminado de ingresar atributos



Ejemplo de Uso
bashCopyIngresa el nombre de la clase: Usuario
Ingresa los atributos de la clase en el formato 'tipo nombre'. Escribe 'fin' para terminar.
Atributo: String nombre
Atributo: String email
Atributo: int edad
Atributo: fin
Esto generará los siguientes archivos:

Usuario.java
UsuarioDAO.java
UsuarioInterface.java
UsuarioServicio.java

Estructura de Archivos Generados
Clase Principal
javaCopypublic class Usuario {
    private String nombre;
    private String email;
    private int edad;
    // Constructor, getters, setters y toString()
}
Interfaz DAO
javaCopypublic interface UsuarioDAO extends JpaRepository<Usuario, Integer> {
}
Interfaz de Servicio
javaCopypublic interface UsuarioInterface {
    void guardarUsuario(Usuario usuario);
    List<Usuario> listadoUsuario();
    Usuario consultar(int id);
    void eliminarUsuario(int id);
    void inhabilitarUsuario(int id);
    void habilitarUsuario(int id);
}
Clase de Servicio
javaCopy@Service
public class UsuarioServicio implements UsuarioInterface {
    // Implementación de métodos
}
Características Técnicas

Uso de StringBuilder para generación eficiente de código
Manejo de excepciones para operaciones de archivo
Validación de entrada de datos
Generación de código con formato consistente
Integración con Spring Boot y JPA
Soporte para transacciones

Contribuir
Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

Fork el proyecto
Crea una nueva rama (git checkout -b feature/AmazingFeature)
Realiza tus cambios
Commit tus cambios (git commit -m 'Add some AmazingFeature')
Push a la rama (git push origin feature/AmazingFeature)
Abre un Pull Request

Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE.md para más detalles.