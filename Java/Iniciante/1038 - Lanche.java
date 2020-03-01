/*
* Autor: Pierre Vieira
* Data de submissão: 29/02/2020 20:59:09
*/
import java.util.Scanner;
public class Main {


    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int codigo, quantidade;
        float preco = 0;
        codigo = teclado.nextInt();
        quantidade = teclado.nextInt();
        switch (codigo){
            case 1:
                preco += 4;
                break;
            case 2:
                preco += 4.5;
                break;
            case 3:
                preco += 5;
                break;
            case 4:
                preco += 2;
                break;
            case 5:
                preco += 1.5;

        }
        System.out.printf("Total: R$ %.2f\n", preco*quantidade);
    }

}
