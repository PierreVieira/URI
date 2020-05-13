/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 12:36:42
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int codigo_peca1, numero_pecas1, codigo_peca2, numero_pecas2;
            double valor_1, valor_2, valor_a_pagar;
            string[] linha1, linha2;
            linha1 = Console.ReadLine().Split(' ');
            linha2 = Console.ReadLine().Split(' ');
            codigo_peca1 = int.Parse(linha1[0]);
            codigo_peca2 = int.Parse(linha2[0]);
            numero_pecas1 = int.Parse(linha1[1]);
            numero_pecas2 = int.Parse(linha2[1]);
            valor_1 = double.Parse(linha1[2]);
            valor_2 = double.Parse(linha2[2]);
            valor_a_pagar = valor_1 * numero_pecas1 + valor_2 * numero_pecas2;
            Console.WriteLine($"VALOR A PAGAR: R$ {valor_a_pagar.ToString("F2", CultureInfo.InvariantCulture)}");
        }
    }
}
