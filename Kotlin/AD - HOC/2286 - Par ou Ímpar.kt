/*
* Autor: Pierre Vieira
* Data de submissão: 21/03/2023 00:24:18
*/

fun main(args: Array<String>) {
    var turn = 1
    while (true) {
        val numberOfTurns = readLine()!!.toInt()
        if (numberOfTurns == 0) break
        println("Teste $turn")
        solution(numberOfTurns)
        println()
        turn++
    }
}

private fun solution(numberOfTurns: Int) {
    val firstName = readLine()!!
    val secondName = readLine()!!
    repeat(numberOfTurns) {
        val sum = readLine()!!.split(" ").map { it.toInt() }.sum()
        println(if (sum.isEven()) firstName else secondName)
    }
}

private fun Int.isEven(): Boolean = this % 2 == 0