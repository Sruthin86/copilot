package main

import (
	"testing"
	"github.com/stretchr/testify/assert"

)

// Create a test to asset that the function returns a string with a character inserted at a given position.
func TestInjectChar(t *testing.T) {
	want := "Go Green Go White"
	got := "Go reen Go White"
	assert.Equal(t, want, injectChar(got, "G", 3))
}

// Create a test to assert not equal that the function returns a string with a character inserted at a given position.
func TestInjectCharNotEqual(t *testing.T) {
	want := "Go Green Go White"
	got := "Go reen Go White"
	assert.NotEqual(t, want, injectChar(got, "G", 3))
}

// Create a test to assert not equal that the function does not return a string with a character inserted at a given position.
func TestInjectCharNotEqualWithoutChar(t *testing.T) {
	want := "Go Green Go White"
	got := "Go reen Go White"
	assert.NotEqual(t, want, injectChar(got, "G", 3))
}

// Create a function to inject a character at a given position.
func injectChar(s string, c string, i int) string {
	return s[:i] + c + s[i:]
}
