/*
 * day4b.c
 * Copyright (C) 2015 konrad <konrad@serenity>
 *
 * Distributed under terms of the MIT license.
 *
 * Written for the advent of code
 *
 * The python script was not fast enough. This finds hashes with leading zeros many times faster.
 * Like, literally thousands of times faster. This runs in just under 5 seconds for me.
 * The python script ran for three days.
 */
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <bsd/md5.h>

int main(int argc, char* argv[]) {
    struct MD5Context context;
    unsigned char digest[16];
    const char* input = "yzbqklnj";
    long appNumber = 0;
    char* appNumberAscii = malloc(32);
    long firstBytes;

    while(1) {
        //Re-initialize so we start clean every time.
        MD5Init(&context);

        //Hash my specific input string
        MD5Update(&context, input, strlen(input));

        //Hash the ascii representation of the current number.
        sprintf(appNumberAscii, "%d", appNumber);
        MD5Update(&context, appNumberAscii, strlen(appNumberAscii));
        MD5Final(digest, &context);

        //Grab the first 3 bytes.
        //Note: This doesn't work with odd numbers of leading zeros.
        //Something to do with big endianness.
        firstBytes = (*(long*)digest) & 0xFFFFFF;
        if(firstBytes == 0) break;

        appNumber++;
    }

    printf("Found! Number is: %d\n", appNumber);

    free(appNumberAscii);
}


