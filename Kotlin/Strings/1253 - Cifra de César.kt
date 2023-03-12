/*
* Autor: Pierre Vieira
* Data de submissão: 06/03/2023 11:29:35
*/

fun main(args: Array<String>) {
    for (i in 0 until readLine()!!.toInt()) {
        val input = readLine()!!
        println(input.dislocate(readLine()!!.toInt()))
    }
}

fun String.dislocate(n: Int) = map { dislocateLetter(it, n) }.joinToString("")

fun dislocateLetter(letter: Char, n : Int): Char {
    val codeA = 'A'.toInt()
    val codeZ = 'Z'.toInt()
    val deslocation = letter.toInt() - n
    val shiftedValue = when {
        deslocation < codeA -> {
            val outdatedFromA = codeA - deslocation
            codeZ - outdatedFromA + 1
        }
        deslocation > codeZ -> {
            val outdatedFromZ = deslocation - codeZ
            codeA + outdatedFromZ - 1
        }
        else -> deslocation
    }
    return shiftedValue.toChar()
}
