/*
* Autor: Pierre Vieira
* Data de submissão: 04/03/2020 12:31:07
*/
import java.util.Scanner;

import static java.lang.Math.abs;
public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int a, b, c, maior;
        a = teclado.nextInt();
        b = teclado.nextInt();
        c = teclado.nextInt();
        maior = retorna_maior(a, b);
        maior = retorna_maior(maior, c);
        System.out.println(maior+" eh o maior");
    }

    private static int retorna_maior(int a, int b) {
        return (a+b+abs(a-b))/2;
    }

}
