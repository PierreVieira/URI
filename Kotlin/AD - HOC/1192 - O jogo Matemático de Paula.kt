/*
* Autor: Pierre Vieira
* Data de submissão: 24/04/2021 16:57:09
*/
fun main(args: Array<String>) {
    val n = readLine()!!.toInt()
    for (i in 1..n) {
        val line = readLine()!!.toCharArray()
        val n1 = line[0].toString().toInt()
        val letra = line[1]
        val n2 = line[2].toString().toInt()
        println(
            when {
                n1 == n2 -> n1 * n2
                letra.toLowerCase() == letra -> n1 + n2
                else -> n2 - n1
            }
        )
    }
}
