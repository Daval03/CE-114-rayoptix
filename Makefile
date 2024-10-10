all:
	pip install -e .
	pip uninstall bifacial-radiance
	pip install bifacial-radiance

folder:
	rayoptix setup-folders --path "../../../bifacial_radiance/TEMP/Test_97" --namefolder "Test_97"

weather:
	rayoptix set-weather --namefolder "Test_97" --pathcsv "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/test_weather.csv"

g:
	rayoptix ground --name "t1"

h: 
	rayoptix --help