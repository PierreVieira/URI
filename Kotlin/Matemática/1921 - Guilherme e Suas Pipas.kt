/*
* Autor: Pierre Vieira
* Data de submissão: 12/03/2023 01:12:20
*/

import java.math.BigDecimal

fun main(args: Array<String>) {
    val n = readLine()!!.toBigDecimal()
    println((n.multiply(n.subtract(BigDecimal(3)))).divide(BigDecimal(2)))
}