import numpy as np
## Number of random coordinates to be generated.
N = 20000

## Number of times the experiment is repeated.  
repeat = 10

##Radius of circle.
radius = 2

   ## ### Stochastically calculates area of a circle. 
    # Does so by generating random coordinates and calculating fraction of coordinates lying inside the circle to that of total coordinates.
    # The coordinate is considered inside the  circle if \f$ \sqrt{(x-r)^2 + (y-r)^2} \leq r \f$ where \f$ r \f$ is the radius of the circle.
    # <img src="./../images/view.png" width="400" height="400" style="horizontal-align:middle"/>
    # 
    # The fraction is then scaled by total area in which coordinates are generated to get area of the circle (unit).
    # @param N for number of coordinates to generate.
    # @param radius for radius of the circle.
def get_circle_area(N, radius):
    inside_circle = np.sum([(np.random.uniform(low=0, high=2*radius)-radius)**2 + (np.random.uniform(low=0, high=2*radius)-radius)**2 <= radius**2 for _ in range(N)])
    circle_area = ((2*radius)**2)*(inside_circle/N)
    return circle_area

## List of obtained areas for all the experiments 
areas_repeated = [get_circle_area(N, radius) for _ in range(repeat)]
## Mean value of area obtained in all experiments.
circle_area = np.mean(areas_repeated)
## Standard Deviation of area obtained in all experiments
std_circle_area = np.std(areas_repeated)


print("Unit circle Area = ",circle_area,"+-",std_circle_area,"(1 std)")
