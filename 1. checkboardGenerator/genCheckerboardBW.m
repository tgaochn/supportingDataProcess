% genCheckerboardBW.m
% @Author : Tian Gao (tgaochn@gmail.com)
% @Link   :
% @Date   : Wed Feb 27 2019
% Description   :

clc; clear; close all; warning off all;

% Create a rectangular checkerboard that is 5 tiles high and 6 tiles wide. 
% The side of every square is 40 pixels in length.
J = checkerboard(40, 5, 6);
J = J > 0.5;
figure
imshow(J)
