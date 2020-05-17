/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 22:05:30
*/
using System;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int numero;
            numero = int.Parse(Console.ReadLine());
            for (int i = 1; i <= 10; i++) {
                Console.WriteLine($"{i} x {numero} = {numero * i}");
            }
        }
    }
}
