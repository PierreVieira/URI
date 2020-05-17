/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 21:49:40
*/
using System;
using System.Globalization;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int idade, soma_idades, cont;
            double media;
            cont = soma_idades = 0;
            while (true) {
                idade = int.Parse(Console.ReadLine());
                if (idade < 0) {
                    break;
                }
                soma_idades += idade;
                cont += 1;
            }
            media = soma_idades / (double) cont;
            Console.WriteLine(media.ToString("F2", CultureInfo.InvariantCulture));
        }
    }
}
