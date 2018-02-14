// Gmsh project created on Wed Feb 14 09:11:39 2018
Point(1) = {0, 0, 0, 1.0};
Point(2) = {1, 0, 0, 1.0};
Point(3) = {1, 1, 0, 1.0};
Point(4) = {0, 1, 0, 1.0};

Line(1) = {4, 1};
Line(2) = {1, 2};
Line(3) = {2, 3};
Line(4) = {3, 4};

Line Loop(5) = {1, 2, 3, 4};
Plane Surface(6) = {5};

Physical Point(101) = {4, 1};
Physical Point(102) = {2, 3};

Physical Line(101) = {1};
Physical Line(102) = {3};
Physical Line(201) = {4, 2};

Physical Surface(1) = {6};
