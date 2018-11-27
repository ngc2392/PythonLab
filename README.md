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

**Assignment:** Explore how the following basics work in Python:

- Variable declarations
- Algebraic expressions/assignment/computational statements 
- conditional statements
- loops
- simple text/numeric input and output.

This exploration should be accompanied by a number of simple programs, whose sole aim is to see if you're understanding what you're reading.  

Note that, frequently, you will not be able to turn straight to the information you're looking for; for example, it might be difficult to locate how to do simple console input.  Google is the answer, of course; "Python user input" is a good search to locate the info you're looking for.  Remember to be on the lookout for version 2 vs version 3 incompatibilities!

**Assignment:** Once you're done, complete this assignment by writing a program that reads in two integers, and prints all of the positive factors they have in common. 

## Assignment 3: Text Processing

Fundamental to most programming languages are facilities for the manipulation of text.  String variables and the ability to perform operations on them are universal.

Consult your tutorial sources to discover and play with the tools Python supplies for text manipulation.  Write plenty of samples yourself (in addition to copying and playing with the sample code you find) to see what works, and how. 

**Assignment:** Write a python program that asks the user for five text strings.  The program should then report on whether any of those strings is a sub-string of another (all such combinations should be reported).  

**Assignment:** Extend the previous program to lift the restriction to five strings; first ask the user how many strings she will enter, then read in and analyze all of them.  Note that this will require you to sort out how to hold all of the strings in memory at once --- you'll need some array-like data structure to do the work.  See what you can find.

**Assignment:** Write a program that reads in a sentence and outputs the words in that sentence, all lowercase and ordered alphabetically.  So, if I type:

*A hero; yes, a great HERO indeed - don't you agree?*

Your program would output

*a a agree don't great hero hero indeed yes you*

The list of punctuation marks you should remove is . , ; : -"/

## Assignment 4: The Standard Library

Once your language is rich enough, you can begin to extend the language, not by adding new features, but by writing code and storing it in an organized library so that you or other programmers can use that code.  Every function you write supplies the programmer with something new they can do without working hard.  

Like Java or C++ (or most other useful languages), Python comes with a rich standard library of facilities that you can be sure are available all the time.

Use your resources to review the sorts of facilities that are available in the Python Standard Library.  What do you have to do to access and use one of these facilities?  Get some example code working.

**Assignment:** Use library facilities for random number generation to write a program that reads in a file and outputs a new file containing the same lines of text, but shuffled in a random order.  There are lots of ways to do this, some quite clever and short!  Read and explore.

**Assignment:** Write a program that accepts a directory name and an extension, and prints all files in that directory that have that extension.  For instance, on my machine I might supply /home/fry/s17/syllabi and pdf, and the program would print a list of all files ending in .pdf in that folder.  Bonus points for allowing the user to choose the directory by presenting a standard file chooser, instead of typing the name.

## Assignment 5: Files


Files are the most common form of data storage, and text files are the simplest form to consider.  Refer to your tutorial and reference resources and spend some time with the tools Python supplies for reading from and writing to text files.  

**Assignment:** Write a program that counts the number of lines of text in a file and prints the answer on the console.

**Assignment:** Write a new version of the program from Assignment 3.  Now you should read the input from a file instead of from the user, and you should write your results to a new file.  Your program should begin by asking the user for the names of the input and output files.  Handle punctuation in the same way as before.  Process all of the text in the file.

**Assignment:** Modify the previous program so that eliminates duplicated words in the output.

**Assignment:** Our web server generates many of log files.  One of them, the access log, has a line of text written to it every time a client visits a web page.  The lines look like this:

```
/blog/bubba/120716/chicken.html   9-14-2016   17:46   205.23.104.49
```

The first entry is the page that was accessed (in this case, the file chicken.html, which is found in the folder /blog/bubba/120716). The second entry is the date (American style, month-day-year), the third is the time (24-hour clock), and the fourth is the IP address of the computer that requested the page.

Our log file will typically have hundreds of thousands of such lines for a week, if we have an active server.  Note that you shouldn't expect these lines to come in any particular order (not even chronological!).

Write a Python script that reads such a log file, and prints to a separate file a list of the top 10 pages on our web site in terms of number of visits.  You should output your results to a separate file.  Include in the output the name of each page, followed by the number of visits that page received.  Again, you should print only the top 10, in decreasing order.

**Assignment:** Companies are often more interested in unique hits, that is, they want to know the number of distinct visitors that viewed a page.  Modify your previous script so that it only counts new views if the IP numbers are distinct.  For example, if this is the log file:

