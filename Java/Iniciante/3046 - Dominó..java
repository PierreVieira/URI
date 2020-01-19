/*
 * Autor: Pierre Vieira
 * Data de submissão: 19/01/2020 18:09:08
 */
import java.util.Scanner;

public class Main {

    private static int duplo_n(int n) {
        // Eq de recorrência
        // D(0) = 1
        // D(n) = D(n - 1) + (n + 1)
        return (n * n + 3 * n) / 2 + 1;
    }

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int n;
        n = teclado.nextInt();
        System.out.println(duplo_n(n));
    }
}

