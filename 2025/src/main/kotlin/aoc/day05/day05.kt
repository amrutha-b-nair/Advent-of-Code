package aoc.day05

import java.io.File
import kotlin.text.trim

fun main() {
    val lines = File("2025/inputs/day05.txt").readLines()

    val parts = lines.joinToString("\n").split("\n\n")

    val ranges = parts[0].lines()
        .map {
            val (start, end) = it.trim().split("-").map(String::toLong)
            start to end
        }
    val ids = parts[1].lines().map { it.trim().toLong() }

    println("Part 1: ${part1(ranges, ids)}")
    println("Part 2: ${part2(ranges)}")
}


fun part1(range: List<Pair<Long, Long>>, ids: List<Long>): Int {
    var count = 0

    for (id in ids){
        for ((start, end) in range) {
            if (id in start..end) {
                count++
                break
            }
        }
    }
    return count
}

fun part2(ranges: List<Pair<Long, Long>>): Long {
    var total = 0L

    val sorted = ranges.sortedBy { it.first }
    var currentStart = sorted[0].first
    var currentEnd = sorted[0].second

    for ((start, end) in sorted.subList(1, sorted.size)) {
        if (start <= currentEnd) {
            currentEnd = maxOf(end, currentEnd)
        } else {
            total += currentEnd - currentStart + 1
            currentStart = start
            currentEnd = end
        }
    }

    total += currentEnd - currentStart + 1


    return total
}


