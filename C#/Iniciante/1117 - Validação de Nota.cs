/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 14:34:38
*/
using System;
using System.Globalization;

namespace URI {
    class URI {
        static void Main(string[] args)
        {
            double x, y;
            while (true)
            {
                x = double.Parse(Console.ReadLine());
                if (x < 0 || x > 10)
                {
                    Console.WriteLine("nota invalida");
                }
                else
                {
                    break;
                }
            }
            while (true)
            {
                y = double.Parse(Console.ReadLine());
                if (y < 0 || y > 10)
                {
                    Console.WriteLine("nota invalida");
                }
                else
                {
                    break;
                }
            }
            Console.WriteLine($"media = {(0.5*(x + y)).ToString("F2", CultureInfo.InvariantCulture)}");
        }
    }
}
