/*
* Autor: Pierre Vieira
* Data de submissão: 20/03/2023 03:26:37
*/

import java.util.Scanner

fun main(args: Array<String>) {
    val scanner = Scanner(System.`in`)
    val n = scanner.nextInt()
    val v = IntArray(101)
    val vis = BooleanArray(101)

    for (i in 0 until n) {
        v[i] = scanner.nextInt()
    }

    var ans = 1
    for (i in 0 until n) {
        if (!vis[i]) {
            val tam = getTam(i, v, vis)
            ans = ans / gcd(ans, tam) * tam
        }
    }

    println(ans)
}

private fun getTam(i: Int, v: IntArray, vis: BooleanArray, tam: Int = 0): Int {
    if (vis[i]) return tam
    vis[i] = true
    return getTam(v[i] - 1, v, vis, tam + 1)
}

private fun gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)