#---------------------------------------------------------------------#
# Title: ValidationClass.py
# Desc: Validates user inputs, files, data types, and other
# Change Log: (Who, When, What)
# AHolmes, 2022-Mar-25, Created File>
#---------------------------------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class ErrorProcessor:
    def valid_int():
        """
        Returns
        -------
        intID : TYPE = INTEGER
            DESCRIPTION = returns a valid integer
        """
        while True:
            try:
                intID = int(input('Enter ID / Position: ').strip())
                return intID
            except:
                print('Please only enter whole numbers.')
    
    def valid_str(strQuestion, answers = []):
        """
        Parameters
        ----------
        strQuestion : TYPE = string
            DESCRIPTION = displays the question that the user will respond to
        answers : TYPE, optional = list
            DESCRIPTION. The default is []. displays the possible answers

        Raises
        ------
        Exception
            DESCRIPTION = if user enters without typing anything

        Returns
        -------
        strAnswer : TYPE = string
            DESCRIPTION = the user's response to strQuestion
        """
        while True:
            try:
                if len(answers) > 0:
                    strAnswer = str(input(strQuestion).strip().lower())
                    if (strAnswer not in answers):
                        raise Exception('Please enter a valid choice: ' + print(answers))
                else:
                    strAnswer = str(input(strQuestion).strip())
                if not strAnswer:
                    raise Exception('Empty string. Please enter value.')
                return strAnswer
            except:
                print('Please enter a string.')
