package main

import "fmt"
import "math"

type Vertex struct {
	X, Y float64
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
func main() {
	x := Vertex{3, 4}
	fmt.Println(x.Abs())
}
