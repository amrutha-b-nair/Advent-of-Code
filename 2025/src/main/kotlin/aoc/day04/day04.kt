package aoc.day04

import java.io.File
import java.io.Serializable

fun main() {
    val inputs = File("2025/inputs/day04.txt")
        .readLines()
        .map { line ->
            line.trim().split("").filter { it.isNotEmpty() }.toMutableList()
        }.toMutableList()
    println(inputs)
    println("Part 1: ${part1(inputs)}")
    println("Part 2: ${part2(inputs)}")
}


fun part1(inputs: List<List<String>>): Int {
    var count = 0
    val nRows = inputs.size
    val nCols = inputs[0].size
    println("$nRows, $nCols")
    for (i in 0..nRows-1){
        for (j in 0..nCols-1){
            if(isAccessible(inputs,nRows, nCols, i, j)) {
                count++
            }
        }
    }
    return count
}

fun part2(inputs: MutableList<MutableList<String>>): Int {
    var totalCount = 0
    var count: Int
    val nRows = inputs.size
    val nCols = inputs[0].size
    println("$nRows, $nCols")
    do {
        count = 0
        var accessiblePos = mutableListOf<List<Int>>()
        for (i in 0..nRows - 1) {
            for (j in 0..nCols - 1) {
                if (isAccessible(inputs, nRows, nCols, i, j)) {
                    count++
                    accessiblePos.add(listOf(i,j))
                }
            }
        }
        for (pos in accessiblePos){
            inputs[pos[0]][pos[1]] = "."
        }
        totalCount+=count

    } while (count > 0)
    return totalCount
}



fun isAccessible(grid: List<List<String>>, nRows: Int, nCols: Int, x: Int, y: Int ): Boolean {
    if (grid[x][y] != "@") {
        return false
    }
    var count = 0
    for (i in -1..1){
        for (j in -1..1){
            if (!(i == 0 && j == 0)&& (x+i) in 0..nRows-1 && (y+j) in 0..nCols-1){
                if (grid[x+i][y+j] == "@") {
                    count++
                    if (count > 3) return false
                }
            }
        }
    }
    return true
}
