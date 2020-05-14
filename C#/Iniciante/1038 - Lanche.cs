/*
* Autor: Pierre Vieira
* Data de submissão: 14/05/2020 09:02:20
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int codigo, quantidade;
            double[] precos = {4.00, 4.50, 5.00, 2.00, 1.50};
            string[] linha = Console.ReadLine().Split(' ');
            codigo = int.Parse(linha[0]);
            quantidade = int.Parse(linha[1]);
            Console.WriteLine($"Total: R$ {(quantidade*precos[codigo - 1]).ToString("F2", CultureInfo.InvariantCulture)}");
        }
    }
}
