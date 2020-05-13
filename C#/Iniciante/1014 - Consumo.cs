/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 12:43:53
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int x;
            double y;
            x = int.Parse(Console.ReadLine());
            y = double.Parse(Console.ReadLine());
            Console.WriteLine($"{(x/y).ToString("F3", CultureInfo.InvariantCulture)} km/l");
        }
    }
}
