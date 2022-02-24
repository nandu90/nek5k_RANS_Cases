//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0, 8, 0, 1.0};
//+
Point(3) = {-4, 8, 0, 1.0};
//+
Point(4) = {-4, 0, 0, 1.0};
//+
Point(5) = {40, 0, 0, 1.0};
//+
Point(6) = {40, 8, 0, 1.0};
//+
Point(7) = {0, -1, 0, 1.0};
//+
Point(8) = {40, -1, 0, 1.0};
//+//+
Point(9) = {-4.0, 0.5, 0, 1.0};
//+
Point(10) = {-4.0, 7.5, 0, 1.0};
//+
Point(11) = {40, 7.5, 0, 1.0};
//+
Point(12) = {40, 0.5, 0, 1.0};
//+
Point(13) = {0, 0.5, 0, 1.0};
//+
Point(14) = {0, 7.5, 0, 1.0};
//+
Point(15) = {2.0, 8, 0, 1.0};
//+
Point(16) = {2.0, 7.5, 0, 1.0};
//+
Point(17) = {2.0, 0.5, 0, 1.0};
//+
Point(18) = {2.0, 0.0, 0, 1.0};
//+
Point(19) = {2.0, -1.0, 0, 1.0};
//+
Line(1) = {4, 1};
//+
Line(2) = {1, 7};
//+
Line(3) = {7, 19};
//+
Line(4) = {19, 8};
//+
Line(5) = {8, 5};
//+
Line(6) = {5, 12};
//+
Line(7) = {12, 11};
//+
Line(8) = {11, 6};
//+
Line(9) = {6, 15};
//+
Line(10) = {15, 2};
//+
Line(11) = {2, 3};
//+
Line(12) = {3, 10};
//+
Line(13) = {10, 9};
//+
Line(14) = {9, 4};
//+
Line(15) = {10, 14};
//+
Line(16) = {14, 16};
//+
Line(17) = {16, 11};
//+
Line(18) = {5, 18};
//+
Line(19) = {18, 1};
//+
Line(20) = {9, 13};
//+
Line(21) = {13, 17};
//+
Line(22) = {1, 13};
//+
Line(23) = {13, 14};
//+
Line(24) = {14, 2};
//+
Line(25) = {15, 16};
//+
Line(26) = {16, 17};
//+
Line(27) = {17, 18};
//+
Line(28) = {18, 19};
//+
Line(29) = {17, 12};
//+
Physical Curve("walls", 30) = {1, 2, 3, 4, 11, 10, 9};
//+
Physical Curve("inlet", 31) = {14, 13, 12};
//+
Physical Curve("outlet", 32) = {5, 6, 7, 8};
//+
Curve Loop(1) = {14, 1, 22, -20};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {12, 15, 24, 11};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {13, 20, 23, -15};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {2, 3, -28, 19};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {22, 21, 27, 19};
//+
Plane Surface(5) = {5};
//+
Curve Loop(6) = {23, 16, 26, -21};
//+
Plane Surface(6) = {6};
//+
Curve Loop(7) = {24, -10, 25, -16};
//+
Plane Surface(7) = {7};
//+
Curve Loop(8) = {28, 4, 5, 18};
//+
Plane Surface(8) = {8};
//+
Curve Loop(9) = {27, -18, 6, -29};
//+
Plane Surface(9) = {9};
//+
Curve Loop(10) = {26, 29, 7, -17};
//+
Plane Surface(10) = {10};
//+
Curve Loop(11) = {25, 17, 8, 9};
//+
Plane Surface(11) = {11};
//+
Physical Surface("fluid", 33) = {3, 2, 7, 11, 6, 10, 1, 5, 4, 9, 8};
//+
Transfinite Surface {1} = {4, 1, 13, 9};
//+
Transfinite Surface {3} = {9, 13, 14, 10};
//+
Transfinite Surface {2} = {10, 14, 2, 3};
//+
Transfinite Surface {5} = {1, 18, 17, 13};
//+
Transfinite Surface {6} = {13, 17, 16, 14};
//+
Transfinite Surface {7} = {14, 16, 15, 2};
//+
Transfinite Surface {4} = {7, 19, 18, 1};
//+
Transfinite Surface {8} = {19, 8, 5, 18};
//+
Transfinite Surface {9} = {18, 5, 12, 17};
//+
Transfinite Surface {10} = {17, 12, 11, 16};
//+
Transfinite Surface {11} = {16, 11, 6, 15};
//+
Transfinite Curve {-14, 22, -27, 6, 12, -24, 25, -8} = 4 Using Progression 1.0;
//+
Transfinite Curve {13, 23, 26, 7} = 30 Using Progression 1.0;
//+
Transfinite Curve {2, 28, 5} = 6 Using Bump 1.0;
//+
Transfinite Curve {11, -15, -20, -1} = 20 Using Progression 1.2;
//+
Transfinite Curve {-10, 16, 21, -19, 3} = 20 Using Progression 1.2;
//+
Transfinite Curve {-9, 17, 29, -18, 4} = 40 Using Progression 1.025;
//+
Recombine Surface {3, 2, 1, 6, 7, 11, 10, 9, 5, 4, 8};
