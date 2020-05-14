/*
* Autor: Pierre Vieira
* Data de submissão: 14/05/2020 09:16:54
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            string[] linha = Console.ReadLine().Split(' ');
            int n1, n2, aux;
            n1 = int.Parse(linha[0]);
            n2 = int.Parse(linha[1]);
            if (n2 < n1) {
                aux = n2;
                n2 = n1;
                n1 = aux;
            }

            Console.WriteLine(n2 % n1 == 0 ? "Sao Multiplos" : "Nao sao Multiplos");
        }
    }
}
