/*
 * Autor: Pierre Vieira
 * Data de submissão: 19/01/2020 17:43:31
 */
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int e, d, dif;
        String[] line = teclado.nextLine().split(" ");
        e = Integer.parseInt(line[0]);
        d = Integer.parseInt(line[1]);
        dif = d - e;
        if (dif < 0){
            System.out.println("Eu odeio a professora!");
        }
        else if(dif >= 3){
            System.out.println("Muito bem! Apresenta antes do Natal!");
        }
        else{
            System.out.println("Parece o trabalho do meu filho!");
            e += 2;
            if(e > 23){
                System.out.println("Fail! Entao eh nataaaaal!");
            }
            else{
                System.out.println("TCC Apresentado!");
            }
        }
    }
}
