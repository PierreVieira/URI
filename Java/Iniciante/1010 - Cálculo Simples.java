import java.util.Scanner;

/*
 * Autor: Pierre Vieira
 * Data de submissão: 26/01/2020 13:52:03
 */
public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        String line1, line2;
        int qtde_peca1, qtde_peca2;
        float valor_peca1, valor_peca2;
        line1 = teclado.nextLine();
        line2 = teclado.nextLine();
        qtde_peca1 = Integer.parseInt(line1.split(" ")[1]);
        qtde_peca2 = Integer.parseInt(line2.split(" ")[1]);
        valor_peca1 = Float.parseFloat(line1.split(" ")[2]);
        valor_peca2 = Float.parseFloat(line2.split(" ")[2]);
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", qtde_peca1*valor_peca1 + qtde_peca2*valor_peca2);
    }
}
