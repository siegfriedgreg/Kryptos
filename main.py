from kryptos import Krux as kx
import os

'''

Kryptos Solving Board 

1) create tools to solve K1-k2
    A) use pk_1 to "cover" elements in k_1
    B) create veng_table
    C) Algorithm:
        1) using pk_1[n], find row of veng_table[n][0]
        2) using row of veng_table[n][0], find k_1[n]
        3) using column of k_1[n], find veng_table[0][n]
        4) return veng_table[0][n]
2) create tools to solve k3
    A) clear '?'s
    B) KEY[14x24]   create 14 row 24 col matrix from string;
    C) KEY[24x14]   rotate left 90;
    D) KEY[42x8]    create 42 row 8 col matrix;
    E) KEY[8x42]    rotate left 90;
3) create tools to solve k4
    A) Figure out?????

4) create tools to solve k5

'''

def screen_clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

################################################################################
####------------>>>>            MAIN PROGRAM
################################################################################

if __name__ == '__main__':

    # instantiate class
    me = kx()
    table = me.veng_table()
    ans = ""
    repeat = True
    screen_clear()

    while repeat:

        # Display Menu
        print(" Please choose a display option: ")
        print("\t Solve K_1 = 1 ")
        print("\t Solve K_2 = 2 ")
        print("\t Solve K_3 = 3 ")
        print("\t --- Quit Program! = 9 ")

        # Ask for input
        input_var = input("Choice:  ")

        # Clear the command|terminal
        screen_clear()

        # Filter input to proper request
        if input_var == '1':
            ans = me.vc_solve12(table, 1)
        elif input_var == '2':
            ans = me.vc_solve12(table, 2)
        elif input_var == '3':
            ans = me.vc_solve3()
        elif input_var == '9':
            repeat = False
        else:
            print("---- Please Input A Valid Choice! ----\n")

        print("\n" + str(ans[0::]) + "\n")

    # Clean Up!
    del(me) 

    screen_clear()

################################################################################
####------------>>>>            END PROGRAM
################################################################################
  
