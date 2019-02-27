% genCheckerboardWithoutGreen.m
% @Author : Tian Gao (tgaochn@gmail.com)
% @Link   : 
% @Date   : Wed Feb 27 2019
% Description   : 

clc; clear; close all; warning off all;

numsquares = [20, 20];  %rows columns
squaresize = 100;

pattern = rand([numsquares, 3]);
checkerboard = imresize(pattern, squaresize, 'nearest');

% remove green channel using HSV color space
% Convert RGB image to chosen color space
I = rgb2hsv(checkerboard);

% Define thresholds for channel 1 based on histogram settings
channel1Min = 0.571;
channel1Max = 0.172;

% Define thresholds for channel 2 based on histogram settings
channel2Min = 0.000;
channel2Max = 1.000;

% Define thresholds for channel 3 based on histogram settings
channel3Min = 0.000;
channel3Max = 1.000;

% Create mask based on chosen histogram thresholds
sliderBW = ((I(:, :, 1) >= channel1Min) | (I(:, :, 1) <= channel1Max)) & ...
    (I(:, :, 2) >= channel2Min) & (I(:, :, 2) <= channel2Max) & ...
    (I(:, :, 3) >= channel3Min) & (I(:, :, 3) <= channel3Max);
BW = sliderBW;

% Initialize output masked image based on input image.
maskedRGBImage = checkerboard;

% Set background pixels where BW is false to zero.
maskedRGBImage(repmat(~BW, [1 1 3])) = 0;

checkerboard = maskedRGBImage;
imshow(checkerboard)
