/*
* Autor: Pierre Vieira
* Data de submissão: 04/03/2020 12:40:28
*/
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int x;
        float y;
        x = teclado.nextInt();
        y = teclado.nextFloat();
        System.out.printf("%.3f km/l\n", x/y);
    }

}
