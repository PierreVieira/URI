/*
* Autor: Pierre Vieira
* Data de submissão: 14/05/2020 13:11:24
*/
using System;
using System.Globalization;
using Microsoft.VisualBasic;

namespace URI {
    class URI {
        static void Main(string[] args)
        {
            string[] linha = Console.ReadLine().Split(' ');
            double a, b, c;
            a = double.Parse(linha[0]);
            b = double.Parse(linha[1]);
            c = double.Parse(linha[2]);
            double[] vetor = {a, b, c};
            Array.Sort(vetor);
            a = vetor[2];
            b = vetor[1];
            c = vetor[0];
            if (a >= b + c || b >= a + c || c >= a + b)
            {
                Console.WriteLine("NAO FORMA TRIANGULO");
            }
            else
            {
                if (a * a == b * b + c * c) {
                    Console.WriteLine("TRIANGULO RETANGULO");
                }
                else if (a * a > b * b + c * c) {
                    Console.WriteLine("TRIANGULO OBTUSANGULO");
                }
                else if (a * a < b * b + c * c) {
                    Console.WriteLine("TRIANGULO ACUTANGULO");
                }
                if (a == b && b == c)
                {
                    Console.WriteLine("TRIANGULO EQUILATERO");
                }
                else if (a == b || a == c || b == c){
                    Console.WriteLine("TRIANGULO ISOSCELES");
                }
            }
        }
    }
}
