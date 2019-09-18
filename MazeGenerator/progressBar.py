import os
import math

class ProgressBar():
    
    def __init__(self, displayDetail, updateFreq):
        self.updateFreq = updateFreq
        # Enable progress bar if not already displaying details
        if displayDetail:
            self.enabled = False
        else:
            self.enabled = True
    
    # Display a progress bar to command line using the value input
    def displayBar(self, value):
        # If value given decimal, convert to percentage
        if value < 1.0:
            value = value * 100
            
        barValue = 5 # Each bar represents 5%
        # Calculate number of bars needed
        barNumber = int(value // barValue) 
        
        # Get the number of display bars (-) vs spaces (out of 10 needed) 
        # before the percentage value is displayed in the middle of the bar
        if barNumber >= 10:
            beforeBars = 10
        else:
            beforeBars = barNumber
        beforeSpaces = 10 - beforeBars
        
        # Get the number of display bars (-) vs spaces (out of 10 needed)
        # after the percentage value is displayed in the middle of the bar
        if barNumber <= 11:
            afterBars = 0
        else:
            afterBars = barNumber - 10
        afterSpaces = 10 - afterBars
        
        # Display percentage bar
        print('[ ' + (beforeBars * '-') + (beforeSpaces * ' ') +
              ' ' + str(round(value, 1)) + '% ' +
              (afterBars * '-') + (afterSpaces * ' ') + ' ]')
    
    # Prepare to display the progress bar for the process of creating a graph
    def displayCreateGraphProgress(self, progress):
        if self.enabled:
            os.system('cls') # Clear console

            print('Creating graph...')
            self.displayBar(progress)
        
    # Prepare to display the progress bar for the process of assigning graph
    # weights.
    # Assumes the progress of creating graph is already complete.
    def displayAddWeightsProgress(self, progress):
        if self.enabled:
            os.system('cls') # Clear console
            # Display full progress of graph creation
            print('Created graph.')
            self.displayBar(100)
            
            print('Adding weights...')
            self.displayBar(progress)
        
    # Prepare to display the progress bar for the maze generaion algorithm.
    # Assumes graph creation and weight assignment is already complete.
    def displayAlgorithmProgress(self, progress):
        if self.enabled:
            os.system('cls') # Clear console
            # Display full progress of graph creation and weight assignmenet
            print('Created graph.')
            self.displayBar(100)
            print('Added weights.')
            self.displayBar(100)
            
            if progress == 100:
                print('Algorithm finished.')
            else:
                print('Algorithm working...')
            self.displayBar(progress)