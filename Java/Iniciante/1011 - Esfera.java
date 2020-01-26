import java.util.Scanner;

import static java.lang.StrictMath.pow;

/*
 * Autor: Pierre Vieira
 * Data de submissão: 26/01/2020 14:14:37
 */
public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        double raio = teclado.nextFloat();
        double volume = 3.14159*pow(raio, 3)*(4.0/3);
        System.out.printf("VOLUME = %.3f\n", volume);
    }
}
