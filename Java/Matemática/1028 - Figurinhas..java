/*
* Autor: Pierre Vieira
* Data de submissão: 19/01/2020 17:52:39
*/
import java.util.Scanner;

public class Main {
    private static int mdc(int n1, int n2) {
        int aux;
        while (n2 % n1 != 0){
            aux = n2;
            n2 = n1;
            n1 = aux % n1;
        }
        return n1;
    }

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int n, x, y, aux;
        String[] line;
        n = teclado.nextInt();
        teclado.nextLine();
        for (int i = 0; i < n; ++i){
            line = teclado.nextLine().split(" ");
            x = Integer.parseInt(line[0]);
            y = Integer.parseInt(line[1]);
            if(x > y){
                aux = x;
                x = y;
                y = aux;
            }
            System.out.println(mdc(x, y));
        }
    }
}
