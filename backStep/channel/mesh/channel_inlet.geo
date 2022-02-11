// Gmsh project created on Thu Feb 10 12:43:22 2022
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0, 9, 0, 1.0};
//+
Point(3) = {-18, 0, 0, 1.0};
//+
Point(4) = {-18, 9, 0, 1.0};
//+
Point(5) = {0, 0.5, 0, 1.0};
//+
Point(6) = {0, 8.5, 0, 1.0};
//+
Point(7) = {-18, 8.5, 0, 1.0};
//+
Point(8) = {-18, 0.5, 0, 1.0};
//+
Line(1) = {3, 1};
//+
Line(2) = {1, 5};
//+
Line(3) = {5, 6};
//+
Line(4) = {6, 2};
//+
Line(5) = {2, 4};
//+
Line(6) = {4, 7};
//+
Line(7) = {7, 8};
//+
Line(8) = {8, 3};
//+
Line(9) = {8, 5};
//+
Line(10) = {7, 6};
//+
Physical Curve("walls", 11) = {1, 5};
//+
Physical Curve("per1", 12) = {6, 7, 8};
//+
Physical Curve("per2", 13) = {4, 3, 2};
//+
Curve Loop(1) = {1, 2, -9, 8};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {10, 4, 5, 6};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {7, 9, 3, -10};
//+
Plane Surface(3) = {3};
//+
Physical Surface("fluid", 14) = {3, 2, 1};
//+
Transfinite Surface {1};
//+
Transfinite Surface {2};
//+
Transfinite Surface {3};
//+
Transfinite Curve {7, 3} = 25 Using Bump 0.3;
//+
Transfinite Curve {-8, 2, 6, -4} = 12 Using Progression 1.75;
//+
Transfinite Curve {5, 10, 9, 1} = 4 Using Progression 1;
//+
Recombine Surface {2, 3, 1};
