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
    
    def displayBar(self, value):
        if value < 1.0:
            value = value * 100
            
        barNumber = int(value // 10)
        
        if barNumber >= 5:
            beforeBars = 5
        else:
            beforeBars = barNumber
        beforeSpaces = 5 - beforeBars
        
        if barNumber <= 6:
            afterBars = 0
        else:
            afterBars = barNumber - 5
        afterSpaces = 5 - afterBars
        
        print('[ ' + (beforeBars * '-') + (beforeSpaces * ' ') +
              ' ' + str(round(value, 2)) + '% ' +
              (afterBars * '-') + (afterSpaces * ' ') + ' ]')
    
    def displayCreateTreeProgress(self, progress):
        if self.enabled:
            os.system('cls') # Clear console

            print('Creating tree...')
            self.displayBar(progress)
        
    def displayAddWeightsProgress(self, progress):
        if self.enabled:
            os.system('cls') # Clear console
            print('Created tree.')
            self.displayBar(100)
            
            print('Adding weights...')
            self.displayBar(progress)
        
    def displayAlgorithmProgress(self, progress):
        if self.enabled:
            os.system('cls') # Clear console
            print('Created tree.')
            self.displayBar(100)
            print('Added weights.')
            self.displayBar(100)
            
            if progress == 100:
                print('Algorithm finished.')
            else:
                print('Algorithm working...')
            self.displayBar(progress)