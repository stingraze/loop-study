#!/usr/bin/perl
#Refenced https://perlmaven.com/multi-dimensional-arrays-in-perl for this code.
use strict;
use warnings;

my @matrix;

my $counter1 = 0;
my $counter2 = 0;
my $counter3 = 0;

my $text = "";


while ($counter1 < 3){
	$counter1++;
	while ($counter2 < 3){
		$counter2++;
		while ($counter3 < 3){
			$counter3++;
		$text = "$counter1 $counter2 $counter3";
		$matrix[$counter1][$counter2][$counter3] = $text;
		print "$text\n";
		
		}		
	}
}

#$matrix[1][1] = 'one-one';
#$matrix[1][2] = 'one-two';

#print "$matrix[0][0]\n";
#print "$matrix[1][1]\n";
