import java.util.Scanner;

/*
 * Autor: Pierre Vieira
 * Data de submissão: 26/01/2020 14:35:30
 */
public class Main {
    private static int qtdeChar(String plays, char c) {
        int cont = 0;
        for (int i = 0; i < plays.length(); ++i){
            if (plays.charAt(i) == c){
                cont++;
            }
        }
        return cont;
    }

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int numero;
        String plays;
        while (true){
            numero = teclado.nextInt();
            if (numero == 0) break;
            teclado.nextLine();
            plays = teclado.nextLine();
            System.out.println("Mary won "+qtdeChar(plays, '0')+" times and John won "+qtdeChar(plays, '1')+" times");
        }
    }
}
