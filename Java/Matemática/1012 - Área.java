import java.util.Scanner;

/*
 * Autor: Pierre Vieira
 * Data de submissão: 02/02/2020 14:30:25
 */
public class Main {

    public static void main(String[] args) {
        String[] entrada;
        Scanner teclado = new Scanner(System.in);
        double a, b, c, area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo;
        entrada = teclado.nextLine().split(" ");
        a = Double.parseDouble(entrada[0]);
        b = Double.parseDouble(entrada[1]);
        c = Double.parseDouble(entrada[2]);
        area_triangulo = a*c/2;
        area_circulo = 3.14159*c*c;
        area_trapezio = (a + b)*c/2;
        area_quadrado = b*b;
        area_retangulo = a*b;
        System.out.printf("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f\n", area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo);
    }
}
