package aoc.day06

import java.io.File
import kotlin.collections.map
import kotlin.text.trim

fun main() {
    val inputs = File("inputs/day06.txt").readLines()

    println("Part 1: ${part1(inputs)}")
     println("Part 2: ${part2(inputs)}")
}


fun part1(inputs: List<String>): Long {
    val mappedInput = inputs.map{ it -> it.trim().split(" ").filter{ it.isNotEmpty() }}
    val problems = mutableListOf<List<String>>()
    for (i in 0 until mappedInput[0].size){
        problems.add(
            mappedInput.map { it[i] }
        )
    }

    var final = 0L

    for (problem in problems) {
        if (problem.last() == "+"){
            final+= problem.dropLast(1).map(String::toLong)
                .reduce{acc, value -> acc + value }
        } else if (problem.last() == "*"){
            final+= problem.dropLast(1).map(String::toLong)
                .reduce{acc, value -> acc * value }
        }
    }

    return final

}

fun part2(inputs: List<String>): Long  {

    val maxLength = inputs.maxOf{ it.length }
    val mappedInput = inputs.map { str ->
        str.padEnd(maxLength, ' ').split("")
    }

    val stretched = mappedInput[0].indices.map { i ->
        mappedInput.dropLast(1).joinToString("") { it[i] }
    }

    val problems = mutableListOf<List<String>>()
    var current = mutableListOf<String>()

    for (value in stretched) {
        if (value.isBlank()) {
            if (current.isNotEmpty()) {
                problems.add(current)
                current = mutableListOf()
            }
        } else {
            current.add(value.trim())
        }
    }

    if (current.isNotEmpty()) {
        problems.add(current)
    }

    val operations = mappedInput.last().filter { it.isNotBlank() }
    val reducers: Map<String, (Long, Long) -> Long> = mapOf(
        "+" to Long::plus,
        "*" to Long::times
    )
    return problems.withIndex().sumOf { (index, problem) ->
        problem
            .map(String::toLong)
            .reduce(reducers.getValue(operations[index]))
    }
}



