/*
* Autor: Pierre Vieira
* Data de submissão: 25/02/2020 22:32:29
*/
import java.util.Scanner;
public class Main {


    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int c, n, valor_total, placa, tamanho;
        char entrada_saida;
        while (teclado.hasNext()) {
            c = teclado.nextInt();
            n = teclado.nextInt();
            Estacionamento estacionamento = new Estacionamento();
            estacionamento.espacos = new int[c];
            valor_total = 0;

            for (int i = 0; i < n; ++i) {
                entrada_saida = teclado.next().charAt(0);
                if (entrada_saida == 'C') {
                    placa = teclado.nextInt();
                    tamanho = teclado.nextInt();
                    if (estacionamento.addCarro(placa, tamanho)) {
                        valor_total += 10;
                    }
                } else if (entrada_saida == 'S') {
                    placa = teclado.nextInt();
                    estacionamento.remover_carro(placa);
                }
            }
            System.out.println(valor_total);
        }
        teclado.close();
    }
    static class Estacionamento{
        int[] espacos;
        public boolean addCarro(int placa, int tamanho){
            int p_inicial = getPosicaoInicial(tamanho);
            if (p_inicial == -1){
                return false;
            }
            for (int i = p_inicial; i < p_inicial + tamanho; ++i){
                espacos[i] = placa;
            }
            return true;
        }

        private int getPosicaoInicial(int tamanho) {
            int p_inicial = -1;
            for (int i = 0; i < espacos.length; ++i){
                if (espacos[i] == 0){
                    if (p_inicial == -1){
                        p_inicial = i;
                    }
                    if (i + 1 - p_inicial >= tamanho){
                        return p_inicial;
                    }
                }
                else {
                    p_inicial = - 1;
                }
            }
            if (espacos.length - p_inicial >= tamanho){
                return p_inicial;
            }
            return -1;
        }
        private void remover_carro(int placa){
            for (int i = 0; i < espacos.length; ++i){
                if (espacos[i] == placa){
                    espacos[i] = 0;
                }
            }
        }

    }
}
