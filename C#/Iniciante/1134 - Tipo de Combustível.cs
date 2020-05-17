/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 21:37:57
*/
using System;

namespace URI {
    class Program {
        static void Main(string[] args) {
            string[] combustiveis = { "Alcool", "Gasolina", "Diesel" };
            int[] n_comb = {0, 0, 0};
            int n;
            Console.WriteLine("MUITO OBRIGADO");
            while (true) {
                n = int.Parse(Console.ReadLine());
                if (n <= 4 && n >= 1) {
                    if (n == 4) {
                        for (int i = 0; i < 3; i++) {
                            Console.WriteLine($"{combustiveis[i]}: {n_comb[i]}");
                        }
                        break;
                    }
                    n_comb[n - 1]++;
                }
            }
        }
    }
}
