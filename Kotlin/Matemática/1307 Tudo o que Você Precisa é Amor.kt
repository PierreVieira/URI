fun main(args: Array<String>) {
    for (n in 0 until readLine()!!.toInt()) {
        println(
            "Pair #${n + 1}: ${
                solve(
                    s1 = readLine()!!,
                    s2 = readLine()!!
                )
            }"
        )
    }
}

fun solve(s1: String, s2: String): String {
    val dec1 = s1.toInt(2)
    val dec2 = s2.toInt(2)
    if (dec1 % dec2 == 0) return LOVE_MESSAGE
    for (i in 2 until (dec2 / 2) + 1) {
        if (dec1 % i == 0 && dec2 % i == 0) return LOVE_MESSAGE
    }
    return NO_LOVE_MESSAGE
}

private const val LOVE_MESSAGE = "All you need is love!"
private const val NO_LOVE_MESSAGE = "Love is not all you need!"