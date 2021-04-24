/*
* Autor: Pierre Vieira
* Data de submissão: 24/04/2021 16:38:48
*/
import java.util.*


fun mdc(n1: Int, n2: Int): Int {
    var n1 = n1
    var n2 = n2
    var aux: Int
    while (n2 % n1 != 0) {
        aux = n2
        n2 = n1
        n1 = aux % n1
    }
    return n1
}

fun main(args: Array<String>) {
    val teclado = Scanner(System.`in`)
    var x: Int
    var y: Int
    var aux: Int
    var line: Array<String>
    val n: Int = teclado.nextInt()
    teclado.nextLine()
    for (i in 0 until n) {
        line = teclado.nextLine().split(" ".toRegex()).toTypedArray()
        x = line[0].toInt()
        y = line[1].toInt()
        if (x > y) {
            aux = x
            x = y
            y = aux
        }
        println(mdc(x, y))
    }
}
