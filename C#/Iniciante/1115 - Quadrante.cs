/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 13:53:44
*/
using System;

namespace URI {
    class URI {
        static void Main(string[] args)
        {
            string[] linha;
            int x, y;
            while (true)
            {
                linha = Console.ReadLine().Split(' ');
                x = int.Parse(linha[0]);
                y = int.Parse(linha[1]);
                if (x == 0 || y == 0)
                {
                    break;
                }
                else
                {
                    if (x > 0 && y > 0)
                    {
                        Console.WriteLine("primeiro");
                    }
                    else if (x > 0 && y < 0)
                    {
                        Console.WriteLine("quarto");
                    }
                    else if (x < 0 && y < 0)
                    {
                        Console.WriteLine("terceiro");
                    }
                    else
                    {
                        Console.WriteLine("segundo");
                    }
                }
            }
        }
    }
}
