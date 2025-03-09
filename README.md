# Rubik's Mosaic Text Generation
I like Rubik's Cubes. My average time to solve a 3X3 is about a minute. I wanted to explore creating Rubik's Cube mosaics, so I purchased 100 "Magic Cubes" for 12 cents each. Whenever I want to add text to a mosaic, I struggle to get the letters and spacing correct, so I created this program to help me generate the text.

I first created a Python CLI using the Pillow Image library to test if this app was going to work. After I was able to prove that it was possible to generate the images, I created the generator as an Angular app. The app is customizable to adapt to any size mosaic you want. Here are the steps the app takes to create the mosaic:
<ol>
<li>The user enters the text for the mosaic</li>
<li>The user chooses if they want the text vertically aligned to the top, center, or bottom of the mosaic. The app will then calculate the minimum number of cubes needed to make the mosaic and the dimensions of the mosaic.</li>
<li>The user can set the desired dimensions of the mosaic, or leave it at the minimum.</li>
<li>The user sets the background color of the mosaic.</li>
<li>The user sets the color of the text.</li>
<li>The app will then calculate the spacing of the text both horizontally and vertically.</li>
<li>An array of coordinates of each piece of each letter is created.</li>
<li>The app generates the image and give the option to download the image.</li>
</ol>

The app is hosted on GitHub pages, which you can view [here](https://ryanmontville.com/rubiksTextGeneration/).

## An example of all the letters, numbers, and special characters
<div>
	<img src="/images/letters.png" alt="Letters A - Z" title="Letters A - Z" style="width: 49%; display: inline-block;" />
	<img src="/images/numbers.png" alt="Numbers 0 - 9 and special characters" style="width: 49%; display: inline-block;" />
</div>

## Example combinations of colors
Here are some examples of how different colored text will look with different colored backgrounds. (Your Rubik's cube's colors might look different than the images below.)
<div>
	<img src="/images/red-combos.png" alt="An example of how different colors of text will look on a red background" title="An example of how differnt colors of text will look on a red background" style="width: 30%; display: inline-block;" />
	<img src="/images/orange-combos.png" alt="An example of how different colors of text will look on a orange background" title="An example of how differnt colors of text will look on a orange background" style="width: 30%; display: inline-block;" />
	<img src="/images/yellow-combos.png" alt="An example of how different colors of text will look on a yellow background" title="An example of how differnt colors of text will look on a yellow background" style="width: 30%; display: inline-block;" />
	<img src="/images/blue-combos.png" alt="An example of how different colors of text will look on a blue background" title="An example of how differnt colors of text will look on a blue background" style="width: 30%; display: inline-block;" />
	<img src="/images/green-combos.png" alt="An example of how different colors of text will look on a green background" title="An example of how differnt colors of text will look on a green background" style="width: 30%; display: inline-block;" />
	<img src="/images/white-combos.png" alt="An example of how different colors of text will look on a white background" title="An example of how differnt colors of text will look on a white background" style="width: 30%; display: inline-block;" />
</div>

## Examples of images generated with the program
<div>
	<img src="images/helloworld.png" alt="HELLO WORLD generated" title="HELLO WORLD generated" style="width: 48%; display: inline-block" />
	<img src="images/ryanmontville.png" alt="RYAN MONTVILLE generated" title="RYAN MONTVILLE generated" style="width: 48%; display: inline-block" />
</div>

