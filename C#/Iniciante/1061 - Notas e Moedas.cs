/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 15:28:44
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            string[] linha1 = Console.ReadLine().Split(" ");
            string[] linha2 = Console.ReadLine().Split(" : ");
            string[] linha3 = Console.ReadLine().Split(" ");
            string[] linha4 = Console.ReadLine().Split(" : ");
            int d1, d2, h1, h2, m1, m2, s1, s2, dias, horas, minutos, segundos;
            d1 = int.Parse(linha1[1]);
            d2 = int.Parse(linha3[1]);
            h1 = int.Parse(linha2[0]);
            m1 = int.Parse(linha2[1]);
            s1 = int.Parse(linha2[2]);
            h2 = int.Parse(linha4[0]);
            m2 = int.Parse(linha4[1]);
            s2 = int.Parse(linha4[2]);
            dias = d2 - d1;
            horas = h2 - h1;
            minutos = m2 - m1;
            segundos = s2 - s1;
            if (horas < 0)
            {
                horas += 24;
                dias -= 1;
            }

            if (minutos < 0)
            {
                minutos += 60;
                horas -= 1;
            }

            if (segundos < 0)
            {
                segundos += 60;
                minutos -= 1;
            }

            if(dias < 0)
            {
                dias = 0;
            }
            Console.WriteLine($"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)");
        }
    }
}
