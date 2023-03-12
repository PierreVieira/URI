/*
* Autor: Pierre Vieira
* Data de submissão: 06/03/2023 11:13:32
*/

private fun thirdStep(string: String) : String {
    var mappedString = ""
    val limitedIndex = string.length / 2
    string.forEachIndexed { index: Int, char: Char ->
        mappedString += if (index >= limitedIndex) char.dislocate(-1) else char
    }
    return mappedString
}

private fun secondStep(string: String) : String = string.reversed()

private fun firstStep(string: String) : String {
    var mappedString = ""
    string.forEach {
        mappedString += if (it.isLowerCase() || it.isUpperCase()) it.dislocate(3).toString() else it
    }
    return mappedString
}

private fun Char.dislocate(positions: Int): Char = (toInt() + positions).toChar()

fun main(args: Array<String>) {
    for (i in 0 until readLine()!!.toInt()) {
        val input = readLine()!!
        val mappedInput = thirdStep(secondStep(firstStep(input)))
        println(mappedInput)
    }
}