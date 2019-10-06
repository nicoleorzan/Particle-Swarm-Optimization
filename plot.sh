#!/bin/bash      

gnuplot -e "
set terminal gif animate delay 0.5;
set output 'file_test.gif';

set xrange [-1.2:0.6];
set yrange [-1:1];
set ticslevel 0;

set xlabel '{/Symbol r}';
set ylabel 'sin(3{/Symbol r})';
set nokey;

filedata = 'file_test.txt';
n = system(sprintf('cat %s | wc -l', filedata));

do for [j=1:n-1] {
    set title 'time '.j;
    plot filedata u 2:3 every ::1::j w l lw 2, filedata u 2:3 every ::j::j w p pt 7 ps 2;
    pause 0.105;
};
"
