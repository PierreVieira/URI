/*
* Autor: Pierre Vieira
* Data de submissão: 19/01/2020 17:10:54
*/
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int a, b, c, d;
        a = teclado.nextInt();
        b = teclado.nextInt();
        c = teclado.nextInt();
        d = teclado.nextInt();
        System.out.printf("DIFERENCA = %d\n", (a*b - c*d));
    }
}
