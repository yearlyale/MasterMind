import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import org.python.util.PythonInterpreter;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Juego juego = new Juego(); // Se inicializa el juego, la respuesta final y los intentos disponibles.
        int attempts = 10;
        ArrayList<Integer> pines = new ArrayList<Integer>();
        HashMap<Integer, Integer> check = new HashMap<Integer, Integer>(); // HashMap en el que se van guardando las respuestas del jugador.

        while (attempts != 0) { // Se itera mientras el jugador aun tenga intentos disponibles.
            System.out.println("\n Intentos: " + attempts);
            System.out.println("Escribe 4 numeros del 1 al 8:");

            // Se inicializa el interprete de python y se ejecuta el archivo resolver.py
            String[] argumentos = {"juego.ans.get(1)", "juego.ans.get(2)", "juego.ans.get(3)", "juego.ans.get(4)"};
            PythonInterpreter interpreter = new PythonInterpreter();
            PythonInterpreter.initialize(null, null, argumentos);
            interpreter.execfile("../resolver.py");
            // Se imprimen las respuestas.
            System.out.println(check);

            pines = juego.comprobar(check, 1); //Llamada al metodo que comprueba la respuesta propuesta
                        
            // Comprobacion para terminar el juego
            if (check.get(1) != juego.ans.get(1) || check.get(2) != juego.ans.get(2) ||
                    check.get(3) != juego.ans.get(3) || check.get(4) != juego.ans.get(4)) {
                attempts -= 1;
                juego.newAttempt();
            } else {
                System.out.println("\nFELICIDADES, GANASTE!!");
                System.exit(0);
            }
        } System.out.println("\nPERDISTE :(");
    }
}
