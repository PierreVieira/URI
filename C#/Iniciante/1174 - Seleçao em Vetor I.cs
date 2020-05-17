/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 22:51:36
*/
using System;
using System.Globalization;

namespace URI {
    class Program {
        static void Main(string[] args) {
            double[] vet = new double[100];
            for (int i = 0; i < 100; i++) {
                vet[i] = double.Parse(Console.ReadLine());
            }
            for (int i = 0; i < 100; i++) {
                if (vet[i] <= 10) {
                    Console.WriteLine($"A[{i}] = {(vet[i]).ToString("F1")}");
                }
            }
        }
    }
}
