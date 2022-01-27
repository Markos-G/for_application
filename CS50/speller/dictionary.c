// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

unsigned int w_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 6000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int len = strlen(word);
    char x_word[len];
    x_word[len] = '\0';
    for (int i = 0; i < len; i++)
    {
        x_word[i] = tolower(word[i]);
    };
    unsigned int pos = hash(x_word);
    node *current = table[pos];
    while (current != NULL)
    {
        if (strcmp((*current).word, x_word) == 0)
        {
            return true;
        }
        else
        {
            current = (*current).next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //Written by Daniel J. Bernstein (also known as djb2)
    unsigned long hash = 5381;
    int c;
    while ((c = *word++))
    {
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    }
    return (unsigned int)(hash % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *open_dict = fopen(dictionary, "r");
    if (open_dict == NULL)
    {
        return false;
    }

    char word[LENGTH + 1] ;
    while (fscanf(open_dict, "%s", word) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(open_dict);
            return false;
        }
        (*new_node).next = NULL;
        strcpy((*new_node).word, word);
        // make words case-insensitive they are already
        // for ( int i =0 ; i < strlen(new_node->word); i++)
        // {
        //     new_node->word[i] = tolower(new_node->word[i]);
        // }
        unsigned int pos = hash(word);
        (*new_node).next = table[pos];
        table[pos] = new_node;
        w_count += 1;
    }
    fclose(open_dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return w_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *current = table[i];
        while (current != NULL)
        {
            node *temp = (*current).next;
            free(current);
            current = temp;
        }
    }
    return true;
}
