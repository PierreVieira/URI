/*
* Autor: Pierre Vieira
* Data de submissão: 17/05/2020 00:19:09
*/
using System;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int x, z, cont = 1;
            x = int.Parse(Console.ReadLine());
            while (true) {
                z = int.Parse(Console.ReadLine());
                if (z > x) {
                    break;
                }
            }
            while (x <= z) {
                x += x + 1;
                cont++;
            }
            Console.WriteLine(cont+1);
        }
    }
}
