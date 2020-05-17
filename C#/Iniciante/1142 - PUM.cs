/*
* Autor: Pierre Vieira
* Data de submissão: 17/05/2020 00:09:58
*/
using System;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int number;
            int[] vet = { 1, 2, 3 };
            number = int.Parse(Console.ReadLine());
            for (int i = 0; i < number; i++) {
                for (int j = 0; j < 3; j++) {
                    Console.Write(vet[j]+" ");
                    vet[j]+=4;
                }
                Console.WriteLine("PUM");
            }
        }
    }
}
