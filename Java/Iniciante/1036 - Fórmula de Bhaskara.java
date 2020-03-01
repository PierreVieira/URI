/*
* Autor: Pierre Vieira
* Data de submissão: 29/02/2020 23:01:33
*/
import java.util.Scanner;

import static java.lang.StrictMath.pow;

public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        double a, b, c, delta, r1, r2;
        a = teclado.nextDouble();
        b = teclado.nextDouble();
        c = teclado.nextDouble();
        delta = b*b - 4*a*c;
        r1 = (-b + pow(delta, 0.5))/(2*a);
        r2 = (-b - pow(delta, 0.5))/(2*a);
        if(delta < 0 || a == 0){
            System.out.println("Impossivel calcular");
        }
        else {
            System.out.printf("R1 = %.5f\nR2 = %.5f\n", r1, r2);
        }
    }

}
