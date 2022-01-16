# kalturaHacks
Scripts to make using Kaltura less mind-bogglingly painful

## List of scripts
<table>
<tr><th>Script</th><th>Description</th><th>Data files used</th><th>Other requirements</th><th>Notes</th></tr>
<tr><td>kalturaCaptionStripper.py</td><td>Formats downloaded Kaltura caption files for creating lecture transcripts</td><td>One or more *.srt files downloaded from Kaltura</td><td></td><td>Future iterations should be able to re-upload the edited transcripts</td></tr>
</table>

## Setting up
The code for this project requires the following list of packages in order to run.
<ul>
<li>os</li>
<li>pandas</li>
<li>sys</li>
<li>tkinter</li>
</ul>

To install using conda, execute the command:

	conda install os
	conda install pandas
	
...and so on

To install using pip, execute the command:

	pip install os
	pip install pandas
	
...and so on

## Running
Once python and the packages listed above have been installed, to run a script from command line, execute the command:

	python kalturaCaptionStripper.py
	
...and so on
