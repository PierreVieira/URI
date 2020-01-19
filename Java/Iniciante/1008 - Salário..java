/*
* Autor: Pierre Vieira
* Data de submissão: 19/01/2020 17:15:54
*/
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int a, b;
        double c;
        a = teclado.nextInt();
        b = teclado.nextInt();
        c = teclado.nextDouble();
        System.out.println("NUMBER = "+a);
        System.out.printf("SALARY = U$ %.2f\n", b*c);
    }
}