/*
* Autor: Pierre Vieira
* Data de submissão: 19/01/2020 16:58:00
*/
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int a, b;
        a = teclado.nextInt();
        b = teclado.nextInt();
        System.out.println("PROD = "+(a*b));
    }
}