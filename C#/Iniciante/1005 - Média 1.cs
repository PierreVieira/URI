/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 11:18:27
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            double n1, n2;
            n1 = 3.5*double.Parse(Console.ReadLine());
            n2 = 7.5*double.Parse(Console.ReadLine());
            Console.WriteLine("MEDIA = "+((n1 + n2)/11).ToString("F5", CultureInfo.InvariantCulture));
        }
    }
}
