/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 12:11:10
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            double n1, n2, n3;
            n1 = 2 * double.Parse(Console.ReadLine());
            n2 = 3 * double.Parse(Console.ReadLine());
            n3 = 5 * double.Parse(Console.ReadLine());
            Console.WriteLine("MEDIA = "+((n1 + n2 + n3)/10).ToString("F1", CultureInfo.InvariantCulture));
        }
    }
}
