### Volume

The program accepts three command-line arguments: input represents the name of the original audio file, output represents the name of the new audio file that should be generated, and factor is the amount by which the volume of the original audio file should be scaled.

The program first reads the header, which is exactly 44 bytes long, from the input file and write the header to the output file. Reads the rest of the data from the WAV file, one 16-bit (2-byte) sample at a time, multiplying each sample by the factor and write the new sample to the output file. All with care for memory allocation.
