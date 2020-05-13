/*
* Autor: Pierre Vieira
* Data de submissão:
*/
using System;
using System.Globalization;

namespace URI
{
    class URI
    {
        static void Main(string[] args)
        {
            double a, b, c;
            string triangulo, quadrado, circulo, trapezio, retangulo;
            string[] linha = Console.ReadLine().Split(' ');
            a = double.Parse(linha[0]);
            b = double.Parse(linha[1]);
            c = double.Parse(linha[2]);
            triangulo = formatar((a * c) / 2);
            circulo = formatar(3.14159 * c * c);
            trapezio = formatar(((a + b) * c) / 2);
            quadrado = formatar(b * b);
            retangulo = formatar(a * b);
            Console.WriteLine($"TRIANGULO: {triangulo}\nCIRCULO: {circulo}\nTRAPEZIO: {trapezio}\nQUADRADO: {quadrado}\nRETANGULO: {retangulo}");
        }

        static String formatar(double number)
        {
            return number.ToString("F3", CultureInfo.InvariantCulture);
        }
    }
}