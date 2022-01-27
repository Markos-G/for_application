#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string);
int count_words(string);
int count_sentences(string);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sen = count_sentences(text);
    // printf("%i, %i ,%i\n",letters,words,sen);
    int index = round(0.0588 * letters / words * 100 - 0.296 * sen / words * 100 - 15.8);
    // printf("%i\n",(int) round(index));
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 1 && index <= 16)
    {
        printf("Grade %i\n", index);
    }
    else
    {
        printf("Grade 16+\n");
    }
}



int count_letters(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i <= n; i++)
    {
        if (isalpha(text[i]))
        {
            count++ ;
        }
    }
    return count;
}

int count_words(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i <= n; i++)
    {
        if (text[i] == ' ' || text[i] == '\0')
        {
            count++ ;
        }
    }
    return count;
}

int count_sentences(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i <= n; i++)
    {
        if (text[i] == '.' ||
            text[i] == '?' ||
            text[i] == '!')
        {
            count++ ;
        }
    }
    return count;
}