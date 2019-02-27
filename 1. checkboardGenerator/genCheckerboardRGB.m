% genCheckerboardRGB.m
% @Author : Tian Gao (tgaochn@gmail.com)
% @Link   : 
% @Date   : Wed Feb 27 2019
% Description   : 

clc; clear; close all; warning off all;

numsquares = [20, 20];  %rows columns
squaresize = 100;

pattern = rand([numsquares, 3]);
checkerboard = imresize(pattern, squaresize, 'nearest');

imshow(checkerboard);
