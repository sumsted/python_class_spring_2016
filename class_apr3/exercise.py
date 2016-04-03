'''CONTROLLING ROBOT WITH AN EVENT LOOP
We're going to create an event loop. An event loop is
a loop that always runs. It looks for events, like key presses,
and then depending on the event causes some action to take
place, like moving a robot.

Our event loop will accept commands from the keyboard and
then tell our robot to go in a particular direction.
'''

'''Notice that you can either import dragonbot or gopibot.
They use the same function names for control.
'''
#import dragonbot as robot
import gopibot as robot


'''Set robot_debug to False to send commands to the robot.
'''
robot.robot_debug = False


'''*** STEP 1 THE EVENT LOOP***
Create a while loop that always runs.
Remember that a while statement is like an if statement.
It expects to have a boolean expression following it.
A boolean is either True or False.
'''

    '''*** STEP 2 PRINT INSTRUCTIONS ***
    You can print commands out to the screen so that the user
    will know which keys do what. You need commands that move the robot
    left, right, forward and back. You can also add rotate left and rotate right.\
    the w-forward, s-backward, a-left, d-right pattern would be good. You could
    use z-rotateleft and c-rotateright. You may also want a command like 'q'
    that lets the user exit the loop.
    '''


    '''*** STEP 3 ACCEPT INPUT ***
    You need to accept a key from a user using the input() function.
    Remember to pass input a prompt. input() returns a string. You'll need
    to store this value in a variable. Like this
    command = input("direct: ")
    '''


    '''*** STEP 4 MAKE ROBOT MOVE ***
    This is the part of our program where we make the robot do something.
    You'll need an if statement that calls a different robot function for each
    command the user enters. If a command is not found we just won't do anything.
    Here's how part of it might look. Notice that 'q' executes the break statement.
    Break tells python to exit the current loop. This ends our program.
    if command == 'q':
        break
    elif command == 'w':
        robot.forward()
    elif command == 's':
        robot.backward()
    '''

'''*** STEP 5 WE'RE DONE ***
Now we are outside of our loop. The program is about to end. We can
print a message telling the user thanks.
'''
