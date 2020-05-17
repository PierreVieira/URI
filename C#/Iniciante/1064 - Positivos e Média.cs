/*
* Autor: Pierre Vieira
* Data de submissão: 17/05/2020 00:04:08
*/
using System;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int qtde_positivos;
            double number, media, soma_positivos;
            soma_positivos = qtde_positivos = 0;
            for (int i = 0; i < 6; i++) {
                number = double.Parse(Console.ReadLine());
                if (number > 0) {
                    qtde_positivos++;
                    soma_positivos += number;
                }
            }
            media = soma_positivos / qtde_positivos;
            Console.WriteLine($"{qtde_positivos} valores positivos\n{media.ToString("F1")}");
        }
    }
}
