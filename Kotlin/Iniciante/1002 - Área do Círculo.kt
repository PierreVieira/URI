/*
* Autor: Pierre Vieira
* Data de submissão: 24/04/2021 16:07:30
*/
import java.lang.Math.pow
import java.math.BigDecimal
import java.math.RoundingMode

fun main(args: Array<String>) {

    val raio = readLine()!!.toDouble()
    val pi = 3.14159
    val area = pi * pow(raio, 2.0)
    val resultado = BigDecimal(area).setScale(4, RoundingMode.HALF_EVEN)
    println("A=$resultado")

}