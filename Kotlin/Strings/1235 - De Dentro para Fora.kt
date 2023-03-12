/*
* Autor: Pierre Vieira
* Data de submissão: 06/03/2023 11:29:35
*/

fun solution(string: String): String {
    var firstHalf = ""
    var secondHalf = ""
    val halfLimit = string.length / 2
    string.forEachIndexed { index: Int, char: Char ->
        if (index < halfLimit) {
            firstHalf += char
        } else {
            secondHalf += char
        }
    }
    return firstHalf.reversed() + secondHalf.reversed()
}

fun main(args: Array<String>) {
    for (i in 0 until readLine()!!.toInt()) {
        println(solution(readLine()!!))
    }
}
