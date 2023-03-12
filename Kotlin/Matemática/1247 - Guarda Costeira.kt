/*
* Autor: Pierre Vieira
* Data de submissão: 11/03/2023 22:42:31
*/

import kotlin.math.pow
import kotlin.math.sqrt

fun main(args: Array<String>) {
    while (true) {
        try {
            val (D, VF, VG) = readLine()!!.split(" ").map { it.toDouble() }
            println(result(D, VF, VG))
        } catch (e: NullPointerException) {
            break
        }
    }
}

fun result(d: Double, vf: Double, vg: Double): String {
    val tf = 12.0 / vf
    val hypotenuse = sqrt(d.pow(2.0) + 144.0)
    val tg = hypotenuse / vg
    return if (tg <= tf) "S" else "N"
}