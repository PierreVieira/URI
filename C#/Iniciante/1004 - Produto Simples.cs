/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 11:14:34
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int n1, n2;
            n1 = int.Parse(Console.ReadLine());
            n2 = int.Parse(Console.ReadLine());
            Console.WriteLine("PROD = "+(n1 * n2));
        }
    }
}