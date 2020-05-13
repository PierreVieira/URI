/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 14:06:35
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int n, q100, q50, q20, q10, q5, q2, q1;
            n = int.Parse(Console.ReadLine());
            Console.WriteLine(n);
            q100 = n / 100;
            n -= 100 * q100;
            q50 = n / 50;
            n -= 50 * q50;
            q20 = n / 20;
            n -= 20 * q20;
            q10 = n / 10;
            n -= 10 * q10;
            q5 = n / 5;
            n -= 5 * q5;
            q2 = n / 2;
            n -= 2 * q2;
            q1 = n;
            Console.WriteLine($"{q100} nota(s) de R$ 100,00");
            Console.WriteLine($"{q50} nota(s) de R$ 50,00");
            Console.WriteLine($"{q20} nota(s) de R$ 20,00");
            Console.WriteLine($"{q10} nota(s) de R$ 10,00");
            Console.WriteLine($"{q5} nota(s) de R$ 5,00");
            Console.WriteLine($"{q2} nota(s) de R$ 2,00");
            Console.WriteLine($"{q1} nota(s) de R$ 1,00");
        }
    }
}
