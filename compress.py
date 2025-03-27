
import numpy as np
from PIL import Image
from scipy.fftpack import dct, idct

# ========== FUNCIONES DE RLE ==========
def rle_encode_line(line):
    encoded = []
    count = 1
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            count += 1
        else:
            encoded.append((count, line[i-1]))
            count = 1
    encoded.append((count, line[-1]))
    return encoded

def rle_decode_line(encoded):
    return [val for count, val in encoded for _ in range(count)]

def rle_encode_image(img):
    return [rle_encode_line(row) for row in img]

def rle_decode_image(encoded_img):
    return np.array([rle_decode_line(row) for row in encoded_img], dtype=np.uint8)

# ========== FUNCIONES DE DCT ==========
def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

def dct_compress(img, keep=4):
    h, w = img.shape
    compressed = np.zeros((h, w), dtype=np.float32)
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            block = img[i:i+8, j:j+8]
            dct_block = dct2(block)
            mask = np.zeros_like(dct_block)
            mask[:keep, :keep] = 1
            dct_block *= mask
            compressed[i:i+8, j:j+8] = idct2(dct_block)
    return np.clip(compressed, 0, 255).astype(np.uint8)

# ========== CARGAR IMAGEN DE ENTRADA ==========
try:
    img = Image.open("example.jpeg").convert("L")  # Convertir a escala de grises
    img = img.resize((128, 128))  # Redimensionar para pruebas
except Exception as e:
    print("❌ Error al cargar la imagen: example.jpeg")
    print(e)
    exit(1)

img_np = np.array(img)

# ========== PROCESAR ==========
rle_encoded = rle_encode_image(img_np)
rle_decoded = rle_decode_image(rle_encoded)

dct_result = dct_compress(img_np, keep=4)

# ========== GUARDAR RESULTADOS ==========
Image.fromarray(img_np).save("entrada_grayscale.png")
Image.fromarray(rle_decoded).save("rle_result.png")
Image.fromarray(dct_result).save("dct_result.png")

# ========== MOSTRAR TAMAÑOS ==========
original_size = img_np.size
rle_size = sum(len(row) for row in rle_encoded) * 2

print("✅ Imágenes guardadas:")
print("- entrada_grayscale.png")
print("- rle_result.png")
print("- dct_result.png")
print(f"Tamaño original: {original_size} bytes (aprox)")
print(f"Tamaño estimado RLE: {rle_size} bytes (cada par cuenta como 2)")
