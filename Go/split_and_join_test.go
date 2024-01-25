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

// Create a function to split a string on space and join it back together with an underscore.

func splitAndJoin(s string, sep string) string {
	return strings.Join(strings.Split(s, sep), "_")
}
