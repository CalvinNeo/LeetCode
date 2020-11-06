package main

import (
    "fmt"
)

func checkStraightLine(coordinates [][]int) bool {
    if len(coordinates) < 2{
        return false
    }
    dx := coordinates[0][0] - coordinates[1][0]
    dy := coordinates[0][1] - coordinates[1][1]
    for _, p := range coordinates[2:] {
        x := p[0]
        y := p[1]
        dx2 := x - coordinates[1][0]
        dy2 := y - coordinates[1][1]
        if dx2 * dy != dy2 * dx {
            return false
        }
    }
    return true
}

func main(){

}