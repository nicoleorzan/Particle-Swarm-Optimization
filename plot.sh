#!/bin/bash      

gnuplot -e "
set xrange [-1:1];
set yrange [-1:1];
set ticslevel 0;

set xlabel 'x';
set ylabel 'y';

filedata = 'file2.txt';
n = system(sprintf('cat %s | wc -l', filedata));

do for [j=1:n-1] {
    set title 'time '.j;
    plot filedata u 2:3 every ::1::j w l lw 2, filedata u 2:3 every ::j::j w p pt 7 ps 2;
    pause 0.105;
};
"
