package main

import (
	"strings"
	"testing"
	"github.com/stretchr/testify/assert"
)

// Create a function to test split a string and join it back together with an underscore.
func TestSplitAndJoin(t *testing.T) {
	want := "this_is_a_string"
	got := "this is a string"
	assert.Equal(t, want, splitAndJoin(got, " "))
}

// Create a function to test not equal split a string and join it back together with an underscore.
func TestSplitAndJoinNotEqual(t *testing.T) {
	want := "this_is_a_string"
	got := "this is a string"
	assert.NotEqual(t, want, splitAndJoin(got, " "))
}

// Create a function to test not equal split a string and join it back together without underscore.
func TestSplitAndJoinNotEqualWithoutUnderscore(t *testing.T) {
	want := "this is a string"
	got := "this is a string"
	assert.NotEqual(t, want, splitAndJoin(got, " "))
}	

// Create a function to split a string on space and join it back together with an underscore.

func splitAndJoin(s string, sep string) string {
	split := strings.Split(s, sep)
	return strings.Join(split, "_")	
}
