import java.io.IOException;
import java.util.Scanner;
/*
  Autor: Pierre Vieira
  Data de submissão: 17/01/2019 14:23:58
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        String mes[] = {"January", "February", "March", "April","May","June","July","August","September","October","November","December"};
        Scanner teclado = new Scanner(System.in);
        int numero = teclado.nextInt();
        System.out.println(""+mes[numero-1]);
 
    }
 
}
