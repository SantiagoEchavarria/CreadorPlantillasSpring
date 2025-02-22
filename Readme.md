# Java Class Generator 🛠️

## Índice 📑
- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura de Archivos Generados](#estructura-de-archivos-generados)


## Descripción 📖
Este proyecto proporciona una herramienta para generar automáticamente clases Java junto con sus respectivas interfaces y clases de servicio siguiendo un patrón de diseño DAO (Data Access Object) y la estructura de Spring Boot.

El generador crea automáticamente cuatro archivos Java diferentes para cada entidad:
1. **Clase Principal**: Una clase Java básica con los atributos especificados, constructor y método toString().
2. **Interfaz DAO**: Una interfaz que extiende JpaRepository para operaciones de base de datos.
3. **Interfaz de Servicio**: Define los métodos básicos de CRUD y gestión de estado.
4. **Clase de Servicio**: Implementación de la interfaz de servicio con la lógica de negocio básica.

## Características ✨
* Generación automática de código boilerplate
* Integración con Spring Boot y JPA
* Soporte para operaciones CRUD básicas
* Manejo de estados (habilitado/inhabilitado)
* Validación de entrada de datos
* Manejo de errores robusto

## Instalación 💻
1. Clona este repositorio:
   ```bash
   git clone [URL del repositorio]
   ```

2. Compila el generador:
   ```bash
   javac JavaClassGenerator.java
   ```

## Uso 🚀
1. Ejecuta el generador:
   ```bash
   java JavaClassGenerator
   ```

2. Sigue las instrucciones en pantalla:
   - Ingresa el nombre de la clase
   - Ingresa los atributos en formato "tipo nombre"
   - Escribe "fin" cuando hayas terminado de ingresar atributos

### Ejemplo de Uso 📝
```bash
Ingresa el nombre de la clase: Usuario
Ingresa los atributos de la clase en el formato 'tipo nombre'. Escribe 'fin' para terminar.
Atributo: String nombre
Atributo: String email
Atributo: int edad
Atributo: fin
```

Esto generará los siguientes archivos:
* `Usuario.java`
* `UsuarioDAO.java`
* `UsuarioInterface.java`
* `UsuarioServicio.java`

## Estructura de Archivos Generados 📂

### Clase Principal
```java
public class Usuario {
    private String nombre;
    private String email;
    private int edad;
    // Constructor, getters, setters y toString()
}
```

### Interfaz DAO
```java
public interface UsuarioDAO extends JpaRepository {
}
```

### Interfaz de Servicio
```java
public interface UsuarioInterface {
    void guardarUsuario(Usuario usuario);
    List listadoUsuario();
    Usuario consultar(int id);
    void eliminarUsuario(int id);
    void inhabilitarUsuario(int id);
    void habilitarUsuario(int id);
}
```

### Clase de Servicio
```java
@Service
public class UsuarioServicio implements UsuarioInterface {
    // Implementación de métodos
}
```


