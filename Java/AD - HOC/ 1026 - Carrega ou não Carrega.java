import java.util.Scanner;

/*
 * Autor: Pierre Vieira
 * Data de submissão: 26/01/2020 15:20:36
 */
public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        long x, y;
        while (teclado.hasNext()) {
            x = teclado.nextLong();
            y = teclado.nextLong();
            System.out.println(x ^ y);
        }
    }
}
