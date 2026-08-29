# Python Calculator

A simple calculator I created while learning Python, and also made a web version so that people can try the calculator in a browser without having to type in commands.

## Features

- +, -, , / operations

- Asks for more calculations until told otherwise

- No crashes due to dividing by zero

- Can be run as a script in your terminal by typing 'calculator.py', or can be seen in a browser by typing 'index.html'

## Assembly

The 'calculator.py' file itself is the calculator, which asks for two numbers and an operation until the user decides to stop. I made this myself by applying the concepts that I was learning with Python, such as getting input from the user with conditionals, and loops.

The 'index.html' file is the web version of the calculator, which uses much of the same logic as 'calculator.py', but I had to get help from an AI since I have no experience in HTML, CSS, or JavaScript yet. I'm very proud of how well it turned out, especially considering that I had to learn much of it by trial-and-error.

The files 'vercel.json' and 'requirements.txt' were added later on when I was trying to deploy the project, and will likely be deleted in the future. I don't completely understand how Vercel works with Python scripts and websites, which is why I'm sure that these files don't serve much of a purpose, besides testing.

## Operation

To run the terminal version of this calculator, type the following command into your terminal:

```bash

python calculator.py

```

Then follow the prompts until you are asked to stop.

To view the web version, open 'index.html' in your browser, or view the page in a browser if the site is deployed.

## Purpose

I created this script as my very first project after learning about loops, conditionals, and user input in Python. The web version was created afterwards mainly for fun, and to see how far I could go in a project that I had to manually type in, compared to a language I have no experience in.

## Compatibility

It is unclear how compatible this project is, since the only reason that 'calculator.py' works is because it is not connected to any database or other Python script, besides the 'api/.py' route, which is not used by 'index.html'.

The 'requirements.txt' file has 'Flask' listed, but 'calculator.py' is simply run as a script in the terminal. 'Index.html' has no connection to an API or database either, which means that the Flask dependency, and 'api/.py' route in 'vercel.json' are not being used. This means that I will likely have to create an API version, or remove some unecessary dependencies in the future.

---

Please let me know if you have any suggestions or concerns! I am always looking to improve, and any feedback is appreciated!