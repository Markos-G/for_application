### Recover

JPEGs have “signatures,” patterns of bytes that can distinguish them from other file formats. Specifically, the first three bytes of JPEGs are ***0xff 0xd8 0xff*** from first byte to third byte, left to right. The fourth byte, meanwhile, is either ***0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee, or 0xef***. Put another way, the fourth byte’s first four bits are ***1110***.

Digital cameras tend to store photographs contiguously on memory cards, whereby each photo is stored immediately after the previously taken photo. Accordingly, the start of a JPEG usually demarks the end of another. However, digital cameras often initialize cards with a FAT file system whose “block size” is 512 bytes. The implication is that these cameras only write to those cards in units of 512 B.

Each time we find a signature, we open a new file for writing and start filling that file with bytes from my memory card, closing that file only once encountering another signature. We read 512 B at a time into a buffer for efficiency’s sake.

The program accepts exactly one command-line argument, the name of a forensic image from which to recover JPEGs.
The files generated are named ###.jpg, where ### is a three-digit decimal number, starting with 000 for the first image and counting up.
We take care for any memory leakage.
