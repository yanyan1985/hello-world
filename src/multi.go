package main

import "fmt"
import "time"

func showchild(c chan int) {
	for {
		fmt.Print("child wait\n")
		data := <-c
		fmt.Print("child recieved ")
		fmt.Print(data)
		fmt.Print("\n")
	}
}
func main() {
	c := make(chan int)
	go showchild(c)
	for index := 0; index < 10; index++ {
		c <- index
		fmt.Print("parent send ")
		fmt.Print(index)
		fmt.Print("\n")
		time.Sleep(1000000000)
	}
}
