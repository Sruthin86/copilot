# GitHub-Copilot


## Introduction

- GitHub Copilot is "AI pair programmer for your code".
- GitHub Copilot is a result collaboration between GitHub and OpenAI.
- At it's core Copilot is a model trained on publicly available repositories on GitHub, paired with natural language processing techniques.
- It supports most programming languages but it performs better with Python, C, C++, JavaScript, TypeScript, GO, etc.
- Copilot's prompts can be entered in English, Chinese, French, German, Italian, Japanese, Portuguese, Spanish.
- Copilot can be installed as a [Visual Studio Plugin](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-extension?view=vs-2022).

## Prompts in natural language to generate HTML
- Create a basic HTML page
```
<!-- Create a basic html page-->
```
- Create headings and list items
```
<!-- Add a 2nd level heading to the page-->
<!-- Create a list with 6 items-->
```
- Add images and links
```
<!-- Add an image of MSU Beaumount Tower -->
<!-- Add a link to the MSU website -->
```
- Create a columned layout
```
 <!-- Create a 3 column layout for text-->
```
- Create forms
```
<!-- Create a form that accepts name, email, and phone number-->
<!-- Create a phone number input field which accepts 10 digits in xxx-xxx-xxxx format with a placeholder xxx-xxx-xxxx -->
<!-- Add a dropdown for Affiliation with Undergraduate, Graduate, Staff, and Faculty options -->
```
- Adding stylesheets
```
<!-- Add Bootstrap -->
<!-- Add test.css -->
```
- Create responsive columns
```
<!-- Create a 3 column layout that switches to 1 column on mobile devices -->
```
- Create popup modals
```
<!-- Create a modal box with a button to close it-->
```

## Prompts in natural language to generate basic functions in Python

- Create some basic functions and call them from the command line.
```
# Create a function to print hello world

# Create a function to call hello_world function from command line

# pass two integers from command line and add them

# import sys module to read command line arguments
```
- Create a function to get the count of numbers grater than the previous one in the list.
```

# create a list of 7 three digit random numbers

# Create a function to find out how many numbers in the list are larger than the previous number and return the count.

```
### Test Driven Development
- Create a test class before writing the function and create a function based on the test.
```
# Create a test class to test the area of the triangle

# Create a test using assert not equal

# Create a function to test the area of a triangle

# Create a function to test the area of a triangle

# Create a test class to test the  better count larger numbers function

```

## Prompts in natural language to analyze large datasets using Jupyter Notebook

- Import packages that are necessary to load, process, and analyze large sets of data
```
# Import packages to load large data sets and create plots

```
- Get the titanic dataset and read the dataframe
```
# Assign Titanic dataset url to a variable

# Read the data into a pandas dataframe

# Print the first 5 rows of the data frame
```
- Analyze the data
```
# Compute how many passengers survived and print the value in a human-friendly format

# Compute how many passengers survived and print the value in a human-friendly format
```
- Create visualizations.
```
# Create a visualization of the corelation between the pclass and passengers who survived and did not survive
```

## Prompts in natural language to generate basic functions using GO

- Create some basic functions in GO
```
// Create a function that takes two integers and returns the sum of them.

// Create a function that calls the add function and prints the result from the command line.

// Create a function which accepts two integer parameters from the command line and prints the sum.

Refactored sample code

func main() {
	total_args := len(os.Args[1:])
	fmt.Println("Total Args =", total_args)
	args := os.Args
	// Convert string to int
	a, _ := strconv.Atoi(args[1])
	b, _ := strconv.Atoi(args[2])
	fmt.Println("Sum =", add(a, b))
}
```
### Writing tests
- Create a test for joining a string with an underscore
```
// Create a function to test split a string and join it back together with an underscore.

// Create a test that tests the not equal condition for the split and join function.

// Create a function to split a string on space and join it back together with an underscore.

// Create a test function to test if a number is prime.

// Create a function to test if a number is prime.

// Create a test function to assert that the number passed is not prime.

```
- Create a function to inject chars at a position and test it
```
// Create a function to inject a character at a given position.

// Create a test to assert that the function returns a string with a character inserted at a given position.

// Create a test to assert not equal that the function returns a string with a character inserted at a given position.

```
## Copilot on the Command Line
- `gh` is GitHub on command line. For installation instructions for GitHub CLI, see the [GitHub CLI repository](https://github.com/cli/cli#installation).
- Add the Copilot extension using `gh extension install github/gh-copilot`.
- Login to your GitHub on the CLI using `gh auth login` or `gh auth login --web -h github.com`.
- Copilot is capable of "explaning" or "suggesting" commands
```
 gh copilot explain "Chmod -R 777"

 gh copilot explain "Chmod -R 777 /"

 gh copilot explain "^foo^bar"

 gh copilot explain ":(){ :|: &}; :"

 gh copilot suggest "Command to find files that are grater than 1G in size"

``` 

