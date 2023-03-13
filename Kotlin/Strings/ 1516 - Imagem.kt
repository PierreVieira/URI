/*
* Autor: Pierre Vieira
* Data de submissão: 13/03/2023 15:19:49
*/


data class Dimensions(
    val height: Int,
    val width: Int
)

class Matrix(private var dimensions: Dimensions) {

    private var data: MutableList<List<Char>> = mutableListOf()

    fun addLine(line: String) {
        data.add(line.toList())
    }

    fun expand(newDimensions: Dimensions) {
        val heightMultiplier = newDimensions.height / dimensions.height
        val widthMultiplier = newDimensions.width / dimensions.width
        val newData: MutableList<List<Char>> = mutableListOf()
        data.forEach { line ->
            val newLine: MutableList<Char> = mutableListOf()
            line.forEach {
                for (i in 0 until widthMultiplier) {
                    newLine.add(it)
                }
            }
            for (i in 0 until heightMultiplier) {
                newData.add(newLine)
            }
        }
        data = newData
    }

    fun show() {
        data.forEach {
            println(it.joinToString(""))
        }
    }
}

private fun String.asIntValues() = split(" ").map { it.toInt() }

fun main(args: Array<String>) {
    while (true) {
        val (height, width) = readLine()!!.asIntValues()
        if (height == 0 && width == 0) break
        val matrix = Matrix(Dimensions(height, width))
        for (i in 0 until height) {
            matrix.addLine(readLine()!!)
        }
        val (newHeight, newWidth) = readLine()!!.asIntValues()
        matrix.apply {
            expand(Dimensions(newHeight, newWidth))
            show()
        }
        println()
    }
}

