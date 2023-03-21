/*
* Autor: Pierre Vieira
* Data de submissão: 20/03/2023 02:22:48
*/

fun main(args: Array<String>) {
    repeat(readLine()!!.toInt()) {
        val line = readLine()!!.split(" ")
        val initialConfig = line.first()
        val c = line[1].toLong()
        println(solve(initialConfig, c))
    }
}

fun decide(element: Pair<Char, Long>): Char {
    return when {
        element.first == 'X' && element.second % 2 == 0L -> 'X'
        element.first == 'X' && element.second % 2 == 1L -> 'O'
        element.first == 'O' && element.second % 2 == 0L -> 'O'
        else -> 'X'
    }
}

fun solve(initialConfig: String, blinks: Long): String {
    val blinkCountList = mutableListOf(blinks)
    val offCountList = mutableListOf(if (initialConfig[0] == 'X') blinks / 2 else (blinks + 1) / 2)

    for (i in 1 until initialConfig.length) {
        blinkCountList.add(offCountList[i - 1])
        val lastBlink = blinkCountList.last()
        offCountList.add(if (initialConfig[i] == 'X') lastBlink / 2 else (lastBlink + 1) / 2)
    }

    val mapping = initialConfig.mapIndexed { index, char -> char to blinkCountList[index] }
    return mapping.map(::decide).joinToString("")
}