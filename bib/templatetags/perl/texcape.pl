#!/usr/bin/perl -w
use TeX::Encode;
use Encode;
use utf8;
use strict;

while (my $line = <>) {
	print encode('latex', decode('utf8', $line))
}
