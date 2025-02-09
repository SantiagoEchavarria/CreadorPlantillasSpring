# Java Class Generator 🛠️

## Índice 📑
- [Descripción](#descripción)
- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura de Archivos Generados](#estructura-de-archivos-generados)
- [Características Técnicas](#características-técnicas)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

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

## Requisitos Previos 📋
* Java JDK 8 o superior
* Spring Boot en tu proyecto (para usar las clases generadas)
* Jakarta Persistence API

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

## Características Técnicas 🔧
* Uso de StringBuilder para generación eficiente de código
* Manejo de excepciones para operaciones de archivo
* Validación de entrada de datos
* Generación de código con formato consistente
* Integración con Spring Boot y JPA
* Soporte para transacciones

## Contribuir 🤝
Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Fork el proyecto
2. Crea una nueva rama
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Realiza tus cambios
4. Commit tus cambios
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
5. Push a la rama
   ```bash
   git push origin feature/AmazingFeature
   ```
6. Abre un Pull Request
