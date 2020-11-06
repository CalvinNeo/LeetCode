package main

import (
    "container/heap"
    "fmt"
)

type IntHeap []int
 
func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) {
    // Push and Pop use pointer receivers because they modify the slice's length,
    // not just its contents.
    *h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}

func nthSuperUglyNumber(n int, primes []int) int {
    h := &IntHeap{1}
    heap.Init(h)
    tot := 0
    mx := 0
    for h.Len() > 0{
        x := (heap.Pop(h)).(int)
        for {
            if x <= mx{
                x = (heap.Pop(h)).(int)
                continue
            }else{
                mx = x
                break
            }
        }
        // fmt.Printf("==> %v", x)
        tot ++
        if tot == n{
            return x
        }else{
            for _, m := range primes{
                heap.Push(h, x * m)
            }
        }
    }
    return 0
}

func main() {
    fmt.Printf("%v\n", nthSuperUglyNumber(12, []int{2,7,13,19}))
}
// func main() {
//     h := &IntHeap{2, 1, 5, 6, 4, 3, 7, 9, 8, 0}  // 创建slice
//     heap.Init(h)  // 初始化heap
//     fmt.Println(*h)
//     fmt.Println(heap.Pop(h))  // 调用pop
//     heap.Push(h, 6)  // 调用push
//     fmt.Println(*h)
//     for len(*h) > 0 {
//         fmt.Printf("%d ", heap.Pop(h))
//     }

// }