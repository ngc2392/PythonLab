# PythonLab


## Assignment 1

To get started with the semester, we should start by installing a development environment, that is, a program we can use to write Python programs.  For instance, we used Eclipse in CDS 142 to write Java programs.

I suggest the IDE PyCharm for python development.  There is a free "community" edition, and a professional edition.  You can actually get access to the professional edition for free with an academic license, but it is not necessary for our work.

You can download, read about, and install PyCharm from The JetBrains Website (Links to an external site.)Links to an external site.. 

Your first assignment: Get PyCharm installed on your computer (you can use it in Linux on the lab/classroom machines as well, but get it on your machine).  
Get on the Web and find a simple example python script, and figure out how to create a project in PyCharm, copy the sample script into it, and get that script to run.
Bring up a command line shell, and use the internet (or your instructor) to help you figure out how to navigate to the folder containing your script and execute it using the python interpreter.
Note: several years ago, the python language evolved from version 2 to version 3, and there were several major incompatible changes to the language.  To this day, there is still a lot of python code out there that does not work under version 3.  We will study version 3 of the language this semester, but you must be aware of this distinction, and be careful when you study example code from tutorials to understand what version of python the code is written for.

## Assignment 2 

It's time to start learning some python!

I suggest two sources of study to begin:

First, to learn about using PyCharm, there are some tutorial videos (Links to an external site.)Links to an external site. that you can watch to help find your way around the IDE.  Now, some of what you see here might be over your head, but don't worry about that.  Poke around.  One thing to be sure you've sorted out --- how to make sure PyCharm is using python 3.
At the main web site for the python community (Links to an external site.)Links to an external site., you can find tons and tons of resources.  First off, there is much documentation and a long tutorial (Links to an external site.)Links to an external site., aimed at experienced programmers, and a beginner's guide (Links to an external site.)Links to an external site. as well.
As you get further along, you will begin to make use of the extensive reference material, especially the library references.
Review the tutorials, get a sense of their structure.  It takes work to figure out how to read material like this; that work has to start now.

Assignment: Explore how the following basics work in Python:

Variable declarations
Algebraic expressions/assignment/computational statements
conditional statements
loops
simple text/numeric input and output.
This exploration should be accompanied by a number of simple programs, whose sole aim is to see if you're understanding what you're reading.  

Note that, frequently, you will not be able to turn straight to the information you're looking for; for example, it might be difficult to locate how to do simple console input.  Google is the answer, of course; "Python user input" is a good search to locate the info you're looking for.  Remember to be on the lookout for version 2 vs version 3 incompatibilities!

Assignment: Once you're done, complete this assignment by writing a program that reads in two integers, and prints all of the positive factors they have in common. 

## Assignment 3

Fundamental to most programming languages are facilities for the manipulation of text.  String variables and the ability to perform operations on them are universal.

Consult your tutorial sources to discover and play with the tools Python supplies for text manipulation.  Write plenty of samples yourself (in addition to copying and playing with the sample code you find) to see what works, and how. 

Assignment: Write a python program that asks the user for five text strings.  The program should then report on whether any of those strings is a sub-string of another (all such combinations should be reported).  

Assignment: Extend the previous program to lift the restriction to five strings; first ask the user how many strings she will enter, then read in and analyze all of them.  Note that this will require you to sort out how to hold all of the strings in memory at once --- you'll need some array-like data structure to do the work.  See what you can find.

Assignment: Write a program that reads in a sentence and outputs the words in that sentence, all lowercase and ordered alphabetically.  So, if I type:

A hero; yes, a great HERO indeed - don't you agree?

Your program would output

a a agree don't great hero hero indeed yes you

The list of punctuation marks you should remove is . , ; : -"/

'Data Functions' folder is used with 'Assignment 6'

