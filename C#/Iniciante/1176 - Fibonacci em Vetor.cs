/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 23:11:04
*/
using System;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int number, qtde;
            qtde = int.Parse(Console.ReadLine());
            for (int i = 0; i < qtde; i++) {
                number = int.Parse(Console.ReadLine());
                Console.WriteLine($"Fib({number}) = {fib(number)}");
            }
        }

        private static System.UInt64 fib(int number) {
            System.UInt64 primeiro, segundo, proximo = 0;
            if (number == 0) {
                return 0;
            }
            if (number == 1) {
                return 1;
            }
            primeiro = 0;
            segundo = 1;
            while (number > 1) {
                proximo = primeiro + segundo;
                primeiro = segundo;
                segundo = proximo;
                number--;
            }
            return proximo;
        }
    }
}