```
/blog/bubba/120716/chicken.html   9-14-2016   17:46   205.23.104.49
/blog/bubba/120716/chicken.html   9-15-2016   12:43   205.23.104.49
/blog/bubba/120716/chicken.html   9-17-2016   21:09   194.33.212.111
/blog/bubba/120716/chicken.html   9-10-2016   8:11   12.65.4.100
/blog/bubba/120716/chicken.html   9-19-2016   14:13   205.23.104.49
```

Then the page received 5 views, but only 3 unique views.  


## Assignment 6: modules; functions and multifile programs

Key to designing programs beyond trivial size is to exploit the organizational tools provided by the language in order to divide up our work into manageable, reasonably independent chunks.  In the most languages, the primary such tool is the function (or procedure, or subroutine, or method... lots of names for the same thing).

In your tutorial resources, explore functions, how they are defined, how parameters and return values work, what scoping rules exist, etc.. Write a few examples and get them to work.

Building coherent, named collections of functions is the next step up the organizational ladder.  Study the idea of a python module, how they work, what they're for.  What can be inside a module? How do you define one?  How are the members of a module related?

**Assignment:** create a set of functions for "analyzing" data.  That is, functions that take lists of numbers and return various statistics about them:  we want functions that

- return the minimum entry,
- the maximum entry,
- the k'th largest entry (that is, if I pass a list and the number 4, I'll get the number that would come 5th if we listed them in ascending order (Note that, as usual, we begin counting from 0).
- the median
- the average
- the standard deviation.
Name all of these functions well, place them in a module, and write an example program (not part of that module) that shows how they might be used.

(remember, the point of this assignment is to get familiar with creating and calling and organizing functions; there may be simple ways to do some of these tasks without writing a function; write the function anyway)

Note that, if future assignments, part of the expectation will be that you decompose your solution into functions where appropriate.

PERSONAL NOTE: 'Data Functions' folder is used with 'Assignment 6'


## Assignment 7: Data Structures

Python has several data structures beyond the basic list that are "built in" to the language.  These include dictionaries (aka maps), sets and tuples.

Review your tutorial sources and other materials and play with examples of all of these.  

**Assignment:** Use a map to solve the following problem: write a function that accepts the name of a log file (formatted as in the the problem from Assignment 5).  This program should write a new file that shows the IP of each unique visitor (see the original problem for a discussion) and the number of distinct pages visited by that visitor.

Use a dictionary indexed by the visitor IP to solve this problem.

**Assignment:** You can use a python list as a stack -- a data container that can have items placed into it and taken out.  When you take an item out of a stack, you get the most recently added item (this is called a LIFO, or last-in, first-out, policy). 

Write a program that reads a file that specifies how items are being processed.  The file contains one word per line; for most lines, the word is the name of something that gets added to our stack.  In the special case of the word POP (all caps), we instead remove an item from the stack.

Your program should simply process the file, and then print out the contents of the stack, in order from least- to most-recently added, after all the commands in the file have been processed.

## Assignment 8: Libraries and API's -- The Final Project

For a long time, application development has relied on the use of libraries -- collections of pre-built functions, classes, modules, etc., that allow us to compose ever more complex applications.  By writing a library, one developer simplifies the work of others.

This idea has evolved in recent years to include the idea of services -- software running on internet servers (the buzzword cloud gets used a lot here) that we can interact with through a library called an API.  The API allows us to interact with the server so that we can use its facilities as if they were part of our application.

To use such a service, we typically have a few extra steps compared to what we've done thus far:

- Many such services require us to register with the service and obtain the right to use it.  For some commercial services, this might cost us some money.  In other cases, it might be about security (the service wants to ensure that only allowed clients use the service.
- You have to download and install the API library, as these do not (typically) come included with your language's standard library.
- You have to study the API documentation and figure out how to use it.

For this project, we will use the Google Maps Python API.  You can start your research at this page describing the python Google Maps API (Links to an external site.)Links to an external site..

**Assignment:** figure out how to acquire an API key, so that you can write python programs that use the maps API. 

**Assignment:** once you have the API key, find some sample code, download it, adjust it to use your key, and verify that you have things set up correctly.  I will install the python API on the lab machines; if you want to do this on your own machine, you'll have to use pip to install it yourself.

Note that your key has limits, particularly limits on daily usage.  Make sure you know where to check on your usage, so you know when you are approaching your daily limits or other limits.

**Assignment:** Play with the various facilities that the API provides.  Get used to the way the API provides data to you, and what questions it can answer.

**Assignment:** Write a program that allows the user to type in two "places" keywords (such as "theater" and "restaurant").  You should then find the three pairs of such places that are closest to each other, and within 50 miles of your current location.  So, if I enter theater and restaurant as above, you will print the three (theater, restaurant) pairs that are within 50 miles of me, and are closest to each other among all possible such pairings.  




