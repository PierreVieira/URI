/*
* Autor: Pierre Vieira
* Data de submissão: 14/05/2020 11:41:01
*/
using System;
using System.Globalization;
using Microsoft.VisualBasic;

namespace URI {
    class URI {
        static void Main(string[] args)
        {
            string[] linha = Console.ReadLine().Split(' ');
            double x, y;
            x = double.Parse(linha[0]);
            y = double.Parse(linha[1]);
            if (x == 0 && y == 0)
            {
                Console.WriteLine("Origem");
            }
            else if (x == 0)
            {
                Console.WriteLine("Eixo Y");
            }
            else if (y == 0)
            {
                Console.WriteLine("Eixo X");
            }
            else if (x < 0 && y < 0)
            {
                Console.WriteLine("Q3");
            }
            else if(x > 0 && y > 0)
            {
                Console.WriteLine("Q1");
            }
            else if (x < 0 && y > 0)
            {
                Console.WriteLine("Q2");
            }
            else
            {
                Console.WriteLine("Q4");
            }
        }
    }
}
