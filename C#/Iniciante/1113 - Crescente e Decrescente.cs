/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 13:40:12
*/
using System;
using System.Globalization;
using Microsoft.VisualBasic;

namespace URI {
    class URI {
        static void Main(string[] args)
        {
            string[] linha;
            int x, y;
            do
            {
                linha = Console.ReadLine().Split(' ');
                x = int.Parse(linha[0]);
                y = int.Parse(linha[1]);
                if (x > y)
                {
                    Console.WriteLine("Decrescente");
                }
                else if (x < y)
                {
                    Console.WriteLine("Crescente");
                }
            } while (x != y);
        }
    }
}
