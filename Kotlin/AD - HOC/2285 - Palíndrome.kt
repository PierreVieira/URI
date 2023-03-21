/*
* Autor: Pierre Vieira
* Data de submissão: 21/03/2023 00:39:17
*/

fun main(args: Array<String>) {
    var testNumber = 1

    while (true) {
        val n = readLine()!!.toInt()
        if (n == 0) break
        val s = readLine()!!
        val dp = IntArray(n + 1) { Int.MAX_VALUE }
        dp[0] = 0
        for (i in 1..n) {
            for (j in 0 until i) {
                if (isPalindrome(s, j, i - 1)) {
                    dp[i] = minOf(dp[i], dp[j] + 1)
                }
            }
        }
        println("Teste $testNumber")
        println(dp[n])
        println()
        testNumber++
    }
}

private fun isPalindrome(s: String, i: Int, j: Int): Boolean {
    var start = i
    var end = j
    while (start < end) {
        if (s[start] != s[end]) {
            return false
        }
        start++
        end--
    }
    return true
}