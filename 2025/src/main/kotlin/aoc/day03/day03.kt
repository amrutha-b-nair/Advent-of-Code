package aoc.day03

import java.io.File

fun main() {
    val inputs = File("2025/inputs/day03.txt")
        .readLines()
    println(inputs)
    println("Part 1: ${part1(inputs)}")
    println("Part 2: ${part2(inputs)}")
}

fun part1(inputs: List<String>): Long {
    var finalVoltage = 0L
    for (input in inputs){
        var first = 0
        var second = 0
        val batteries = input.trim().map { it.digitToInt() }
        for (i in 0..<batteries.size){
            if (batteries[i] > first && i+1 < batteries.size) {
                first = batteries[i]
                second = batteries[i+1]
            } else {
                if (batteries[i] > second) {
                    second = batteries[i]
                }
            }
        }
        finalVoltage += first*10 + second
        println(first*10 + second)
    }
    return finalVoltage
}

fun part2(inputs: List<String>): Long {
    var finalVoltage = 0L
    val batteryCount = 12
    for (input in inputs){
        var batteries = input.trim().map { it.digitToInt() }.toMutableList()
        for(index in 0..batteryCount-1){
            if (batteries.size <= batteryCount) {
                break
            }
            val possible = batteries.subList(index, batteries.size + index-batteryCount+1)
            val result = possible.withIndex().maxBy { it.value }
            batteries = (batteries.take(index) + batteries.subList(result.index+index, batteries.size)).toMutableList()
        }
        println("batteries:::::${ batteries.take(batteryCount).joinToString("").toLong() }")
        finalVoltage += batteries.take(batteryCount).joinToString("").toLong()
    }
    return finalVoltage
}
