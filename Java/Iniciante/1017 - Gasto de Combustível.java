/*
* Autor: Pierre Vieira
* Data de submissão: 11/02/2020 22:13:41
*/
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int tempo, velocidade, distancia;
        float litros;
        tempo = teclado.nextInt();
        velocidade = teclado.nextInt();
        distancia = velocidade * tempo;
        litros = (float) distancia / 12;
        System.out.printf("%.3f\n", litros);
    }
}
