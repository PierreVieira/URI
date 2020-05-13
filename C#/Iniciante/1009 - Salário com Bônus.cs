/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 13:20:10
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            String nome_vendedor;
            double salario, vendas, comissao;
            nome_vendedor = Console.ReadLine();
            salario = double.Parse(Console.ReadLine());
            vendas = double.Parse(Console.ReadLine());
            comissao = 0.15 * vendas;
            Console.WriteLine($"TOTAL = R$ {(comissao + salario).ToString("F2", CultureInfo.InvariantCulture)}");
        }
    }
}
