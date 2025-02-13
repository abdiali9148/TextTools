# Software Development Plan

Phase 0: Requirements Analysis
------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [ ] Re-write the instructions in your own words.
    *   print a maximum of 10 lines. just like cat if it is less than 10
*   [ ] Explain the problem this program aims to solve.
    *   after 10 lines it automatically stops and doesnt cause an erro
    *   List what you already know how to do.
      * I already know how to do cat, so i will do a for loop of 10 times and it stops after that.
    *   Point out any challenges that you can foresee.
      * i dont think i know how to do a for loop for files.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
*   [ ] Explain what form the program's output will take.


Phase 1: Design
---------------
*(30% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.

Deliver:

*   [ ] Pseudocode that captures how each function works in plain language.
    *   Pseudocode != Python.  Do not paste your finished source code into this part of the plan.
    *   Describe important functions and classes in your program.  Include such details as:
    - ```python
      input: list of filenames
      output: prints a maximum of 10 lines
      
      =============
      if the arguments contain -n:
        make whatever is after that the count
      if not:
        make count 10
      
      open the file
        for over line in it print the line
        have a count so it stops at the count
      ```
      
*   [ ] Explain what happens in the face of good and bad input.
    *   As you think of specific examples, write them under **Phase 3** so you can run them as soon as the program is functional.
      * in the good part of the input, it stops at whatever the count is. in the bad part i dont know how to raise exceptions with the options.


Phase 2: Implementation
-----------------------
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] Working code in the `src/` folder.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   i dont want to put any error messages in the tool function but that seems to be the only way i can. 


Phase 3: Testing and Debugging
------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   I tested all the example code you gave me.
    * the only problem i ran into was the error messages. im not sure if i put it in the tool function.
