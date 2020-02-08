import java.util.Scanner;

/*
 * Autor: Pierre Vieira
 * Data de submissão:
 */
public class Main {

    public static void main(String[] args) {
        int idade_monica, idade_filho1, idade_filho2, idade_filho3;
        Scanner teclado = new Scanner(System.in);
        idade_monica = teclado.nextInt();
        idade_filho1 = teclado.nextInt();
        idade_filho2 = teclado.nextInt();
        idade_filho3 = idade_monica - idade_filho1 - idade_filho2;
        if (idade_filho1 > idade_filho2 && idade_filho1 > idade_filho3){
            System.out.printf("%d\n", idade_filho1);
        } else if(idade_filho2 > idade_filho1 && idade_filho2 > idade_filho3){
            System.out.printf("%d\n", idade_filho2);
        } else{
            System.out.printf("%d\n", idade_filho3);
        }
    }
}
