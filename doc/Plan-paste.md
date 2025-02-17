# Software Development Plan

Phase 0: Requirements Analysis
------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [ ] Re-write the instructions in your own words.
    *   joins files together and seperates them with a comma.
      *  so they will be printed at the same time. just FileA, FileB
*   [ ] Explain the problem this program aims to solve.
    *   I already know how to print files, the hard part will be combining them by a comma.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   same as all the other ones 
*   [ ] Explain what form the program's output will take. 
    *   if after paste only one file is there, it will be just like cat, else there has 
       * there has to be more than one file so paste can be functional. 


Phase 1: Design
---------------
*(30% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.

Deliver:

*   [ ] Pseudocode that captures how each function works in plain language.
    *   Pseudocode != Python.  Do not paste your finished source code into this part of the plan.
    *   ```python
            for all the files in the argument.
                join the files together. "i found this to be easier instead of having the files in 
                   in the args still"
            
            for the range of the len(lines)
                for every line in the file.
                  add the line to the print variable.
            then print the jointed print variable.
                    

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
    *  I also found these last 2 functions to be easier if i just have a seperate variable for the files.
