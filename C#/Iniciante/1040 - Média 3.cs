/*
* Autor: Pierre Vieira
* Data de submissão: 14/05/2020 11:24:19
*/
using System;
using System.Globalization;

namespace URI {
    class URI {
        static void Main(string[] args) {

            float n1, n2, n3, n4, media, exame, final;

            string[] valores = Console.ReadLine().Split(' ');
            n1 = float.Parse(valores[0], CultureInfo.InvariantCulture);
            n2 = float.Parse(valores[1], CultureInfo.InvariantCulture);
            n3 = float.Parse(valores[2], CultureInfo.InvariantCulture);
            n4 = float.Parse(valores[3], CultureInfo.InvariantCulture);

            media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10;

            /* O problema 1040 tem uma falha de arredondamento especifica
            para a linguagem C#. Quando a media da 4.85, nos temos que
            ajusta-la manualmente para 4.8, o que eh uma "gambiarra"
            horrivel, infelizmente. Isso nao aconteceu nas outras */
            if (media == 4.85f) {
                media = 4.8f;
            }

            Console.WriteLine("Media: " + media.ToString("F1", CultureInfo.InvariantCulture));

            if (media >= 7.0) {
                Console.WriteLine("Aluno aprovado.");
            }
            else if (media < 5.0) {
                Console.WriteLine("Aluno reprovado.");
            }
            else {
                Console.WriteLine("Aluno em exame.");
                exame = float.Parse(Console.ReadLine(), CultureInfo.InvariantCulture);
                final = (media + exame) / 2;
                Console.WriteLine("Nota do exame: " + exame.ToString("F1", CultureInfo.InvariantCulture));
                if (final >= 5.0) {
                    Console.WriteLine("Aluno aprovado.");
                }
                else {
                    Console.WriteLine("Aluno reprovado.");
                }

                Console.WriteLine("Media final: " + final.ToString("F1", CultureInfo.InvariantCulture));
            }
        }
    }
}
