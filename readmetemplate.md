### AdventofCode
Solutions to the Advent of Code puzzles with some incredibly overkill generative scripts. It's the holidays, have fun with it.

https://adventofcode.com

While in root directory run the following command to automatically:
1. Create a new directory with todays day nested under the current year
2. Create an input.txt file to quickly copy/paste the advent data
3. Create 2 solution.py files (1 for each part) with starter code to read in the txt file and start smashing away at a solution

If you know your a baller and going to complete EVERY challenge you can add the '--all' flag to create a new directory for every day of te month instead of just todays date.

Finally, if you want to overwrite a directory add '--overwrite' and all files will be replaced.

Non baller way of creating new directory

``
python create_new_day.py
``

Baller way of creating a directory for every day of month

``
python create_new_day.py --all
``

Now it's time to update the readme with all your solutions. Because if displayed code isnt pretty than I don't know what is.
Anyways, doing this is easy, define a 'readmetemplate.md' in the root folder and run the following script:

``python update_readme_stats.py``

This will automatically run your solutions, time it and display each solution for each day in the readme.

Bonkers.

<hr>

