/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 21:59:24
*/
using System;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int numero, soma;
            while (true) {
                soma = 0;
                numero = int.Parse(Console.ReadLine());
                if (numero == 0) {
                    break;
                }
                if (numero % 2 != 0) {
                    numero++;
                }
                for (int i = 0; i < 5; i++) {
                    soma += numero;
                    numero += 2;
                }
                Console.WriteLine(soma);
            }
        }
    }
}
