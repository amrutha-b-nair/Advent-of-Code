package aoc.day01

import java.io.File

fun main() {
    val input = File("2025/inputs/day01.txt").readLines()
    println(input)
    println("Part 1: ${part1(input)}")
    println("Part 2: ${part2(input)}")
}
fun part1(inputs: List<String>): Int {
    var zeroCount = 0
    var currentPos = 50
    for (input in inputs) {
       val letter = input[0]
        val dist = input.substring(1).toInt()
        currentPos = if (letter == 'L') {
            (currentPos + 100 - dist) % 100
        } else {
            (currentPos + dist) % 100
        }
        if (currentPos == 0) zeroCount += 1
    }

    return zeroCount
}


fun part2(inputs: List<String>): Any {
    var zeroCount = 0
    var currentPos = 50
    for (input in inputs) {
        val dist = input.substring(1).toInt()

        if (input[0] == 'L') {
            zeroCount += dist / 100
            val steps = 100 - (dist % 100)
            val newPos = (currentPos + steps) % 100
            if ((currentPos in 1..< newPos) || newPos == 0) zeroCount += 1
            currentPos = newPos
        } else  if (input[0] == 'R') {
            val rawNewPos = (currentPos + dist)
            zeroCount += rawNewPos / 100
            currentPos = rawNewPos % 100
        }
    }
    return zeroCount
}


