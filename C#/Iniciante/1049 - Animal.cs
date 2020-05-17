/*
* Autor: Pierre Vieira
* Data de submissão: 16/05/2020 13:17:15
*/
using System;
using System.Globalization;
using Microsoft.VisualBasic;

namespace URI {
    class URI {
        static void Main(string[] args) {
            string vertebrado, tipo, come;
            vertebrado = Console.ReadLine();
            tipo = Console.ReadLine();
            come = Console.ReadLine();
            if (vertebrado == "vertebrado") {
                if (tipo == "ave") {
                    if (come == "carnivoro") {
                        Console.WriteLine("aguia");
                    }
                    else {
                        Console.WriteLine("pomba");
                    }
                }
                else {
                    if (come == "onivoro") {
                        Console.WriteLine("homem");
                    }
                    else {
                        Console.WriteLine("vaca");
                    }
                }
            }
            else {
                if (tipo == "inseto") {
                    if (come == "hematofago") {
                        Console.WriteLine("pulga");
                    }
                    else {
                        Console.WriteLine("lagarta");
                    }
                }
                else {
                    if (come == "hematofago") {
                        Console.WriteLine("sanguessuga");
                    }
                    else {
                        Console.WriteLine("minhoca");
                    }
                }
            }
        }
    }
}
