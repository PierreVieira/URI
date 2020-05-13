/*
* Autor: Pierre Vieira
* Data de submissão:
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int a, b, c, d;
            string[] linha;
            linha = Console.ReadLine().Split(' ');
            a = int.Parse(linha[0]);
            b = int.Parse(linha[1]);
            c = int.Parse(linha[2]);
            d = int.Parse(linha[3]);
            if (b > c && d > a && c + d > a + b && c > 0 && d > 0 && a % 2 == 0)
            {
                Console.WriteLine("Valores aceitos");
            }
            else
            {
                Console.WriteLine("Valores nao aceitos");
            }
        }
    }
}
