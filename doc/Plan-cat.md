# Software Development Plan

Phase 0: Requirements Analysis
------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [ ] Re-write the instructions in your own words.
    *   The cat tool is produce one line or more on STDOUT. use > to add more than one file. 
*   [ ] Explain the problem this program aims to solve.
    *   print the files onto the shell 
    *   Describe what a *good* solution looks like.
      * When it matches the examples
    *   List what you already know how to do.
      *  I already know how to open a file.
      * for file in args:
        f = open(file)
    *   Point out any challenges that you can foresee.
      * I need to know how to get the command line in tt.py and make cat work.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
  * program has 2 inputs.
    * the file names
    * and the data in the files names. use open() to access.
*   [ ] Explain what form the program's output will take.
  * When good arguments are given to the program, the output is the concatenation of the contents of the named files 
  * If the file list is 0, display an error message. 
  * If a filename is spelled wrong, just let the program crash. 
  * If a file is inaccessible, just let the program crash.


Phase 1: Design
---------------
*(30% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.

Deliver:

*   [ ] Pseudocode that captures how each function works in plain language.
    *   Pseudocode != Python.  Do not paste your finished source code into this part of the plan.
    * ```python
          cat function:
          input: takes a list of filenames
          output: prints a lot of text to the screen
                  returns nothing
          =============
          get a list of filenames from the user, put it into the variable 'filenames'
          for file in filenames:
              open the file and put it in a variable 'f'
              read each line in f in a for loop:
                  print each line of text, but DON'T print an extra newline!!!
                  The line already has its own \n
              close the file
          ```
*   [ ] Explain what happens in the face of good and bad input.
    *   As you think of specific examples, write them under **Phase 3** so you can run them as soon as the program is functional.
      * in good inputs, it works, in bad inputs it gives an error


Phase 2: Implementation
-----------------------
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] Working code in the `src/` folder.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   went well


Phase 3: Testing and Debugging
------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   I ran all of the cases that you had examples on.
    * I made sure the error code only did what it was supposed to.
