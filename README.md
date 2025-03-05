# Welcome to Time-ato!! 🍅 ⏰

CM3 Future Proofing Challenge - Computer Science Final project for Fahnam Naqvi & Siddhi Pareek (BOS 2 Team 3)

Let's start this READ ME with a little fact, Pomodoro in Italian means Tomato. Now, you must be questioning why am I telling you this? To that the answer is you will see...

Both of us very often stuggled with our attention span, getting distracted after every 5 minutes, or procastinating till last minute. Even if we, with Gods grace, save ourselves from that, we always end up just doing things without actually learning. In a subject like computer science which is so confusing to us, this cannot pass. When we saw a pomodoro timer as a suggestion for our project, we remembered that pomodoro is a certified techinque which actually helps people. As we are a big belivers that you should help youself in order to reach a position where you can help others, we made somthing that we will use, even if others don't see the appeal.

To give a explanation of the bigger picture, so I can answer your earlier question, our timer looks like a tomato beacuse going of of what pomodoro means in Italian (how could we pass off the perfect op-pun-tunity for its name?). It took a lot of back-and-forth debate because one of us adores tomato in each and every form, and the other will never order something if the tomatoes are not removeable.

Since the idea for our project was inspired by the suggestions given by Professor Lombardo, we wanted to challenge ourselves by making the name of our timer literal to its looks. At first we wanted the tomato to be an analog clock with the seeds as the multiples of five, but due to lack of time and experience with coding we choose a less complicated option and went with the digital clock. We wanted it to look cute as we are just girls <3 To make us use something it has to be cute and pretty, duh. Bright colors and a cute interface are enough to keep me from changing the tab to be honest.

Are we proud of it? For sure we are, this timer took blood and sweat, so it's our baby. Of course, just like humans it also has flaws which we will dive into later.

We used Gemini and Deep Seek to get the code (But, we made sure that we know how each line of code - which will be backed up by the viva voce).

Our code consist of 7 functions: 2 in python and 5 in Java Script. Now hold your horses- the reason we used another language is because we were unable to install and create a virtual environment using xvfb (which was the library which could handle any solution we could have made Python). so we left it there choosing something over nothing, prioritizing a functional result.

**Explaining the functionality:**

Project.py:

The main function for the Project.py is flask which make sure we are able to create a web page (which is what are project is), and to direct it to html the second function in the file, and that to be sure that the code run smootly by the first function being a debug. Additionally, as we mentioned before that because we did not know how to install a virtual environment we were not able to do main coding in python instead we choose java leading to us only having 2 funcions in Project.py file.

Requirements.txt:

This file just contains Flask and pytest, which can be installed together if the user runs the pip install -r requirements.txt command. Flask is essential to make sure our project works as an app, and opens in another browser webpage using a port. Pytest works as a python debuger, and is crucial for our test_project.py file.

Test_project.py:

This file makes the testing of the code smooth. When this runs, it automatically detects and executes all functions prefixed with test_. 
Like we learned in class, for each test function, certain assert commands are pushed as an argument, providing access to the client.

Script.js:

This is what our main code is, though this is in Java script we can still read it - just saying. Talking about the functions of this script the first function is about the start time, and the 2nd main function is about the stop time interval. The third main function is about the 25 min interval of the pomodoro timer. Then last but not the least, the 4th function is about the break times.

Style.css:

This file is all about the design of the timer. This was very crucial for us as we didn't just want to make anything, we wanted to make a cute timer. So this is the file/ code that mades the font Arial in size two, ensures everything on the webpage is centered, creating all of the buttons with the height of 100vh, ... I will not bore you with all the details of the timer, as you can see it when you try it - we belive on the visual appeal. Just to give a essense of it all this is the file that made us achive our secondary goal of aesthetics.
