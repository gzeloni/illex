# ILLEX Documentation

## Overview

This expression parser processes text templates with variable substitutions, assignments, and function handlers. It uses a state machine approach to interpret and evaluate expressions, making it suitable for template processing, configuration files, and domain-specific languages.

## Basic Syntax

### Variable References
Use the `@` symbol to reference variables:
```
@variable_name
```

Example:
```
Hello, @name!
```

### Variable Assignment
Assign values to variables using the `@variable = value` syntax:
```
@username = John Doe
Hello, @username!
```

### Parameter Substitution
Use curly braces to substitute parameters passed to the parser:
```
Hello, {username}!
```

### Comments
Use `\\` or `#` at the beginning of a line to create comments:
```
\\ This is a comment
# This is also a comment
@variable = 42  // This is not a comment (only line-beginning comments are supported)
```

## Advanced Features

### Variable Escaping
Use the backslash character `\` to escape variables and prevent further processing:
```
@variable\text
```

Example:
```
@number\px   // Will output the value of @number followed by "px"
```

### Array/Object Indexing
Access array elements or object properties using square brackets:
```
@array[0]
@dict["key"]
@dict[variable_key]
```

### Handler Functions
Execute registered handlers using the colon syntax:
```
:handler_name(arguments)
```

Built-in handlers include:
- `:split(text, delimiter)` - Split text into an array
- `:abs(value)` - Get absolute value
- `:date(format)` - Format dates

Example:
```
@ip_parts = :split(192.168.0.1, .)
First part: @ip_parts[0]
```

### Nested Processing
Variables can be used within other expressions:
```
@doubled = :multiply(@number, 2)
```

## Variable Assignment and Processing

The parser processes text in multiple phases:
1. Parameter substitution phase
2. Variable assignment phase with real-time substitution
3. Variable replacement phase
4. Handler processing phase

### Type Handling

The parser attempts to preserve appropriate types:
- String literals are preserved as strings
- Numbers are converted to numerical values
- Python literals (lists, dictionaries, etc.) are evaluated correctly
- Complex expressions use safe evaluation

## Error Handling

If an error occurs during processing, the parser will include an error message in the output:
```
[Error: variable_name[invalid_index] -> error message]
```

## Advanced Usage Examples

### Basic Template

```
@name = John
@age = 30
Hi @name, you are @age years old!
```

### Array Processing

```
@items = ["apple", "banana", "cherry"]
First item: @items[0]
Last item: @items[2]
Number of items: :len(@items)
```

### Object/Dictionary Handling

```
@user = {"name": "John", "email": "john@example.com"}
Username: @user[name]
Email: @user[email]
```

### Function Handlers

```
@dates = :split("2023-01-01,2023-02-01", ,)
Formatted: :date(@dates[0], "YYYY-MM-DD")
```

### Nested Expressions

```
@numbers = [10, 20, 30, 40]
@sum = :sum(@numbers)
@average = :divide(@sum, :length(@numbers))
The average is @average
```

### Variable Escaping

```
@width = 100
CSS: width: @width\px;
```

### Combined Example

```
@items = ["apple", "banana", "cherry"]
@count = :length(@items)
@message = :concat("Found ", @count, " items")
@first_item = @items[0]

Report:
- Message: @message
- First item: @first_item
- First letter of first item: @first_item[0]
- In uppercase: :upper(@first_item)
```

## Implementation Notes

- The parser uses a state machine approach to process text
- It handles nested expressions and bracket matching
- It preserves types when possible, converting strings to appropriate Python objects
- It processes variable substitutions in a context-aware manner, respecting comments and string literals
- It supports recursive variable replacement and function handler evaluation