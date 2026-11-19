# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread 
from skimage.color import rgb2gray, rgb2hsv
from skimage.util import img_as_float
from skimage.segmentation import watershed
from scipy.signal import medfilt2d,convolve2d


# Ukol 1: Základy segmentace - prahování
# =============================================================================
# 1. Načtěte obraz 'football.png' a zobrazte si jednotlivé barevné složky tohto obrazu zvlášť spolu s jejich histogramy.
# 2. Zvolte jednu ze složek RGB jako základ pro segmentaci.
# 3. Na základě histogramů vhodně zvolte práh pro prahování obrazu
# 4. Pomocí zvoleného prahu vysegmentujte obraz (čáry a branky: hodnota 1, zbytek: hodnota 0)
# =============================================================================
plt.close('all')

img_football = ...
football_segmentation_output = ...

img_football_R = ...
img_football_G = ...
img_football_B = ...

plt.figure()
plt.subplot(2,3,1)
plt.imshow(img_football_R, cmap = 'gray')
plt.title('R')
plt.subplot(2,3,4)
plt.hist(img_football_R.ravel(), bins= 128)
plt.xlabel('Intensity [-]')
plt.ylabel('Pixel count [-]')
plt.subplot(2,3,2)
plt.imshow(img_football_G, cmap = 'gray')
plt.title('G')
plt.subplot(2,3,5)
plt.hist(img_football_G.ravel(), bins= 128)
plt.xlabel('Intensity [-]')
plt.ylabel('Pixel count [-]')
plt.subplot(2,3,3)
plt.imshow(img_football_B, cmap = 'gray')
plt.title('B')
plt.subplot(2,3,6)
plt.hist(img_football_B.ravel(), bins= 128)
plt.xlabel('Intensity [-]')
plt.ylabel('Pixel count [-]')
plt.show()

threshold = ...
football_segmentation_output = ...

plt.figure()
plt.subplot(1,2,1)
plt.imshow(img_football[:,:,:3])
plt.title('Originální obraz')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(football_segmentation_output, cmap = 'gray')
plt.title('Výstupní segmentace')
plt.axis('off')
plt.show()

# Ukol 2: Dvouprahové segmentace z HSV prostoru
# =============================================================================
# 1. Načtěte obraz 'Boulder_cropped.png' (pouze hodnoty RGB), zobrazte histogramy jednotlivých RGB složek.
# Otázka k zamyšlení: Je možné na základě RGB obraz segmentovat přímo?
# 2. Převeďte obraz do HSV prostoru, zobrazte jednotlivé HSV složky a jejich histogramy.
# 3. Na základě zobrazených HSV dat vyberte kanál, který specifikuje konkrétní barvy, a vynásobte jeho hodnoty 360.
# 4. Zobrazte původní obraz, vybraný HSV kanál, colormapu kanálu a histogram HSV kanálu s horizontální orientací
# 5. Na základě histogramu vybraného HSV kanálu stanovte prahy pro vysegmentování úchytů zelené barvy
# 6. Na zákaldě zvolených prahů vysegmentujte daný kanál
# 7. Vytvořte nový obraz, ve kterém budou mít pouze zelené úchyty svou původní barvu, zbytek bude černý.
# 8. Zobrazte původní barevný obraz, výslednou segmentaci a nový obraz (černé pozadí, zelené úchyty)
# Otázky k zamyšlení: Jak bychom vysegmentovali úchyty modré barvy?
# =============================================================================

plt.close('all')
img_boulder = ...

img_boulder_R = ...
img_boulder_G = ...
img_boulder_B = ...

plt.figure()
plt.subplot(2,3,1)
plt.imshow(img_boulder_R, cmap = 'gray')
plt.title('R')
plt.subplot(2,3,4)
plt.hist(img_boulder_R.ravel(), bins= 128)
plt.xlabel('Intensity [-]')
plt.ylabel('Pixel count [-]')
plt.subplot(2,3,2)
plt.imshow(img_boulder_G, cmap = 'gray')
plt.title('G')
plt.subplot(2,3,5)
plt.hist(img_boulder_G.ravel(), bins= 128)
plt.xlabel('Intensity [-]')
plt.ylabel('Pixel count [-]')
plt.subplot(2,3,3)
plt.imshow(img_boulder_B, cmap = 'gray')
plt.title('B')
plt.subplot(2,3,6)
plt.hist(img_boulder_B.ravel(), bins= 128)
plt.xlabel('Intensity [-]')
plt.ylabel('Pixel count [-]')
plt.show()

