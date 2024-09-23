all:
	pip uninstall bifacial-radiance
	pip install bifacial-radiance
	pip install -e .
	rayoptix --help

s:
	rayoptix setup-folders --path "../../TEMP/T1" --name "T1" --use_absolute

g:
	rayoptix ground --name "t1"

h: 
	rayoptix --help