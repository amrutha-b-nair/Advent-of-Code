package aoc.day02

import java.io.File
import kotlin.math.pow

fun main() {
    val inputs = File("2025/inputs/day02.txt")
        .readText()
        .trim()
        .split(",")
        .map { it.trim().split("-").map(String::toLong) }

    println("Part 1: ${part1(inputs)}")
    println("Part 2: ${part2(inputs)}")
}

fun part1(inputs: List<List<Long>>): Long {
    var totalCount = 0L
    for (input in inputs) {
        totalCount += processInput(input)
    }
    return totalCount
}


fun processInput(input: List<Long>): Long {
    var start = input[0]
    val end = input[1]
    var count = 0L

    val startLength = input[0].toString().length
    val endLength = input[1].toString().length

    start = getFirstMatch(start, end) ?: return 0L
    for (len in startLength..endLength) {
        val endDigit = minOf(10.0.pow(len).toLong() - 1, end)
        if (len % 2 == 1) {
            start =  10.0.pow((len).toDouble()).toLong()
            continue
        }
        val left = start.toString().take(len / 2)
        val match = (left + left).toLong()
        if (match in input[0]..input[1]) {
            val multiple = 10.0.pow(((len + 1) / 2).toDouble()).toLong() + 1
            val times = (endDigit-start)/multiple
            count += match*(times+1) + ((times*(times+1)/2)*multiple)
        }
        start =  10.0.pow((len).toDouble()).toLong()
        continue
    }

    return count
}

fun getFirstMatch(begin: Long, end: Long): Long? {
    var start = begin
    val startLength = start.toString().length
    val endLength = end.toString().length
    while (start <= end) {

        if (startLength % 2 == 1) {
            if (startLength == endLength) return null
            else start =  10.0.pow((startLength).toDouble()).toLong()
        }
        val left = start.toString().take((startLength + 1) / 2)
        val right = start.toString().substring((startLength + 1) / 2)
        val match = (left + left).toLong()
        if (match in begin..end) {
            println(match)
            return match
        }
        start = ((left.toLong() + 1).toString() + right).toLong()
    }
    return null
}



fun part2(inputs: List<List<Long>>): Long {
    var totalCount = 0L
    for (input in inputs) {
        for (value in input[0]..input[1]) {
            if (isAnInvalidId(value.toString())) {
                totalCount += value
            }
        }
    }
    return totalCount
}


fun isAnInvalidId(value: String): Boolean {
    val len = value.length
    for (i in 1..len/2){
        if (len % i != 0) continue
        val repeatBlock = value.take(i)
        if (repeatBlock.repeat(len/i) == value) return true
    }
    return false
}


