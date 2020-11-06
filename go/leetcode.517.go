package main

import (
    "fmt"
)


func findMinMovesTLE(machines []int) int {
    s := Sum(machines)
    n := len(machines)
    if s % n != 0{
        return -1
    }
    target := s / n
    ans := 0

    for{
        flag := true
        lb := make([]int, n)
        rb := make([]int, n)
        acc := 0
        for i := 0; i < n; i++{
            t := target * i // 我左边应该有多少衣服，acc为左边实际有多少
            lb[i] = t - acc // 目前i左边的缺口数
            acc += machines[i]
            if lb[i] != 0{
                flag = false
            }
        }
        if flag == true{
            break
        }
        acc = 0
        for i := n - 1; i >= 0; i--{
            t := target * ((n - 1) - i) // 我右边应该有多少衣服，acc为右边实际有多少
            rb[i] = t - acc // 目前i右边的缺口数
            acc += machines[i]
        }
        nm := make([]int, n)
        copy(nm, machines)
        fmt.Printf("lb %v rb %v\n", lb, rb)
        for i := 0; i < n; i++{
            move_left := false
            move_right := false
            if lb[i] > 0 && machines[i] > 0{
                move_left = true
            }
            if rb[i] > 0 && machines[i] > 0{
                move_right = true
            }
            if move_right && move_left{
                // 如果两边都需要移动，那么就看哪边更少
                if machines[i - 1] > machines[i + 1]{
                    move_left = false
                }else{
                    move_right = false
                }
            }
            if move_right{
                nm[i] --
                nm[i + 1] ++
            }else if move_left{
                nm[i] --
                nm[i - 1] ++
            }
        }
        machines = nm
        ans ++
    }
    return ans
}

func Sum(arr [] int) (ans int){
    ans = 0
    for _, x := range arr{
        ans += x
    }
    return ans
}

func Abs(x int) int{
    if x > 0{
        return x
    }
    return -x
}

func Max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func findMinMoves(machines []int) int {
    s := Sum(machines)
    n := len(machines)
    if s % n != 0{
        return -1
    }
    target := s / n
    mx := 0
    balance := 0
    for i := 0; i < n; i++{
        d := machines[i] - target
        balance += d
        mx = Max(mx, Max(Abs(balance), d))
    }
    return mx
}

func main(){
    fmt.Printf("%v\n", findMinMoves([]int{1,0,5})) // 3
    fmt.Printf("%v\n", findMinMoves([]int{0,3,0})) // 2
    fmt.Printf("%v\n", findMinMoves([]int{0,2,0})) // -1
}