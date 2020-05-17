/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 22:43:28
*/
using System;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int[] vet = new int[10];
            int number;
            number = int.Parse(Console.ReadLine());
            vet[0] = number;
            for (int i = 1; i < 10; i++) {
                vet[i] = vet[i - 1] * 2;
            }
            for (int i = 0; i < 10; i++) {
                Console.WriteLine($"N[{i}] = {vet[i]}");
            }
        }
    }
}
