all:
	pip install -e .
	pip uninstall bifacial-radiance
	pip install bifacial-radiance

folder:
	rayoptix setup-folders --path "../../../bifacial_radiance/TEMP/Test_real" --namefolder "Test_real"

ground:
	rayoptix set-ground --namefolder "Test_real" --material "0.2"

weather:
	rayoptix set-weather --namefolder "Test_real" --pathcsv "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/test_weather.csv"

timestamp:
	rayoptix get-timestamp --namefolder "Test_real" --time "2001-06-17 13:0:0 +1"

genDayLit:
	rayoptix gen-daylit --namefolder "Test_real" --timeindex 2146

makeModule:
	rayoptix make-module --namefolder "Test_real" --pathcsv_makemodule "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeModule_params.csv" 

addCellModule:
	rayoptix add-cell-module --namefolder "Test_real" --pathcsv "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addCellModule_params.csv"

makeModule2:
	rayoptix make-module --namefolder "Test_real" --pathcsv_makemodule "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeModule_params.csv" --pathcsv_cellmodule "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addCellModule_params.csv"

makeScene:
	rayoptix make-scene --namefolder "Test_real" --pathcsv "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeScene_params.csv"

makeOct:
	rayoptix make-oct --namefolder "Test_real"

makeCustomObject:
	rayoptix make-customobject --namefolder "Test_real" --pathcsv "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeObject_params.csv"

appendtoScene-1:
	rayoptix append-to-scene --namefolder "Test_real" --radfile True --pathobject "C:/Users/cambr/bifacial_radiance/TEMP/Test_real/objects/Post1.rad" --text "!xform -rz 0"

appendtoScene-2:
	rayoptix append-to-scene --namefolder "Test_real" --radfile True --pathobject "C:/Users/cambr/bifacial_radiance/TEMP/Test_real/objects/Post2.rad" --text "!xform -rz 0"

appendtoScene-3:
	rayoptix append-to-scene --namefolder "Test_real" --radfile True --pathobject "C:/Users/cambr/bifacial_radiance/TEMP/Test_real/objects/Pile.rad" --text "!xform -rz 0"

makeAnalysisObj:
	rayoptix make-analysis-obj --namefolder "Test_real" --pathfile "C:/Users/cambr/bifacial_radiance/TEMP/Test_real/Test_real.oct" --name "Test_real"

setModuleAnalysis:
	rayoptix set-module-analysis --namefolder "Test_real" --pathcsv "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/moduleAnalysis_params.csv"

setFrontScan:
	rayoptix set-front-scan --namefolder "Test_real" --pathcsv "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/back-frontscan_params.csv"

makeAnalysis:
	rayoptix make-analysis --namefolder "Test_real" --octfile "C:/Users/cambr/bifacial_radiance/TEMP/Test_real/Test_real.oct" --name "Test_real_groundscan" --frontscan True --backscan True

a:
	rayoptix make-analysis-obj --help

h: 
	rayoptix --help