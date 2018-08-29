package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func HelloServer(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello astaxie!")
	log.Print("recieved")
}
func main() {
	logFile, logErr := os.OpenFile("/tmp/a", os.O_CREATE|os.O_RDWR|os.O_APPEND, 0666)
	if logErr != nil {
		fmt.Println(logErr)
		os.Exit(10)
	}
	log.SetOutput(logFile)
	http.HandleFunc("/hello", HelloServer)
	err := http.ListenAndServe(":8888", nil)
	if err != nil {
		log.Fatal("err")
	}
}
