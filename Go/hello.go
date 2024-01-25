// Compile: go build hello.go
package main

import "fmt"

// Create a function that takes two integers and returns the sum of them.
func add(x int, y int) int {
	return x + y
}

// Create a main function that calls the add function and prints the result.
func main() {
	fmt.Println(add(42, 13))
}