img_hsv = ...
selected_channel = ...
multiplied_selected_channel = ...


plt.figure()
plt.subplot(2,3,1)
plt.imshow(img_hsv[:,:,0], cmap = 'gray')
plt.title('H')
plt.subplot(2,3,4)
plt.hist(img_hsv[:,:,0].ravel(), bins= 128)
plt.xlabel('Intensity [-]')
plt.ylabel('Pixel count [-]')
plt.subplot(2,3,2)
plt.imshow(img_hsv[:,:,1], cmap = 'gray')
plt.title('S')
plt.subplot(2,3,5)
plt.hist(img_hsv[:,:,1].ravel(), bins= 128)
plt.xlabel('Intensity [-]')
plt.ylabel('Pixel count [-]')
plt.subplot(2,3,3)
plt.imshow(img_hsv[:,:,2], cmap = 'gray')
plt.title('V')
plt.subplot(2,3,6)
plt.hist(img_hsv[:,:,2].ravel(), bins= 128)
plt.xlabel('Intensity [-]')
plt.ylabel('Pixel count [-]')
plt.show()


plt.figure()
plt.subplot(1,3,1)
plt.imshow(img_boulder)
plt.title('Původní obraz')
plt.subplot(1,3,2)
plt.imshow(multiplied_selected_channel, cmap = 'hsv')
plt.colorbar()
plt.title('Vybraný kanál')
plt.subplot(1,3,3)
plt.title('Histogram vybraného kanálu')
plt.hist(multiplied_selected_channel.ravel(), bins = 256, orientation = 'horizontal')
plt.ylim((0,359))
plt.show()

green_grips_threshold = ...

green_grips_mask = ...

segmented_grips = ...

plt.figure()
plt.subplot(1,3,1)
plt.imshow(img_boulder)
plt.title('Původní obraz')
plt.subplot(1,3,2)
plt.imshow(green_grips_mask, cmap = 'gray')
plt.title('Segmentační maska')
plt.subplot(1,3,3)
plt.title('Vysegmentované úchyty')
plt.imshow(segmented_grips)
plt.show()


#%% Ukol 3
# =============================================================================
# Načtěte obraz krtek.jpg, převeďte jej na šedotónový, do rozsahu 0-1 a zobrazte.
# Obraz filtrujte mediánovým filtrem.
# Získejte gradientní obraz za pomoci Sobelovy masky v obou směrech.
# Snižte kvantovací úroveň gradientního obrazu na 3 bity.
# Aplikujte segmentační metodu rozvodí na tuto parametrickou mapu.
# Výsledky zobrazte.
# =============================================================================
img = ...
img_filtered = ...

plt.figure()
plt.subplot(1,2,1)
plt.imshow(img, cmap = 'gray')
plt.title('Originální obraz')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(img_filtered, cmap = 'gray')
plt.title('Filtrovany obraz')
plt.axis('off')
plt.show()

sobel_mask_x = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobel_mask_y = sobel_mask_x.T

gradient_x=...
gradient_y=...
gradient_img =...

plt.figure()
plt.subplot(2,1,1)
plt.imshow(gradient_img, cmap = 'gray')
plt.title('Gradientni obraz')
plt.axis('off')
plt.subplot(2,1,2)
plt.hist(gradient_img.ravel(),bins=128)
plt.title('Histogram gradientniho obrazu')
plt.xlabel('Jas [-]')
plt.ylabel('Cetnost [-]')
plt.show()

n_levels = 2**3
delta_L = 1 / (n_levels - 1)
img_kvant = ... * ...


img_watershed= ...

plt.figure()
plt.subplot(1,2,1)
plt.imshow(img, cmap = 'gray')
plt.title("Original")
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(img_watershed,cmap='jet')
plt.title("Výstup Watershed")
plt.axis('off')
plt.show()
