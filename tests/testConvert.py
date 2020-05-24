#! /usr/bin/env python
import os
import sys
sys.path.append(os.path.realpath('.'))
from convert import *

def main():
    testToDec()
    print("All tests pass.")


def testToDec():
    assert convertToDec("1011", 2) == 11
    assert convertToDec("1", 2) == 1
    assert convertToDec("0", 2) == 0
    assert convertToDec("101110110001", 2) == 2993

    assert convertToDec("1011", 3) == 31
    assert convertToDec("1", 3) == 1
    assert convertToDec("20", 3) == 6
    assert convertToDec("212012121222", 3) == 456812

    assert convertToDec("1011", 4) == 69
    assert convertToDec("1", 4) == 1
    assert convertToDec("30", 4) == 12
    assert convertToDec("3301303031013030", 4) == 4056732108

    assert convertToDec("210404242043222", 5) == 13631987312
    assert convertToDec("4", 5) == 4

    assert convertToDec("113205530032211", 6) == 98740429999
    assert convertToDec("5", 6) == 5

    assert convertToDec("14205006446", 7) == 456009812
    assert convertToDec("6", 7) == 6

    assert convertToDec("16747606430162431", 8) == 526100012786969
    assert convertToDec("7", 8) == 7

    assert convertToDec("1330672840156", 9) == 387326391270
    assert convertToDec("8", 9) == 8

    assert convertToDec("32639721910", 10) == 32639721910
    assert convertToDec("9", 10) == 9

    assert convertToDec("A460A770A", 11) == 2232323444
    assert convertToDec("A", 11) == 10

    assert convertToDec("7181838472B652", 12) == 763917391021022
    assert convertToDec("B", 12) == 11

    assert convertToDec("31386607A902C", 13) == 72190101011911
    assert convertToDec("C", 13) == 12

    assert convertToDec("92BBB7D11810", 14) == 37269320320918
    assert convertToDec("D", 14) == 13

    assert convertToDec("6996C9E9474", 15) == 3830128012009
    assert convertToDec("E", 15) == 14

    assert convertToDec("1A27A29ADF7E7C", 16) == 7361928731000444
    assert convertToDec("F", 16) == 15

    assert convertToDec("796CC3G814F10D13", 17) == 21619199999125262191
    assert convertToDec("G", 17) == 16

    assert convertToDec("1FHB728BD65E", 18) == 121323115895000
    assert convertToDec("H", 18) == 17

    assert convertToDec("ACDFHB85I", 19) == 181213123123
    assert convertToDec("I", 19) == 18

    assert convertToDec("11J31BD6CFB", 20) == 11242341333111
    assert convertToDec("J", 20) == 19

    assert convertToDec("GAK5CF6FGD", 21) == 13123211929288
    assert convertToDec("K", 21) == 20

    assert convertToDec("2593287LL", 22) == 123259974111
    assert convertToDec("L", 22) == 21

    assert convertToDec("2ILECM86J", 23) == 221111321234
    assert convertToDec("M", 23) == 22

    assert convertToDec("BAM4NL3", 24) == 2189127099
    assert convertToDec("N", 24) == 23

    assert convertToDec("DLG0CIOE5DM", 25) == 1322329775222222
    assert convertToDec("O", 25) == 24

    assert convertToDec("1D6F2P4FJND", 26) == 213124999991111
    assert convertToDec("P", 26) == 25

    assert convertToDec("317MAMQNBJ", 27) == 23241123424234
    assert convertToDec("Q", 27) == 26

    assert convertToDec("241E48RPH", 28) == 810301202301
    assert convertToDec("R", 28) == 27

    assert convertToDec("R2O4IHAS4D", 29) == 393110191991111
    assert convertToDec("S", 29) == 28

    assert convertToDec("45778T42", 30) == 91301012222
    assert convertToDec("T", 30) == 29

    assert convertToDec("1DLH1P39MU", 31) == 38120109922222
    assert convertToDec("U", 31) == 30

    assert convertToDec("2FS2Q6KIJRVPSAK8SE7", 32) == 3090120893271111111111111111
    assert convertToDec("V", 32) == 31

    assert convertToDec("VW3NF3", 33) == 1251280011
    assert convertToDec("W", 33) == 32

    assert convertToDec("OEKHUXAV", 34) == 1283120309111
    assert convertToDec("X", 34) == 33

    assert convertToDec("CQCYY5UEGL0B", 35) == 1231336669420111111
    assert convertToDec("Y", 35) == 34

    assert convertToDec("JHG5UZR89DM", 36) == 71239126669420666
    assert convertToDec("Z", 36) == 35

    print("convertToDec test passes.")


if __name__ == "__main__":
    main()
