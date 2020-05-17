/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 22:12:04
*/
using System;

namespace URI {
    class Program {
        static void Main(string[] args) {
            int n1, n2, aux, sum = 0;
            n1 = int.Parse(Console.ReadLine());
            n2 = int.Parse(Console.ReadLine());
            if (n2 < n1) {
                aux = n1;
                n1 = n2;
                n2 = aux;
            }
            n1++;
            if (n1 % 2 == 0) {
                n1++;
            }
            for (int i = n1; i < n2; i+=2) {
                sum += i;
            }
            Console.WriteLine(sum);
        }
    }
}
