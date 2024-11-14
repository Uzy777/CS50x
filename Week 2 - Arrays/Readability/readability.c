#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// int count_letters(string text);
// int count_words(string text);
// int count_sentences(string text);

int main(void)
{
    // Initialise variables
    int letters = 0;
    int words = 1;
    int sentences = 0;

    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // if (text[i] > 65 && text[i] < 90) || (text[i] > 97 && text[i] < 122)
        if (isalpha(text[i]))
        {
            letters++;
        }

        else if (text[i] == ' ')
        {
            words++;
        }

        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    // Compute the Coleman-Liau index
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    // Print the grade level
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else if (index > 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %i\n", index);
    }
}

// int count_letters(string text)
// {
//     // Return the number of letters in text
// }

// int count_words(string text)
// {
//     // Return the number of words in text
// }

// int count_sentences(string text)
// {
//     // Return the number of sentences in text
// }
