package main

/*
#include <stdio.h>
#include <stdlib.h>
void print(char *str) {
	printf("%s\n", str);
}
*/
import "C"

func main() {
	cs := C.CString("hello")
	C.print(cs)
}
