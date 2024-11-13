https://cs50.harvard.edu/x/2024/psets/1/mario/less/

# Problem to Solve

In a file called `mario.c` in a folder called `mario-less`, implement a program in C that recreates that pyramid, using hashes (`#`) for bricks, as in the below:

```
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

But prompt the user for an `int` for the pyramid’s actual height, so that the program can also output shorter pyramids like the below:

```
  #
 ##
###
```

Re-prompt the user, again and again as needed, if their input is not greater than 0 or not an `int` altogether.


# How to Test
Does your code work as prescribed when you input:

- `-1` or other negative numbers?
- `0`?
- `1` or other positive numbers?
- letters or words?
- no input at all, when you only hit Enter?
