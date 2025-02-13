# Software Development Plan

Phase 0: Requirements Analysis
------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [X] Re-write the instructions in your own words.
    *  use grep and whatever is after it should print each word that has it in the line.
      * it will print every line that has the pattern
    * -v will prints lines that don't have a match
*   [X] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
      * if i put grep blue [file] it will print every line that has blue in it
    *   List what you already know how to do.
      * i can say if pattern in line, print line
    *   Point out any challenges that you can foresee.
      * i might have a challenge finding how to use -v in the arguments
*   [X] List all of the data that is used by the program, making note of where it comes from.
*   [X] Explain what form the program's output will take.
    * the output will need grep and or -v.
    * the output will need at least letter after grep or -v


Phase 1: Design
---------------
*(30% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.

Deliver:

*   [ ] Pseudocode that captures how each function works in plain language.
    *   Pseudocode != Python.  Do not paste your finished source code into this part of the plan.
    *   ```python
        see if -v is in the argument
        if it is, set the pattern to be the second in the argument
        and set all the files everything after the second
        
        if its not in just have pattern be the first in the argument
        have all the files be after the first
        
        open the file
        for every line in the file
        if the pattern is in the line
        print the line
        
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
    *   e.g. i learned how to manipulate files and how to only access some parts of files.
      * what went well was everything but the error messages
      *     i got confused on how to print the error usage if the file is wrong.
    


Phase 3: Testing and Debugging
------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   I did all of the tests that the teacher used in the example and it worked.
      * i had to go back and add a line that if it is using -v then it has to print the file name before the lin
    * im still a little confused on the error message.
