import java.util.ArrayList;
import java.util.HashMap;

public class Juego {

    //Se instancian los HashMaps de respuesta final y su clon.
    HashMap<Integer, Integer> ans = new HashMap<Integer, Integer>();
    HashMap<Integer, Integer> clone = new HashMap<Integer, Integer>();
    ArrayList<Integer> pines = new ArrayList<Integer>();

    public Juego() {
        // Se crea la respuesta final y su clon.
//        ans.put(1, (int) (Math.random() * 8 + 1));
//        ans.put(2, (int) (Math.random() * 8 + 1));
//        ans.put(3, (int) (Math.random() * 8 + 1));
//        ans.put(4, (int) (Math.random() * 8 + 1));
        ans.put(1, 7); // Aqui se ingresa la respuesta manualmente.
        ans.put(2, 6);
        ans.put(3, 5);
        ans.put(4, 3);
        System.out.println(ans);
        newAttempt();
    }

    // En este metodo se recibe la respusta del usuario en un HashMap y la llave
    // por la cual se comienza a comprobar, que siempre debe ser '1'. Este
    // metodo incrementa el valor de 'a' y se llama a si mismo para comprobar
    // la siguiente llave.
    public ArrayList comprobar(HashMap check, int a) {
        if (a <= clone.size()) {
            if (clone.containsValue(check.get(a))) {
                for (int i = 1; i <= clone.size(); i++) {
                    if (clone.get(i) == check.get(i)) {
                        System.out.print("|  RED  |");
                        clone.replace(i, 0);
                        pines.add(2);
                        break;
                    }
                }
                for (int i = 1; i <= clone.size(); i++) {
                    if (clone.get(i) == check.get(a)) {
                        System.out.print("| WHITE |");
                        clone.replace(i, 0);
                        pines.add(1);
                        break;
                    }
                }
            }
            a++;
            comprobar(check, a);
        }
        return pines;
    }

    // Este metodo clona la respuesta final para poder comparar la respuesta
    // propuesta por el usuario sin alterar la respuesta final.
    public void newAttempt() {
        clone.put(1, ans.get(1));
        clone.put(2, ans.get(2));
        clone.put(3, ans.get(3));
        clone.put(4, ans.get(4));
    }
}
