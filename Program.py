import os
import inspect
import sys

def main():
    sandbox()

    def game_over():
        print("I sense a disturbance in the code")
        os._exit(1)
        print('The code is strong in this one')

    def win():
        # TODO fail_if_not_called_from_line_8()
        print(FROGSLAYER_LOGO)
    game_over()
    win()


# Howdy!
#
# Thank you for your interest in FrogSlayer and taking the time to apply.
#
# This file is a coding exercise. Please follow the instructions explicitly -
# you may only write code where specified. We've included reference material
# with information to produce a working solution. This is not a trick problem;
# it is solvable within the given constraints.
#
# It's okay if you can't get a fully working solution; just submit what you
# have. We're more interested in seeing how well you can learn and use
# something new with limited direction.
#
# Instructions:
# Using python 3 and only writing code where indicated (inside the sandbox function), 
# make this program execute the last line of game_over and all of the win function.
# It should output: 
#  'This code is strong in this one'
#  Followed by the FrogSlayer logo
#
# Some useful references:
#
# https://docs.python.org/3.6/library/inspect.html#the-interpreter-stack
# https://docs.python.org/3/library/sys.html#sys.settrace
# https://github.com/python/cpython/blob/3.6/Lib/pdb.py
#
# We have had concerns that this kind of hackery would be required on the job
# at FrogSlayer. I want to reassure you that code quality is important to us
# and that this is only for sake of producing a problem that gets outside of 99%
# of developers' experiences.
#

def sandbox():
    #####################################################
    # Begin sandbox
    # you can only code in this sandbox

    trace_function_name = ['game_over']

    def trace_lines(frame, event, arg):
        if event != 'line':
            return
        frame_code = frame.f_code
        line_no = frame.f_lineno
        frame.f_lineno = frame.f_lineno + 2  ##skips to last line

    def trace_calls(frame, event, arg):
        if event != 'call':
            return
        frame_code = frame.f_code
        function_name = frame_code.co_name
        # print(function_name)
        if function_name in trace_function_name:
            return trace_lines
        return

    sys.settrace(trace_calls)
    #####################################################
    pass

    #####################################################
    # End sandbox
    #####################################################


