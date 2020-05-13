/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 12:14:40
*/
using System;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int a, b, c, d, diferenca;
            a = int.Parse(Console.ReadLine());
            b = int.Parse(Console.ReadLine());
            c = int.Parse(Console.ReadLine());
            d = int.Parse(Console.ReadLine());
            diferenca = a * b - c * d;
            Console.WriteLine("DIFERENCA = "+diferenca);
        }
    }
}
