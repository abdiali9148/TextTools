# Software Development Plan

Phase 0: Requirements Analysis
------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [ ] Re-write the instructions in your own words.
    *   wc prints the number of lines, words, and bytes in a files
*   [ ] Explain the problem this program aims to solve.
    *   each line says the num of lines, num of words, num of bytes, and the filename
*   [ ] List all of the data that is used by the program, making note of where it comes from.
*   [ ] Explain what form the program's output will take.
    * it will take only wc and the file names.   


Phase 1: Design
---------------
*(30% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.

Deliver:

*   [ ] Pseudocode that captures how each function works in plain language.
    *   Pseudocode != Python.  Do not paste your finished source code into this part of the plan.
    *   ```python
        open the file
        read the line
        line_count is gonna be the length of the lines
        word_count is gonna be the sum of every word. use line split for every line in lines
        byte_count is 
        
        print(line_count, word_count, byte_count, and filename)
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
    *   e.g. the easy part was the line count. the hard part was the word count. although i had a talk with the teacher
    * and he helped me easily come to a conclusion for those two


Phase 3: Testing and Debugging
------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
    *   Include a description of what happened for *each test case*.
    *   For any bugs discovered, describe their cause and remedy.
