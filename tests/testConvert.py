#! /usr/bin/env python
import os
import sys
sys.path.append(os.path.realpath('.'))
from convert import *

def main():
    testToDec()
    testToBase()
    print("All tests pass.")


def testToBase():
    assert convertToBase(10, 2) == "1010"
    assert convertToBase(73971310, 3) == "12011012010120011"
    assert convertToBase(761273918309180, 4) == "2231011333211132210030330"
    assert convertToBase(36821238, 5) == "33411234423"
    assert convertToBase(123981301301, 6) == "132542313322005"
    assert convertToBase(30180191, 7) == "514345616"
    assert convertToBase(8373917, 8) == "37743235"
    assert convertToBase(823727881295, 9) == "2822160288888"
    assert convertToBase(7327928190, 10) == "7327928190"
    assert convertToBase(76912237912, 11) == "2A688A53794"
    assert convertToBase(89323983291, 12) == "1538A507B63"
    assert convertToBase(3797937201, 13) == "486AC4526"
    assert convertToBase(37269320320918, 14) == "92BBB7D11810"
    assert convertToBase(73981310, 15) == "67655C5"
    assert convertToBase(8373981010, 16) == "1F320CF52"
    assert convertToBase(23897401801, 17) == "3740E7GAC"
    assert convertToBase(8931013387128, 18) == "2907G848520"
    assert convertToBase(389871030, 19) == "858BF2H"
    assert convertToBase(9371937131, 20) == "768EC2GB"
    assert convertToBase(381731293791, 21) == "A1JHDAAGF"
    assert convertToBase(381731293791, 22) == "6L0I7C851"
    assert convertToBase(3218763128, 23) == "LH22E8M"
    assert convertToBase(2131231439999, 24) == "J8G69KN7N"
    assert convertToBase(8279733980, 25) == "18ML2O95"
    assert convertToBase(2982179301, 26) == "9GPN9LN"
    assert convertToBase(298217930122, 27) == "11DK8HDC1"
    assert convertToBase(23342538, 28) == "19R9I2"
    assert convertToBase(19823120101, 29) == "149D6AQG"
    assert convertToBase(12093011019, 30) == "GHJJ8R9"
    assert convertToBase(191290291218, 31) == "6TGKFGND"
    assert convertToBase(213425499, 32) == "6BH7AR"
    assert convertToBase(4235424578679, 33) == "30CHU6C9U"
    assert convertToBase(4242579000, 34) == "2PCQN1A"
    assert convertToBase(230483304892, 35) == "3KDBIVMM"
    assert convertToBase(5253599098, 36) == "2EVUV0A"
    print("convertToBase test passes.")


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
