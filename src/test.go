package main

import (
	"fmt"
)

func main() {
	s := []byte("ne")
	s1 := append(s, 'a')
	s2 := append(s, 'b')
	fmt.Printf("%p %v\n", &s, s)
	fmt.Printf("%p %v\n", &s1, s1)
	fmt.Printf("%p %v\n", &s2, s2)
	return
	fmt.Println(s1, "==========", s2)
	fmt.Println(string(s1), "==========", string(s2))
}
