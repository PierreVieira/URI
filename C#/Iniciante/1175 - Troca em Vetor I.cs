/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 22:58:06
*/
using System;
using System.Globalization;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int[] vet = new int[20];
            int aux;
            for (int i = 0; i < 20; i++) {
                vet[i] = int.Parse(Console.ReadLine());
            }
            for (int i = 0; i < 10; i++) {
                aux = vet[i];
                vet[i] = vet[19 - i];
                vet[19 - i] = aux;
            }
            for (int i = 0; i < 20; i++) {
                Console.WriteLine($"N[{i}] = {vet[i]}");
            }
        }
    }
}
