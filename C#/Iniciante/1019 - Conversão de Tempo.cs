/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 14:19:56
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int horas, minutos, segundos;
            segundos = int.Parse(Console.ReadLine());
            horas = segundos / 3600;
            segundos %= 3600;
            minutos = segundos / 60;
            segundos %= 60;
            Console.WriteLine(horas+":"+minutos+":"+segundos);
        }
    }
}
