/*
* Autor: Pierre Vieira
* Data de submissão: 13/05/2020 14:24:54
*/
using System;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            int dias, meses, anos;
            dias = int.Parse(Console.ReadLine());
            anos = dias / 365;
            dias %= 365;
            meses = dias / 30;
            dias %= 30;
            Console.WriteLine($"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)");
        }
    }
}
