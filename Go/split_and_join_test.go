package main

// Import packages required for testing.
import (
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

// Create a test to split the string "This is a test string" and join it with underscores.
func TestSplitJoinString(t *testing.T) {
	want := "This_is_a_test_string"
	got := splitJoinString("This is a test string")
	assert.Equal(t, want, got)
}

// Create a test to assert not equal that the string "This is a test string" is not split and joined with underscores.
func TestSplitJoinStringNotEqual(t *testing.T) {
	want := "This is a test string"
	got := splitJoinString("This is a test string")
	assert.NotEqual(t, want, got)
}

// Create a function to split the string and join it with underscores.

func splitJoinString(s string) string {
	return strings.Join(strings.Split(s, " "), "_")
}

// Create a test function to test if a number is prime with.
func TestIsPrime(t *testing.T) {
	want := true
	got := isPrime(7)
	assert.Equal(t, want, got)
}

// Create a test function to assert that the number passed is not prime.
func TestIsPrimeNotEqual(t *testing.T) {
	want := false
	got := isPrime(8)
	assert.NotEqual(t, want, got)
}

// Create a function to test if a number is prime with a integer passed as parameter.
func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i < n/2+1; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
