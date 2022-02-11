//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0, 9, 0, 1.0};
//+
Point(3) = {-4, 9, 0, 1.0};
//+
Point(4) = {-4, 0, 0, 1.0};
//+
Line(1) = {4, 1};
//+
Line(2) = {1, 2};
//+
Line(3) = {2, 3};
//+
Line(4) = {3, 4};
//+
Point(5) = {40, 0, 0, 1.0};
//+
Point(6) = {40, 9, 0, 1.0};
//+
Line(5) = {1, 5};
//+
Line(6) = {5, 6};
//+
Line(7) = {6, 2};
//+
Point(7) = {0, -1, 0, 1.0};
//+
Point(8) = {40, -1, 0, 1.0};
//+
Line(8) = {1, 7};
//+
Line(9) = {7, 8};
//+
Line(10) = {8, 5};
//+

//+
Physical Curve("outlet", 11) = {6, 10};
//+
Physical Curve("inlet", 12) = {4};
//+
Physical Curve("walls", 13) = {3, 7, 1, 8, 9};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {7, -2, 5, 6};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {9, 10, -5, 8};
//+
Plane Surface(3) = {3};
//+
Physical Surface("fluid", 14) = {1, 2, 3};
//+

//+
Transfinite Surface {1} = {4, 1, 2, 3};
//+
Transfinite Surface {2} = {1, 5, 6, 2};
//+
Transfinite Surface {3} = {7, 8, 5, 1};
//+

//+
Transfinite Curve {4, 2, 6} = 30 Using Bump 0.25;
//+
Transfinite Curve {3, -1} = 20 Using Progression 1.25;
//+
Transfinite Curve {-7, 5, 9} = 45 Using Progression 1.125;
//+
Transfinite Curve {8, -10} = 10 Using Progression 1.0;
//+
Recombine Surface {1, 2, 3};
