/*
* Autor: Pierre Vieira
* Data de submissão: 11/02/2020 22:35:04
*/
import java.util.Scanner;
public class Main {

    private static int count(String expressao, char c) {
        int cont = 0;
        for (int i = 0; i < expressao.length(); ++i){
            if(expressao.charAt(i) == c){
                cont++;
            }
        }
        return cont;
    }

    private static String correto(String expressao) {
        if (count(expressao, '(') != count(expressao, ')')){
            return "incorrect";
        }
        if (expressao.charAt(0) == ')'){
            return "incorrect";
        }
        if (expressao.charAt(expressao.length() - 1) == '('){
            return "incorrect";
        }
        return "correct";
    }

    private static String myStrip(String string) {
        String s = "";
        char caractere;
        for (int i = 0; i < string.length(); ++i){
            caractere = string.charAt(i);
            if (caractere != ' '){
                s += caractere;
            }
        }
        return s;
    }

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        while (teclado.hasNext()){
            String expressao;
            expressao = myStrip(teclado.nextLine());
            System.out.println(correto(expressao));
        }
    }
}
