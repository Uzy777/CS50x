#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512 // As per notes

int main(int argc, char *argv[])
{
    // Check for correct usage
    if (argc != 2)
    {
        // Print error message if the program is not given the correct number of arguments
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open the forensic image file specified in the command-line arguments (NOTES)
    char *file = argv[1];
    FILE *raw_file = fopen(file, "r");
    if (raw_file == NULL)
    {
        // Print an error message to standard error if the forensic image file cannot be opened
        // (NOTES)
        printf("Could not open %s.\n", file);
        return 1;
    }

    // Initialise variables
    bool found_jpg = false;

    // Counter for then umber of JPEGs found
    int jpg_counter = 0;

    // Buffer to store a block of data from the forensic image
    uint8_t buffer[BLOCK_SIZE];

    // Array to store the filename of the current JPEG
    char jpg_name[8];

    // Pointer to the current JPEG file
    FILE *outptr = NULL;

    // Read the forensic image file block by block
    while (fread(buffer, BLOCK_SIZE, 1, raw_file) == 1)
    {
        // Check if this block marks the start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous JPEG file, if one was open
            if (found_jpg)
            {
                fclose(outptr);
            }
            else
            {
                found_jpg = true;
            }
            // Open a new JPEG file
            // Generate the filename for the new JPEG image file based on the jpg_count variable
            sprintf(jpg_name, "%03d.jpg", jpg_counter);

            // Open a new JPEG image file with the generated filename
            outptr = fopen(jpg_name, "w");

            if (outptr == NULL)
            {
                fclose(raw_file);
                // Print an error if the new JPEG image file cannot be created
                printf("Could not create %s. \n", jpg_name);
                return 3;
            }
            // Increment the jpg_counter variable
            jpg_counter++;
        }

        // Write the current block to the current JPEG file, if one is open
        if (found_jpg)
        {
            fwrite(buffer, BLOCK_SIZE, 1, outptr);
        }
    }

    // Close the forensic image filed and the last JPEG file, if one was open
    fclose(raw_file);
    if (found_jpg)
    {
        fclose(outptr);
    }

    // Exit the program with a status code of 0 to indicate success
    return 0;
}
