# IDGenerator

This is my second app for public service.

__Goal:__ To generate a case ID for the customer to track the progress of his or her case. The ID allows him or her to access the progress report of the case. 

__Input:__ The first name and the surname (String in Thai) of the user

__Output:__ The User ID text, which combines the first English chracter of name, surname, and a time-based serial number 

__Steps:__

1. Import the tkinter module for creating the graphic user interface (GUI) of this app. 
2. Import the datetime module for getting the present time
3. Set the time format as yyyymmddhhmm
4. Get the value yymmddhhmm as the user ID suffix
5. Create a new function called "Show Output", which gets integer number transformed from the text number input
6. Get the values from the two input boxes (first name and surname)
7. Create a new dictionary for translate the username and surname into English. Avoid using 'I', which seems like 1. Aoid using O whichs seems like 0. Some charcaters were translated in a new way: โ == Z; ใ == E; ไ == U; เ == A; แ == Q, to have diverse ID codes.
8. Use various English characters for Thai vowels
9. Create separate dictionary tables for username and surname translation
10. Translate the username and put the value in a new variable called transName
11. Translate the surname and put the value in a new variable called transSurname
12. Set the value for the output, which combines the first characters of the translated username and surname plus the Integer ID
13. Show the output as text
14. Create a new window for my application
15. Set the size of the app window as 400 x 400 px
16. Set the name of my app as jTech ID Generator.
17. Set the text on what this app does and show it in the window with space between lines at 20 px.
18. Create two text messages to describe the two input boxes
19. Set the locations of the text
20. Set the type of input data as String (plain text)
21. Create an input box for the first name of the user, and set its location
22. Create an input box for the surname, and set its location
23. Add a button, named 'Get ID', and add this command: 'show_output'
24. Set the button size as
25. Pack the button to the screen
26. Show the output on the screen with 20 px space vertically
27. Show the app window
