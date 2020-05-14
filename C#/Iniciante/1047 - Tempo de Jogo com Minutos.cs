/*
* Autor: Pierre Vieira
* Data de submissão: 14/05/2020 14:24:50
*/
using System;
using System.Globalization;
using Microsoft.VisualBasic;

namespace URI {
    class URI {
        static void Main(string[] args)
        {
            string[] linha = Console.ReadLine().Split(' ');
            int a, b, c, d, instante_inicial, instante_final, duracao, duracao_horas, duracao_minutos;
            a = int.Parse(linha[0]);
            b = int.Parse(linha[1]);
            c = int.Parse(linha[2]);
            d = int.Parse(linha[3]);
            instante_inicial = a * 60 + b;
            instante_final = c * 60 + d;
            if (instante_inicial < instante_final)
            {
                duracao = instante_final - instante_inicial;
            }
            else
            {
                duracao = (24 * 60 - instante_inicial) + instante_final;
            }

            duracao_horas = duracao / 60;
            duracao_minutos = duracao % 60;

            Console.WriteLine($"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)" );
        }
    }
}
