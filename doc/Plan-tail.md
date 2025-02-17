# Software Development Plan

Phase 0: Requirements Analysis
------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [ ] Re-write the instructions in your own words.
    *  print only the last 10 lines of the file, if -n is called, it chooses what number is the last lines.
*   [ ] Explain the problem this program aims to solve.
    *    it is going to let me see the end of the file.
    *    I already know how to call a file, print the first 10.
    *    I found out that variable[-10:] will be the last 10.
    *    So if i use a for loop, it will reiterate through the last 10.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *    Takes the either -n or not, the number after -n, and the filename. 
*   [ ] Explain what form the program's output will take.
    *    same as above. 


Phase 1: Design
---------------
*(30% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.

Deliver:

*   [ ] Pseudocode that captures how each function works in plain language.
    *   Pseudocode != Python.  Do not paste your finished source code into this part of the plan.
    *   Describe important functions and classes in your program.  Include such details as:
        *   ```python
            check to see all the ways the file can fail.
            if it is less than 0
            if the first arg is 0, then there has to be a number after
                then make the count variable
                pop the -n and the number so arg is just the files.
            
            
            for every argument
                use the lines = read lines discovered in wordcount.py
                use [-count:] to use the last of the count backwards
                print lines
        ```
*   [ ] Explain what happens in the face of good and bad input.
    *   As you think of specific examples, write them under **Phase 3** so you can run them as soon as the program is functional.


Phase 2: Implementation
-----------------------
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] Working code in the `src/` folder.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. what you learned, what didn't go according to plan.


Phase 3: Testing and Debugging
------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *  i found that lines[-count:] was the best way to use the last of a count.