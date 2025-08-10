# Python Intermediate Features

A comprehensive collection of Python intermediate concepts and examples, focusing on advanced language features like decorators and list comprehensions. This project serves as a learning resource and reference for Python developers looking to enhance their understanding of intermediate-level Python programming techniques.

## 🎯 Project Purpose

This project demonstrates key intermediate Python concepts through practical, runnable examples. It's designed to help developers:
- Understand and implement Python decorators
- Master list comprehensions and functional programming patterns
- Learn best practices for intermediate Python development
- Have working examples to reference and experiment with

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Basic understanding of Python fundamentals (functions, classes, basic syntax)

### Installation

1. Clone or download this repository:
```bash
git clone <repository-url>
cd 02-Intermediate
```

2. No external dependencies are required - this project uses only Python standard library features.

3. Verify your Python installation:
```bash
python --version
# or
python3 --version
```

## 📁 Project Structure

```
02-Intermediate/
├── README.md                 # This file - project documentation
├── decorators.py            # Decorator examples and implementations
└── list_comprehensions.py   # List comprehension examples
```

## 🐍 Running the Examples

### Decorators Example

Run the decorator demonstration:

```bash
python decorators.py
# or
python3 decorators.py
```

**Expected Output:**
```
Calling greet...
Hello, Pythonista!
greet finished.
```

### List Comprehensions Example

Run the list comprehension examples:

```bash
python list_comprehensions.py
# or
python3 list_comprehensions.py
```

## 📚 File Descriptions

### `decorators.py`
This file demonstrates the concept of Python decorators through a practical example:

- **`log_function_call(func)`**: A decorator function that logs when a decorated function is called and when it finishes execution
- **`greet(name)`**: A simple function decorated with `@log_function_call` that demonstrates the decorator's functionality
- **Usage Example**: Shows how to apply the decorator and what the output looks like

**Key Learning Points:**
- How decorators wrap functions with additional functionality
- The `@` syntax for applying decorators
- Creating wrapper functions that can accept any arguments

### `list_comprehensions.py`
This file contains examples of Python list comprehensions:

- **Purpose**: Demonstrates concise and readable ways to create lists based on existing sequences
- **Benefits**: More readable than traditional for loops for simple list transformations
- **Use Cases**: Filtering, mapping, and transforming data in a single line

**Key Learning Points:**
- Syntax: `[expression for item in iterable if condition]`
- When to use list comprehensions vs. traditional loops
- Performance considerations and best practices

## 🔧 Customization

Feel free to modify these examples to experiment with different concepts:

- Add more decorator examples (timing, caching, validation)
- Create more complex list comprehensions
- Add error handling and edge cases
- Implement additional intermediate Python features

## 📖 Learning Resources

To deepen your understanding of these concepts, consider exploring:

- [Python Decorators Documentation](https://docs.python.org/3/glossary.html#term-decorator)
- [List Comprehensions Tutorial](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Real Python - Decorators](https://realpython.com/primer-on-python-decorators/)
- [Python List Comprehensions Guide](https://realpython.com/list-comprehension-python/)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more intermediate Python examples
- Improve existing code with better practices
- Add more comprehensive documentation
- Include additional Python features (generators, context managers, etc.)

## 📄 License

This project is open source and available under the [GNU General Public License v3.0](LICENSE).

For more information about the GNU GPL v3.0, please see the [LICENSE](LICENSE) file or visit [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html).

## 🆘 Support

If you encounter any issues or have questions:
1. Check the Python documentation for the specific concept
2. Review the code comments for implementation details
3. Experiment with the examples to better understand the behavior

---

**Happy Python Learning! 🐍✨**