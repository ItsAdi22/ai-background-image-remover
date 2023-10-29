from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Select image file')
outputPath = easygui.filesavebox(title='Save file to...')

input_image = Image.open(inputPath)
output_image = remove(input_image)

output_image.save(outputPath)
