import java.util.Scanner;

/*
 * Autor: Pierre Vieira
 * Data de submissão: 25/01/2020 17:31:39
 */
public class Main {
    private static int calcula_qtde_chamadas(int n) {
        if(n == 1){
            return 0;
        }
        else if(n == 2){
            return 2;
        }
        return calcula_qtde_chamadas(n - 1) + calcula_qtde_chamadas(n - 2)+ 2;
    }

    private static int fib(int n) {
        if(n == 0){
            return 0;
        }
        else if(n == 1){
            return 1;
        }
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int qtde_casos_teste, n;
        qtde_casos_teste = teclado.nextInt();
        for (int i = 0; i < qtde_casos_teste; ++i){
            n = teclado.nextInt();
            System.out.printf("fib(%d) = %d calls = %d\n", n, calcula_qtde_chamadas(n), fib(n));
        }
    }
}
