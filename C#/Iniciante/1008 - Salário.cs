/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 12:28:28
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int numero_funcionario, qtde_horas_trabalhads;
            double valor_recebido_por_hora_trabalhada;
            numero_funcionario = int.Parse(Console.ReadLine());
            qtde_horas_trabalhads = int.Parse(Console.ReadLine());
            valor_recebido_por_hora_trabalhada = double.Parse(Console.ReadLine());
            Console.WriteLine($"NUMBER = {numero_funcionario}\nSALARY = U$ {(qtde_horas_trabalhads*valor_recebido_por_hora_trabalhada).ToString("F2", CultureInfo.InvariantCulture)}");
        }
    }
}
