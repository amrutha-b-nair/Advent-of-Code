package aoc.day07

import java.io.File

fun main() {
    val inputs = File("inputs/day07.txt").readLines()
        .map { line ->
            line.trim().split("").filter { it.isNotEmpty() }.toMutableList()
        }.toMutableList()

    println("Part 1: ${part1(inputs)}")
    println("Part 2: ${part2(inputs)}")
}

fun part1(inputs: MutableList<MutableList<String>>): Int {
    val startIndex = inputs[0].indexOf("S")
    var beamPositions = setOf(startIndex)
    val nRows = inputs.size
    val nCols = inputs.first().size
    var currentRow = 1
    var countSplits = 0
    while (currentRow < nRows) {
        val newBeamPositions = mutableSetOf<Int>()
        for (beamPosition in beamPositions) {
            if (inputs[currentRow][beamPosition] == "^") {
                if (beamPosition - 1 >= 0) newBeamPositions.add(beamPosition - 1)
                if (beamPosition + 1 < nCols) newBeamPositions.add(beamPosition + 1)
                countSplits++
            } else newBeamPositions.add(beamPosition)
        }
        beamPositions = newBeamPositions
        currentRow++
    }

    return countSplits
}

fun part2(inputs: List<List<String>>): Long {
    val nRows = inputs.size
    val nCols = inputs[0].size
    val dp = Array(nRows) { LongArray(nCols) }

    val startCol = inputs[0].indexOf("S")
    dp[0][startCol] = 1L

    for (r in 1 until nRows) {
        for (c in 0 until nCols) {
            when (inputs[r][c]) {
                "." -> dp[r][c] += dp[r - 1][c]
                "^" -> {
                    if (c > 0) dp[r][c - 1] = dp[r - 1][c] + dp[r][c - 1]
                    if (c < nCols - 1) dp[r][c + 1] = dp[r - 1][c] + dp[r][c + 1]
                }
            }
        }
    }

    return dp[nRows - 1].sum()
}