FROGSLAYER_LOGO = """
                                                    `.-            -.`                                         
                                            `.:+sydmmNd`          `dNmmdys+:.                                  
                                        ./ohmmNNNNNNNNd`          `dNNNNNNNNmmho/.                             
                                    ./sdmNNNNNNNNNNNNNd`          `dNNNNNNNNNNNNNmds/.                         
                                 .+hmmNNNNNNNNNNNNNNNNd`          `dNNNNNNNNNNNNNNNNmmh+.                      
                              `/ymNNNNNNNNNNNNNNNNNNNNd`          `dNNNNNNNNNNNNNNNNNNNNmy/`                   
                            .odmNNNNNNNNNNNNNNNNNNmdhyo            oyhdmNNNNNNNNNNNNNNNNNNmdo.                 
                          -smNNNNNNNNNNNNNNNNmhs+:.```              ```.:+shmNNNNNNNNNNNNNNNNms-               
                        .smNNNNNNNNNNNNNNmho:.`                            `.:ohmNNNNNNNNNNNNNNms.             
                      `+dNNNNNNNNNNNNNmh+-`                                    `-+hmNNNNNNNNNNNNNd+`           
                     -hNNNNNNNNNNNNNds-`                                          `-sdNNNNNNNNNNNNNh-          
                   `+mNNNNNNNNNNNNdo.               .-:-.`                           .odNNNNNNNNNNNNm+`        
                  `smNNNNNNNNNNNdo.               -sdmNmdh/`                           .odNNNNNNNNNNNms`       
                 .yNNNNNNNNNNNmy.                -mNNNNNNNm+                             .ymNNNNNNNNNNNy.      
                `hNNNNNNNNNNNm/`                 +NNNNNNNNNh                              `/mNNNNNNNNNNNh`     
               `yNNNNNNNNNNNh-                   `ymNNNNNNm:                                -hNNNNNNNNNNNy`    
               oNNNNNNNNNNNh.                     `/hNNNNNs          `.--.`                  .hNNNNNNNNNNNo    
              :mNNNNNNNNNNh.                        /NNNNNs        `+hmNNmh+`                 .hNNNNNNNNNNm:   
             `hNNNNNNNNNNm-                         .mNNNNs        sNNNNNNNNo                  -mNNNNNNNNNNh`  
             /NNNNNNNNNNN/                           hNNNNh       `mNNNNNNNNd`                  /NNNNNNNNNNN/  
             dNNNNNNNNNNh`          .-/:.`           oNNNNm`       sNNNNNNNmo                   `hNNNNNNNNNNd  
            -NNNNNNNNNNN/         .smNNNNd/          /NNNNN.       sNNNNNmy:                     /NNNNNNNNNNN- 
            .///////////`         hNNNNNNNm/         -NNNNN+      `mNNNNy`                       `///////////. 
                                  dNNNNNNNNh`        .mNNNNy      +NNNNm.                                      
                                  :dNNNNNNNNh-       `dNNNNm.    .mNNNNo                                       
                                   `/ossdNNNNm+`     `dNNNNNo   `hNNNNm.                                       
                                        `+mNNNNd/`   :NNNNNNNs/+dNNNNNs                                        
                                          .sNNNNNdo/+mNNNNNNNNNNNNNNNN/                                        
            .///////////`                   /dNNNNNNNNNNNNNNNNNNNNNNNN/                          `///////////. 
            -NNNNNNNNNNN/                    .yNNNNNNNNNNNNNNNNNNNNNNNh`         .oyhs/`         /NNNNNNNNNNN- 
             dNNNNNNNNNNh`                    `omNNNNNNNNNNNNNNNNNNNNNNy:.```..:omNNNNms        `hNNNNNNNNNNd  
             /NNNNNNNNNNN/                      +mNNNNNNNNNNNNNNNNNNNNNNmmdddmmmNNNNNNNm        /NNNNNNNNNNN/  
             `hNNNNNNNNNNm-                      sNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdhdNNNh:       -mNNNNNNNNNNh`  
              :mNNNNNNNNNNh.                     .mNNNNNNNNNNNNNNNNNNNNNNNNmho:.``.---`       .hNNNNNNNNNNm:   
               oNNNNNNNNNNNh.                     +NNNNNNNNNNNNNNNNNNNNNNmo.`                .hNNNNNNNNNNNo    
               `yNNNNNNNNNNNh-                    `yNNNNNNNNNNNNNNNNNNNms-                  -hNNNNNNNNNNNy`    
                `hNNNNNNNNNNNm/`                   `sNNNNNNNNNNNNNNNNNd:`                 `/mNNNNNNNNNNNh`     
                 .yNNNNNNNNNNNmy.                   `+dNNNNNNNNNNNNNd+.                  .ymNNNNNNNNNNNy.      
                  `smNNNNNNNNNNNdo.                   `/ydmmNNNmdhs:.                  .odNNNNNNNNNNNms`       
                   `+mNNNNNNNNNNNNdo.                    `.-::--.`                   .odNNNNNNNNNNNNm+`        
                     -hNNNNNNNNNNNNNds-`                                          `-sdNNNNNNNNNNNNNh-          
                      `+dNNNNNNNNNNNNNmh+-`                                    `-+hmNNNNNNNNNNNNNd+`           
                        .smNNNNNNNNNNNNNNmho:.`                            `.:ohmNNNNNNNNNNNNNNms.             
                          -smNNNNNNNNNNNNNNNNmhs+:.```              ```.:+shmNNNNNNNNNNNNNNNNms-               
                            .odmNNNNNNNNNNNNNNNNNNmdhyo            oyhdmNNNNNNNNNNNNNNNNNNmdo.                 
                              `/ymNNNNNNNNNNNNNNNNNNNNd`          `dNNNNNNNNNNNNNNNNNNNNmy/`                   
                                 .+hmmNNNNNNNNNNNNNNNNd`          `dNNNNNNNNNNNNNNNNmmh+.                      
                                    ./sdmNNNNNNNNNNNNNd`          `dNNNNNNNNNNNNNmds/.                         
                                        ./ohmmNNNNNNNNd`          `dNNNNNNNNmmho/.                             
                                            `.:+sydmmNd`          `dNmmdys+:.`                                 
                                                    `.-            -.`                                         

            

"""
if __name__ == '__main__':
    main()