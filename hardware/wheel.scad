difference(){
   cylinder(d=95,h=70);
   cylinder(d=8,h=75);
   for(i = [0,180])
      rotate([0,0,i])
         translate([45,0,0])
            cylinder(d=70,h=75);
}
