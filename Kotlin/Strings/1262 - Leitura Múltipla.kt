/*
* Autor: Pierre Vieira
* Data de submissão: 12/03/2023 00:11:36
*/

fun main(args: Array<String>) {
    while (true) {
        val rastro = readLine() ?: break
        val p = readLine()?.toInt() ?: break
        println(solve(rastro, p))
    }
}

fun solve(rastro: String, p: Int): Int {
    var string = ""
    var cont = 0
    rastro.forEach {
        if (it == 'W') {
            if (string.isNotEmpty()) {
                cont++
            }
            cont++
            string = ""
        } else {
            string += it
            if (string.length == p) {
                cont++
                string = ""
            }
        }
    }
    if (string.isNotEmpty()) {
        cont++
    }
    return cont
}