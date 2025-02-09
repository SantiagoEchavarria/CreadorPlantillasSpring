public class Ciudad {
    private int id;
    private String nombre;

    public Ciudad(int id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Ciudad [" + "id=" + id + ", " + "nombre=" + nombre + "]";
    }
}
