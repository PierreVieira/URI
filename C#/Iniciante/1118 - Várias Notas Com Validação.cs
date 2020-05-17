/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 16:05:22
*/
using System;
using System.Globalization;

namespace URI {
    class URI {
        static void Main(string[] args) {
            double resposta, n1, n2;
            while (true) {
                n1 = validaNota();
                n2 = validaNota();
                Console.WriteLine($"media = {(0.5 * (n1 + n2)).ToString("F2", CultureInfo.InvariantCulture)}");
                resposta = validaResposta();
                if (resposta == 2) {
                    break;
                }
            }
        }

        private static int validaResposta() {
            int resposta;
            while (true) {
                Console.WriteLine("novo calculo (1-sim 2-nao)");
                resposta = int.Parse(Console.ReadLine());
                if (resposta == 1 || resposta == 2) {
                    return resposta;
                }
            }
        }

        private static double validaNota() {
            double nota;
            while (true) {
                nota = double.Parse(Console.ReadLine());
                if (nota <= 10 && nota >= 0) {
                    return nota;
                }
                Console.WriteLine("nota invalida");
            }
        }
    }
}
