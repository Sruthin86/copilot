// Add a package declaration
package main

import (
	"fmt"
)

// Create a function to add two integers and return the result.
func add(a int, b int) int {
	return a + b
}

// Create a function which accepts two integer parameters from the command line and prints the sum.
func main() {
	var a, b int
	fmt.Print("Enter two numbers: ")
	fmt.Scan(&a, &b)
	fmt.Println("Sum: ", add(a, b))
}
