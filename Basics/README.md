# python
All my scripts are going to be here
=======
# Python Basics Learning Project

A comprehensive collection of Python example scripts designed to help beginners learn fundamental Python programming concepts. This project covers essential topics including basic syntax, data structures, control flow, functions, error handling, and file operations.

## 🎯 Project Purpose

This project serves as a hands-on learning resource for Python beginners, providing practical examples of:
- Basic Python syntax and output
- Data types and structures (lists, arrays, dictionaries, sets, tuples)
- Control flow (loops, conditional statements)
- Function definition and usage
- Error handling with try-except blocks
- File I/O operations (JSON)
- String formatting techniques
- Mathematical operations
- Module usage

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd python-showoff-updated/01_basics
   ```
3. Ensure Python is installed and accessible from your command line:
   ```bash
   python --version
   # or
   python3 --version
   ```

## 📁 Project Structure

The project contains the following Python scripts, each demonstrating different Python concepts:

### Core Basics
- **`hello_world.py`** - Basic "Hello, World!" program demonstrating print statements
- **`math_helper.py`** - Simple mathematical operations and calculations
- **`operators.py`** - Examples of Python arithmetic, comparison, and logical operators

### Data Structures
- **`arrays.py`** - Working with arrays using the `array` module
- **`lists.py`** - List operations including creation, manipulation, and methods
- **`dict.py`** - Dictionary creation, access, and manipulation
- **`sets.py`** - Set operations and unique element handling
- **`tuples.py`** - Immutable tuple creation and usage

### Control Flow
- **`for_loop.py`** - For loop examples with different iterables
- **`while_loops.py`** - While loop demonstrations
- **`loops.py`** - Combined examples of both for and while loops

### Functions and Modules
- **`functions.py`** - Function definition, parameters, and calling
- **`modules.py`** - Importing and using Python modules

### Advanced Features
- **`string-format.py`** - Various string formatting methods (%, .format(), f-strings)
- **`json.py`** - JSON file reading and writing operations
- **`try-except.py`** - Error handling with try-except blocks
- **`user-input.py`** - Getting user input and processing it

## 🏃‍♂️ How to Run

### Running Individual Scripts

Each Python script can be run independently. Here are some examples:

```bash
# Basic hello world
python hello_world.py

# Run function examples
python functions.py

# Execute loop demonstrations
python loops.py

# Try error handling examples
python try-except.py
```

### Running All Scripts

To run all scripts in sequence (optional):

```bash
# On Unix-like systems (macOS, Linux)
for file in *.py; do
    echo "Running $file..."
    python "$file"
    echo "---"
done

# On Windows
for %f in (*.py) do (
    echo Running %f...
    python %f
    echo ---
)
```

## 📚 Learning Path

For beginners, we recommend following this learning order:

1. **Start with basics**: `hello_world.py` → `math_helper.py` → `operators.py`
2. **Learn data structures**: `lists.py` → `arrays.py` → `dict.py` → `sets.py` → `tuples.py`
3. **Understand control flow**: `for_loop.py` → `while_loops.py` → `loops.py`
4. **Explore functions**: `functions.py` → `modules.py`
5. **Advanced concepts**: `string-format.py` → `json.py` → `try-except.py` → `user-input.py`

## 🔧 Customization

Feel free to modify any script to experiment with different values, add new examples, or create your own variations. This is a learning project, so experimentation is encouraged!

## 📖 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python Tutorials](https://realpython.com/)

## 🤝 Contributing

This is a learning project, but if you have suggestions for improvements or additional examples, feel free to contribute!

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Learning! 🐍✨**
