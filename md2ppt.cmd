set root=%*

python D:\dev\headrepeater\headrepeater.py "%root%"

pandoc --reference-doc="E:\Downloads\lecture\ref.pptx" "%cd%\_%*" -o "E:\Downloads\lecture\%root:.md=%.pptx" --slide-level 2

del "%cd%\_%root%"

start "C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE" "E:\Downloads\lecture\%root:.md=%.pptx"

exit