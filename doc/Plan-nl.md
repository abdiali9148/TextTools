# Software Development Plan

Phase 0: Requirements Analysis
------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [ ] Re-write the instructions in your own words.
    *   just like cat but add number lines before each line
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
      * having the number before each line
    *   List what you already know how to do.
      * i know how to use for loops, i could use that to keep upping the cound and printing(count + "" + line)
    *   Point out any challenges that you can foresee.
      * nothing as of right now
*   [ ] List all of the data that is used by the program, making note of where it comes from.
  * there is one that is a -ba that includes blank lines. this might be easier. i would need a "blank_lines" variable
*   [ ] Explain what form the program's output will take.
  * it will take the nl input, and or -ba. then the files.


Phase 1: Design
---------------
*(30% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.

Deliver:

*   [ ] Pseudocode that captures how each function works in plain language.
    *   Pseudocode != Python.  Do not paste your finished source code into this part of the plan.
    * ```python
      see if -ba is in the argument
      if it is, make include_blank_lines True
      
      open the file
      for line in f
      print line number and line
      line number plus 1
      
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
    *   e.g. it worked for me and this was the easiest so far!!


Phase 3: Testing and Debugging
------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   I had to go back and edit it because i forgot once you check for something in the argument and its there
      you have to then set the new argument to whatever is after that. 
      it didnt take me that long although.
