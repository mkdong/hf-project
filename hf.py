#!/usr/bin/env python3
import sys
import subprocess

if __name__=='__main__':
    if len(sys.argv) < 2:
        sys.stderr.write("Error: Input file is not given\n")
        exit(-1)

    fname = sys.argv[1]
    if not fname.endswith('.hf'):
        sys.stderr.write("Error: Input file must end with .hf\n")
        exit(-1)
    fbase = fname[:-3]
    with open(fname, 'r') as f:
        lines = f.readlines()
        main = lines[1][:-1].split(' ')
        if main[0] != "h" or main[2] != "f":
            sys.stderr.write("Error syntax at line 1: " + lines[1] + "\n")
            exit(-1)
        prog = '''
        #include <stdio.h>
        
        const char *festival = "''' + main[1] + '''";
        int main()
        {
            printf("Happy %s Festival!\\n", festival);
            return 0;
        }
        '''
        subprocess.run(["gcc", "-o", fbase, "-x", "c++", "-"], input=bytes(prog, encoding='UTF-8'))

