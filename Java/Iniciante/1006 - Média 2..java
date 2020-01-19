/*
 * Autor: Pierre Vieira
 * Data de submissão:
 */
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        double a, b, c;
        a = teclado.nextDouble();
        b = teclado.nextDouble();
        c = teclado.nextDouble();
        System.out.printf("MEDIA = %.1f\n", (2*a+3*b+5*c)/10);
    }
}
