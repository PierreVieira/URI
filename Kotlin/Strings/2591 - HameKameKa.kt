/*
* Autor: Pierre Vieira
* Data de submissão: 18/03/2023 16:28:39
*/

fun main(args: Array<String>) {
    repeat(readLine()!!.toInt()) {
        println(solution(readLine()!!))
    }
}

fun solution(input: String): String = "k" + generateA(calculateQuantitiesA(input))

fun generateA(calculateQuantitiesA: Int): String {
    var string = ""
    repeat(calculateQuantitiesA) {
        string += 'a'
    }
    return string
}

fun calculateQuantitiesA(input: String): Int {
    val quantityAfterH = identifyQuantityAfterLetter('h', input)
    val quantityAfterK = identifyQuantityAfterLetter('k', input)
    return quantityAfterH * quantityAfterK
}

fun identifyQuantityAfterLetter(c: Char, input: String): Int {
    val firstIndex = input.indexOf(c) + 1
    var sum = 0
    for (i in firstIndex until input.length) {
        if (input[i] != 'a') break
        sum++
    }
    return sum
}
