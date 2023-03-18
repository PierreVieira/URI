/*
* Autor: Pierre Vieira
* Data de submissão: 18/03/2023 15:27:42
*/

fun main(args: Array<String>) {
    val pi = 3.141592654
    while (true) {
        val (a, b, c) = readLine()?.split(" ")?.map { it.toDouble() } ?: break
        val result: Double = 5 * ((tan(a * (pi / 180)) * b) + c)
        val resultString = String.format("%.2f", result)
        println(resultString)
    }
}