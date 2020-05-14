/*
* Autor: Pierre Vieira
* Data de submissão: 14/05/2020 10:35:07
*/
using System;
using System.Globalization;

namespace URI {
    class URI {
        static void Main(string[] args)
        {
            double salario, ganhou;
            int reajuste;
            salario = double.Parse(Console.ReadLine());
            if (salario < 400.01)
            {
                reajuste = 15;
            }
            else if (salario < 800.01)
            {
                reajuste = 12;
            }
            else if(salario < 1200.01)
            {
                reajuste = 10;
            }
            else if (salario <= 2000)
            {
                reajuste = 7;
            }
            else
            {
                reajuste = 4;
            }

            ganhou = salario * reajuste / (double) 100;
            Console.WriteLine($"Novo salario: {(salario + ganhou).ToString("F2", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"Reajuste ganho: {ganhou.ToString("F2", CultureInfo.InvariantCulture)}");
            Console.WriteLine($"Em percentual: {reajuste} %");
        }
    }
}
