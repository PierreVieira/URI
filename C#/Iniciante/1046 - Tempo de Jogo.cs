/*
* Autor: Pierre Vieira
* Data de submissão: 14/05/2020 10:22:40
*/
using System;
using System.Globalization;

namespace URI {
    class URI {
        static void Main(string[] args) {
            string[] linha = Console.ReadLine().Split(' ');
            int d1, d2;
            d1 = int.Parse(linha[0]);
            d2 = int.Parse(linha[1]);
            if (d1 == d2) {
                Console.WriteLine("O JOGO DUROU 24 HORA(S)");
            }
            else if (d1 < d2)
            {
                Console.WriteLine($"O JOGO DUROU {d2 - d1} HORA(S)");
            }
            else
            {
                Console.WriteLine($"O JOGO DUROU {24 - d1 + d2} HORA(S)");
            }
        }
    }
}
