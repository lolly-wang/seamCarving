# seamCarving
CIS 581 Course Project

## Source
Implement image resizing utilizing scene carving, based heavily on the methods outlined by Avidan & Shamir in their paper:

"Seam Carving for Content-Aware Image Resizing"; Avidan, S. & Shamir, A.; 2007

## To run
To implement my project, you can just call the main function in ‘test_script.py’ . 

It will read original image, call the ‘carv’ function and print out the carved image (cut 30*30 in all the provided results). 
For convenience, the ‘gif’ part is contained in ‘carv’ function.

To generate ‘gif’ file, it  calls “ imageio.mimsave("carv_test.gif", frames, fps=8)”function. 

The result ’illusion_result_30*30.png’ is kind of failed, but I find it is really interesting.

