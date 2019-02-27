%% Test QR encoding and decoding
%
% Please download and build the core and javase parts of zxing
% from here - http://code.google.com/p/zxing/
%
javaaddpath('.\3rd_party\zxing-1.6\core\core.jar');
javaaddpath('.\3rd_party\zxing-1.6\javase\javase.jar');

% encode a new QR code
test_encode = encode_qr('123', [32 32]);
figure;imagesc(test_encode);axis image;

% decode
% message = decode_qr(imread('testInput\\04.jpg'));
% message = decode_qr(imread('testInput\\old\\QR_code_for_mobile_English_Wikipedia.svg.png'));
% message