#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    char key[26];
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Key must contain only letters\n");
            return 1;
        }
        for (int j = i + 1; j < 26; j++)
        {
            if (argv[1][i] == argv[1][j])
            {
                printf("Duplicate letter(s)\n");
                return 1;
            }
        }
        key[i] = tolower(argv[1][i]);
    }

    string text = get_string("plaintext:  ");
    int n = strlen(text);
    char cipher[n];
    for (int i = 0; i <= n; i++)
    {
        if (!isalpha(text[i]))
        {
            cipher[i] = text[i];
        }
        else
        {
            if (isupper(text[i]))
            {
                int pos = text[i] - 65;
                cipher[i] = toupper(key[pos]);
            }
            else
            {
                int pos = text[i] - 97;
                cipher[i] = key[pos];
            }
        }
    }
    printf("ciphertext: %s", cipher);
    printf("\n");
    return 0;

}