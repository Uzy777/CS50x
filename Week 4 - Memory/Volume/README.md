https://cs50.harvard.edu/x/2024/psets/4/volume/

![alt text](https://cs50.harvard.edu/x/2024/psets/4/volume/wav_file.png)


# Problem to Solve
WAV files are a common file format for representing audio. WAV files store audio as a sequence of “samples”: numbers that represent the value of some audio signal at a particular point in time. WAV files begin with a 44-byte “header” that contains information about the file itself, including the size of the file, the number of samples per second, and the size of each sample. After the header, the WAV file contains a sequence of samples, each a single 2-byte (16-bit) integer representing the audio signal at a particular point in time.

Scaling each sample value by a given factor has the effect of changing the volume of the audio. Multiplying each sample value by 2.0, for example, will have the effect of doubling the volume of the origin audio. Multiplying each sample by 0.5, meanwhile, will have the effect of cutting the volume in half.

In a file called `volume.c` in a folder called `volume`, write a program to modify the volume of an audio file.


# Implementation Details
Complete the implementation of `volume.c`, such that it changes the volume of a sound file by a given factor.

- The program should accept three command-line arguments. The first is `input`, which represents the name of the original audio file. The second is `output`, which represents the name of the new audio file that should be generated. The third is `factor`, which is the amount by which the volume of the original audio file should be scaled.
    - For example, if `factor` is `2.0`, then your program should double the volume of the audio file in input and save the newly generated audio file in `output`.
- Your program should first read the header from the input file and write the header to the output file.
- Your program should then read the rest of the data from the WAV file, one 16-bit (2-byte) sample at a time. Your program should multiply each sample by the `factor` and write the new sample to the output file.
    - You may assume that the WAV file will use 16-bit signed values as samples. In practice, WAV files can have varying numbers of bits per sample, but we’ll assume 16-bit samples for this problem.
- Your program, if it uses `malloc`, must not leak any memory.

