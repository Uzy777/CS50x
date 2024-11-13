#include <cs50.h>
#include <stdio.h>

// void print_row(int spaces, int bricks);

int main(void)
{
    int height;
    // Prompt the user for the pyramid's height
    do
    {
        height = get_int("Height: ");
    }
    // Only allow 1 - 8 inclusively anything else will repeat
    while ((height < 1 || height > 8));

    // Print a pyramid of that height
    for (int row = 0; row < height; row++)
    {
        // Print spaces
        for (int space = 0; space < height - row - 1; space++)
        {
            printf(" ");
        }

        // Print bricks
        for (int column = 0; column <= row; column++)
        {
            printf("#");
        }

        printf("\n");
    }
}

// void print_row(int spaces, int bricks)
// {
//     // Print spaces

//     // Print bricks
// }
