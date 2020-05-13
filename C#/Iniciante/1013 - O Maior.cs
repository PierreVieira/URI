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
            int a, b, c;
            int maior1, maior;
            string[] linha = Console.ReadLine().Split(' ');
            a = int.Parse(linha[0]);
            b = int.Parse(linha[1]);
            c = int.Parse(linha[2]);
            maior1 = (a + b + Math.Abs(a - b)) / 2;
            maior = (maior1 + c + Math.Abs(maior1 - c)) / 2;
            Console.WriteLine($"{maior} eh o maior");
        }

    }
}
