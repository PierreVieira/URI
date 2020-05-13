/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 12:59:08
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int tempo, velocidade_media;
            tempo = int.Parse(Console.ReadLine());
            velocidade_media = int.Parse(Console.ReadLine());
            double distancia = (double) tempo * velocidade_media;
            Console.WriteLine((distancia/12).ToString("F3", CultureInfo.InvariantCulture));
        }
    }
}
