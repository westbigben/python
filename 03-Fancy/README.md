# Fun and Fancy Python Projects

A collection of entertaining and visually appealing Python scripts that demonstrate various programming concepts including graphics, fractals, chatbots, and utilities.

## 🎯 Project Overview

This repository contains a variety of Python scripts that showcase different aspects of programming:
- **Mathematical Visualizations**: Mandelbrot fractal generation
- **Graphics & Animation**: Turtle graphics spirograph
- **Interactive Applications**: Simple rule-based chatbot
- **Utility Tools**: QR code generation, duplicate IP detection from log files

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Dependencies
Install the required packages using pip:

```bash
pip install numpy matplotlib qrcode pillow
```

Or install them individually:
```bash
pip install numpy
pip install matplotlib
pip install qrcode[pil]
```

**Quick Install (Recommended):**
```bash
pip install -r requirements.txt
```

## 📦 Module Requirements

### **mandelbrot_fractal.py**
**Required Modules:**
- `numpy` - For numerical computations and array operations
- `matplotlib.pyplot` - For plotting and displaying the fractal
- `matplotlib` - For colormap support and visualization

**Installation:**
```bash
pip install numpy matplotlib
```

### **turtle_spirograph.py**
**Required Modules:**
- `turtle` - Built-in Python module for graphics (no installation needed)
- `colorsys` - Built-in Python module for color space conversions (no installation needed)

**Installation:**
```bash
# No external packages required - uses built-in Python modules
```

### **simple_chatbot.py**
**Required Modules:**
- No external modules required - uses only built-in Python functions

**Installation:**
```bash
# No external packages required
```

### **qr_code_generator.py**
**Required Modules:**
- `qrcode` - For generating QR codes
- `pillow` (PIL) - For image processing and saving (automatically installed with qrcode)

**Installation:**
```bash
pip install qrcode[pil]
# or simply:
pip install qrcode
```

### **duplicate_ip_detector.py**
**Required Modules:**
- `re` - Built-in module for regular expressions (no installation needed)
- `argparse` - Built-in module for command-line argument parsing (no installation needed)
- `sys` - Built-in system-specific parameters and functions (no installation needed)
- `collections` - Built-in module for specialized container datatypes (no installation needed)
- `pathlib` - Built-in module for object-oriented filesystem paths (no installation needed)
- `typing` - Built-in module for type hints (no installation needed)

**Installation:**
```bash
# No external packages required - uses only built-in Python modules
```

## 📁 Project Structure

```
03-Fancy/
├── README.md
├── requirements.txt              # Dependencies list
├── mandelbrot_fractal.py      # Mandelbrot set visualization
├── turtle_spirograph.py       # Colorful spirograph animation
├── simple_chatbot.py          # Interactive chatbot
├── qr_code_generator.py       # QR code generator
└── duplicate_ip_detector.py   # Log analysis tool for detecting duplicate IPs
```

## 🎮 How to Run

### Mandelbrot Fractal Generator
Generate and display a stunning Mandelbrot set visualization:
```bash
python mandelbrot_fractal.py
```
**Features:**
- Generates an 800x800 pixel fractal image
- Uses the "twilight_shifted" colormap for beautiful visualization
- Configurable plot boundaries and iteration count
- Interactive matplotlib display

### Turtle Spirograph
Create a colorful animated spirograph pattern:
```bash
python turtle_spirograph.py
```
**Features:**
- Draws 36 circles with rainbow colors
- Black background for contrast
- Smooth animation using turtle graphics
- HSV color spectrum generation

### Simple Chatbot
Interact with a basic rule-based chatbot:
```bash
python simple_chatbot.py
```
**Features:**
- Responds to basic greetings and farewells
- Simple input/output interface
- Type 'bye' to exit the conversation
- Extensible response dictionary

### QR Code Generator
Generate QR codes for URLs or text:
```bash
python qr_code_generator.py
```
**Features:**
- Creates QR codes with customizable parameters
- Saves output as PNG image
- Configurable version, box size, and border
- Default generates QR code for GitHub profile

### Duplicate IP Detector
Analyze log files to detect duplicate IP addresses:
```bash
python duplicate_ip_detector.py logfile.log
python duplicate_ip_detector.py --min-count 5 --format apache access.log
python duplicate_ip_detector.py --output duplicates.csv --show-lines server.log
python duplicate_ip_detector.py --create-sample  # Create test data
```
**Features:**
- Supports Apache, Nginx, and generic log formats
- Configurable minimum occurrence threshold
- Detailed statistics and reporting
- CSV export functionality
- Line number tracking for duplicate occurrences
- Built-in sample log generation for testing
- Command-line interface with comprehensive options

## 🛠️ Customization

### Mandelbrot Fractal
- Modify `width` and `height` for different image resolutions
- Adjust `xmin`, `xmax`, `ymin`, `ymax` for different zoom levels
- Change `iterations` for more/less detailed fractals
- Experiment with different `cmap` values for color schemes

### Turtle Spirograph
- Adjust the circle radius by changing the value in `t.circle(100)`
- Modify the rotation angle in `t.right(10)`
- Change the number of colors by modifying the range in the colors list
- Adjust the speed with `t.speed(0)` (0 = fastest)

### QR Code Generator
- Change the `data` variable to encode different URLs or text
- Modify `version`, `box_size`, and `border` parameters
- Customize colors with `fill_color` and `back_color`
- Change the output filename as needed

### Duplicate IP Detector
- Adjust `--min-count` to change the threshold for duplicate detection
- Use `--format` to specify log format (apache, nginx, or generic)
- Add `--show-lines` to display line numbers where IPs appear
- Use `--top N` to limit output to top N most frequent IPs
- Specify `--encoding` for different file encodings
- Customize output with `--output filename.csv` for CSV export
- Modify regex patterns in the code for custom log formats

## 🔧 Troubleshooting

### Common Issues

1. **Matplotlib display issues**: If the Mandelbrot fractal doesn't display, try:
   ```bash
   pip install --upgrade matplotlib
   ```

2. **Turtle graphics not working**: Ensure you have a graphical environment or try:
   ```bash
   export DISPLAY=:0
   ```

3. **QR code generation errors**: Make sure PIL/Pillow is installed:
   ```bash
   pip install pillow
   ```

### Dependencies Check
Verify all packages are installed correctly:
```bash
python -c "import numpy, matplotlib.pyplot, qrcode, turtle, colorsys, re, argparse, sys, collections, pathlib, typing; print('All dependencies installed successfully!')"
```

## 🎨 Output Examples

- **Mandelbrot Fractal**: Interactive matplotlib window with colorful fractal visualization
- **Spirograph**: Animated turtle graphics window with rainbow-colored circular patterns
- **Chatbot**: Command-line interface for interactive conversation
- **QR Code**: PNG image file saved as "my_qr_code.png"
- **Duplicate IP Detector**: Console output with detailed statistics and duplicate IP report, optional CSV export

## 🤝 Contributing

Feel free to contribute by:
- Adding new Python scripts
- Improving existing functionality
- Adding more customization options
- Creating additional visualization types

## 📝 License

This project is open source and available under the [GNU General Public License v3.0](LICENSE).

For more information about the GNU GPL v3.0, please see the [LICENSE](LICENSE) file or visit [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html).

## 🎯 Future Enhancements

Potential improvements and additions:
- Add more fractal types (Julia sets, Sierpinski triangles)
- Implement interactive controls for real-time parameter adjustment
- Add more sophisticated chatbot responses using NLP
- Create a GUI wrapper for easier script execution
- Add export options for different image formats
- Implement batch processing for multiple QR codes

---

**Happy coding! 🐍✨**