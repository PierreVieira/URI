/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 13:25:41
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int raio = int.Parse(Console.ReadLine());
            double volume = (4.0 / 3) * 3.14159 * raio * raio * raio;
            Console.WriteLine($"VOLUME = {volume.ToString("F3", CultureInfo.InvariantCulture)}");
        }
    }
}
