/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 11:07:23
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            double raio;
            double area;
            raio = double.Parse(Console.ReadLine());
            area = raio * raio * 3.14159;
            Console.WriteLine("A=" + area.ToString("F4", CultureInfo.InvariantCulture));
        }
    }
}
