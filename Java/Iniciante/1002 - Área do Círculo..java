/*
 * Autor: Pierre Vieira
 * Data de submissão: 19/01/2020 16:50:21
 */
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        double r;
        r = teclado.nextDouble();
        System.out.printf("A=%.4f\n", 3.14159*r*r);
    }
}
