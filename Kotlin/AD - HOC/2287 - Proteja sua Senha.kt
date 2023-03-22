import java.util.Scanner

data class Input(val numbers: List<Pair<Int, Int>>, val sequence: CharArray)

fun main(args: Array<String>) {
    val inputs = mutableListOf<Input>()
    var testNumber = 1

    val scanner = Scanner(System.`in`)

    while (true) {
        val n = scanner.nextInt()
        if (n == 0) break

        inputs.clear()
        for (i in 0 until n) {
            val numbers = readNumbers(scanner)
            val sequence = readSequence(scanner)
            inputs.add(Input(numbers, sequence))
        }

        println("Teste $testNumber")
        testNumber++

        for (k in 0..5) {
            val firstInput = inputs[0]
            val firstNumber = firstInput.numbers[firstInput.sequence[k] - 'A'].first
            val secondNumber = firstInput.numbers[firstInput.sequence[k] - 'A'].second

            var all = 1
            for (i in 1 until n) {
                if (firstNumber != inputs[i].numbers[inputs[i].sequence[k] - 'A'].first &&
                    firstNumber != inputs[i].numbers[inputs[i].sequence[k] - 'A'].second
                ) {
                    all = 0
                }
            }

            if (k != 0) {
                print(" ")
            }
            print(if (all == 1) firstNumber else secondNumber)
        }
        println(" \n")
    }
}

private fun readNumbers(scanner: Scanner): List<Pair<Int, Int>> {
    val numbers = mutableListOf<Pair<Int, Int>>()
    for (j in 0..4) {
        val first = scanner.nextInt()
        val second = scanner.nextInt()
        numbers.add(Pair(first, second))
    }
    return numbers
}

private fun readSequence(scanner: Scanner): CharArray {
    val sequence = CharArray(6)
    for (k in 0..5) {
        sequence[k] = scanner.next()[0]
    }
    return sequence
}
