# Software Development Plan

Phase 0: Requirements Analysis
------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [ ] Re-write the instructions in your own words.
    *   just like cat but do everything in reverse
*   [ ] Explain the problem this program aims to solve.
        * print files onto shell in reversed order 
      *   Describe what a *good* solution looks like.
          * when the files are in reversed order.
      *   List what you already know how to do.
          * I already know how to do cat but im pretty sure i can just call a "reversed function" 
      *   Point out any challenges that you can foresee.
          * nothing really 
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
    *   Describe important functions and classes in your program.  Include such details as:
        *   ```python
            for every file in the argument
                open the file
                i found this in word count, if i use f.readlines() = lines.
                    it reads every line
                for every line in the lines reverse
                    print the line

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
    *   e.g. what you learned, what didn't go according to plan.
      *  every thing went well.


Phase 3: Testing and Debugging
------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    * nothing really was bothering me, this was the easiest by far.
