/*
 * Autor: Pierre Vieira
 * Data de submissão: 19/01/2020 17:32:20
 */
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        String nome;
        double salario_fixo, total_vendas, total;
        nome = teclado.next();
        salario_fixo = teclado.nextDouble();
        total_vendas = teclado.nextDouble();
        total = total_vendas*0.15 + salario_fixo;
        System.out.printf("TOTAL = R$ %.2f\n", total);
    }
}
