/*
* Autor: Pierre Vieira
* Data de submissão: 24/04/2021 16:15:51
*/
fun main(args: Array<String>) {
    var n = readLine()!!.toInt()
    while (n > 0) {
        n--
        val x = readLine()!!.toInt()
        var qtdeDiv = 0
        for (c in 2..(Math.sqrt((x).toDouble()).toInt() + 1)) {
            if (x % c == 0) {
                qtdeDiv++
            }
        }
        println(if (qtdeDiv == 0) "Prime" else "Not Prime")
    }
}