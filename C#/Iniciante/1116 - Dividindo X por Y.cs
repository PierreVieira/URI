/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 14:47:07
*/
using System;
using System.Globalization;

namespace URI {
    class URI {
        static void Main(string[] args) {
            string[] linha;
            int x, y, n;
            n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n; i++) {
                linha = Console.ReadLine().Split(' ');
                x = int.Parse(linha[0]);
                y = int.Parse(linha[1]);
                if (y != 0) {
                    Console.WriteLine($"{(x / (double)y).ToString("F1", CultureInfo.InvariantCulture)}");
                }
                else {
                    Console.WriteLine("divisao impossivel");
                }
            }
        }
    }
}
