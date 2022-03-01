### Readability

A number of “readability tests” have been developed over the years that define formulas for computing the reading level of a text. One such readability test is the Coleman-Liau index. The Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to understand some text. The formula is:

***index = 0.0588 * L - 0.296 * S - 15.8***

where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

We write a program that takes a text and determines its reading level. Specifically:
- Considers **letters** to be uppercase or lowercase alphabetical character, not punctuation, digits, or other symbols.
- We consider any sequence of characters separated by a space to be a **word**. We assume that a sentence will not start or end with a space, and assume that a sentence will not have multiple spaces in a row.
- We determining the number of **sentences** as any sequence of characters that ends with a period an exclamation point or a question mark as well. Not all periods necessarily mean the sentence is over.
