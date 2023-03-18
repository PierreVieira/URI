/*
* Autor: Pierre Vieira
* Data de submissão: 13/03/2023 16:06:01
*/

fun main(args: Array<String>) {
    val matrix: MutableList<List<Int>> = mutableListOf()
    repeat(4) {
        matrix.add(readLine()!!.map { it.toString().toInt() })
    }
    println(solution(matrix))
}

private fun solution(matrix: List<List<Int>>): String {
    val matrixByColumn = getMatrixByColumn(matrix)
    return getWord(
        matrixByColumn = matrixByColumn,
        firstSum = matrixByColumn.first().sumDigits(),
        lastSum = matrixByColumn.last().sumDigits()
    )
}

fun getMatrixByColumn(matrix: List<List<Int>>): List<List<Int>> {
    val newMatrix: MutableList<List<Int>> = mutableListOf()
    var currentIndex = 0
    repeat(matrix.first().size) {
        val newLine: MutableList<Int> = mutableListOf()
        matrix.forEach { currentLine ->
            newLine.add(currentLine[currentIndex])
        }
        newMatrix.add(newLine)
        currentIndex++
    }
    return newMatrix
}

private fun getWord(
    matrixByColumn: List<List<Int>>,
    firstSum: Int,
    lastSum: Int
): String {
    var word = ""
    for (i in 1 until matrixByColumn.size - 1) {
        val ascii = (firstSum * matrixByColumn[i].sumDigits() + lastSum) % 257
        word += ascii.toChar()
    }
    return word
}

private fun List<Int>.sumDigits(): Int {
    var string = ""
    forEach {
        string += it
    }
    return string.toInt()
}
