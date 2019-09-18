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
            
        barNumber = int(value // 5)
        
        if barNumber >= 10:
            beforeBars = 10
        else:
            beforeBars = barNumber
        beforeSpaces = 10 - beforeBars
        
        if barNumber <= 11:
            afterBars = 0
        else:
            afterBars = barNumber - 10
        afterSpaces = 10 - afterBars
        
        print('[ ' + (beforeBars * '-') + (beforeSpaces * ' ') +
              ' ' + str(round(value, 1)) + '% ' +
              (afterBars * '-') + (afterSpaces * ' ') + ' ]')
    
    def displayCreateGraphProgress(self, progress):
        if self.enabled:
            os.system('cls') # Clear console

            print('Creating graph...')
            self.displayBar(progress)
        
    def displayAddWeightsProgress(self, progress):
        if self.enabled:
            os.system('cls') # Clear console
            print('Created graph.')
            self.displayBar(100)
            
            print('Adding weights...')
            self.displayBar(progress)
        
    def displayAlgorithmProgress(self, progress):
        if self.enabled:
            os.system('cls') # Clear console
            print('Created graph.')
            self.displayBar(100)
            print('Added weights.')
            self.displayBar(100)
            
            if progress == 100:
                print('Algorithm finished.')
            else:
                print('Algorithm working...')
            self.displayBar(progress)