<h1>iTunesUnduplicator</h1>
<h2>Python script to remove duplicate iTunes files.</h2>

<h3>TO RUN THIS SCRIPT</h3>
<ol>
<li>Copy-paste into your iTunes directory.</li>
<li>Open Terminal and navigate to your iTunes directory.</li>
<li>Run via Terminal: python iTunesUnduplicator.py</li>
</ol>

<h3>INSTRUCTIONS FOR USE</h3>
<h4>Trust Mode</h4>
<p>When your run iTunesUnduplicator.py you will be presented with the option to turn Trust Mode on or off.</p>
<ul>
<li><b>1 = Trust Mode ON</b>: The script will automatically check every folder for duplicate files and move duplicates to the Trash. To cancel at any time, enter CTRL-C.</li>
<li><b>2 = Trust Mode OFF</b>: Each time the script encounters a possible duplicate, it will present you with two files: File 1 (likely duplicate) and File 2 (likely original). You are asked to take one of the following actions via a prompt:
<ul>
<li><b>1 = Delete File 1</b>: Deletes the most likely duplicate.</li>
<li><b>2 = Delete File 2</b>: Deletes what iTunesUnduplicator.py though was the original.</li>
<li><b>3 = Skip</b>: Neither file will be deleted. You may or may not be asked about this comparison again.</li>
<li><b>4 = Open In Finder</b>: The enclosing folder of these files will be opened in Finder. The script will continue but you will be asked about this comparison again.</li>
<li><b>5 = Quit</b>: iTunesUnduplicator.py stops and no further files are reviewed.</li>
</ul>
</li>
</ul>

<h3>AFTERWARDS</h3>
<p>Open iTunes and remove dead tracks via the instructions on the following website:
http://paulmayne.org/blog/2007/11/how-to-remove-broken-or-dead-tracks-from-itunes/</p>

<h3>HOW IT WORKS</h3>
<p>iTunesUnduplicator determines two files to be identical if they meet the following criteria:
<ul>
<li>Both files are exactly the <strong>same size</strong> (in terms of MB).</li>
<li>Both files have the <strong>same file extension</strong>.</li>
<li>Both files share the same <strong>root file name</strong>.</li>
</ul>
E.g., The files (<b>1-01 My Song Name 1.m4a</b>), (<b>01 My Song Name 1.m4a</b>), (<b>1-01 My Song Name.m4a</b>), and (<b>01 My Song Name.m4a</b>) all share the same root file name (<b>01 My Song Name</b>).
</p>
<p>iTunesUnduplicator.py uses the following rules when deciding which file is the likely duplicate:
<ul>
<li>No suffix is better than a suffix: e.g., (<b>1-01 My Song Name.m4a</b>) is better than (<b>1-01 My Song Name 1.m4a</b>).</li>
<li>A lower suffix is better than a higher suffix: e.g., (<b>1-01 My Song Name 1.m4a</b>) is better than (<b>1-01 My Song Name 2.m4a</b>).</li>
<li>A CD listing is better than no CD listing: e.g., (<b>1-01 My Song Name 1.m4a</b>) is better than (<b>01 My Song Name 1.m4a</b>).</li>
<li>Not having a suffix takes priority over having a CD listing: e.g., (<b>01 My Song Name.m4a</b>) is better than (<b>1-01 My Song Name 1.m4a</b>)</li>
</ul>
</p>
