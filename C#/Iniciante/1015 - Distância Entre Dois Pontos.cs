/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 13:53:44
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            string[] linha1, linha2;
            double x1, x2, y1, y2, distancia;
            linha1 = Console.ReadLine().Split(' ');
            linha2 = Console.ReadLine().Split(' ');
            x1 = double.Parse(linha1[0]);
            y1 = double.Parse(linha1[1]);
            x2 = double.Parse(linha2[0]);
            y2 = double.Parse(linha2[1]);
            distancia = Math.Sqrt((Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2)));
            Console.WriteLine(distancia.ToString("F4", CultureInfo.InvariantCulture));
        }
    }
}
