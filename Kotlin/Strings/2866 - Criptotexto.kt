/*
* Autor: Pierre Vieira
* Data de submissão: 18/03/2023 16:44:58
*/

fun main(args: Array<String>) {
    repeat(readLine()!!.toInt()) {
        solution(readLine()!!)
        println()
    }
}

private fun solution(input: String) {
    for (i in (input.length - 1) downTo 0) {
        val currentChar = input[i]
        if (currentChar.isLowerCase()) print(currentChar)
    }
}