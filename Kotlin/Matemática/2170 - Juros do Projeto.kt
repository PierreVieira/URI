/*
* Autor: Pierre Vieira
* Data de submissão: 20/03/2023 03:05:34
*/

fun main(args: Array<String>) {
    var projectCounter = 1
    while (true) {
        val (x, y) = readLine()?.split(" ")?.map { it.toDouble() } ?: break
        val jurosPercentual = ((y / x) - 1) * 100
        println("Projeto $projectCounter:")
        val result = String.format("%.2f", jurosPercentual)
        println("Percentual dos juros da aplicacao: $result %\n")
        projectCounter++
    }
}