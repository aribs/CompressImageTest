
# 📊 Comparativa de Compresión de Imágenes: RLE vs DCT

Este proyecto demuestra y compara dos técnicas de compresión de imágenes en escala de grises usando Python:

- **RLE (Run-Length Encoding)**: compresión **sin pérdida**, útil para patrones repetitivos.
- **DCT (Discrete Cosine Transform)**: compresión **con pérdida**, ideal para imágenes fotográficas.

---

## ⚙️ Cómo funciona cada algoritmo

### 🧩 RLE - Run-Length Encoding

**Tipo**: Sin pérdida  
**Uso**: Imágenes simples, íconos, gráficos con pocos colores.

#### 🔍 Funcionamiento:
- Recorre cada fila de píxeles.
- Agrupa secuencias consecutivas con el mismo valor.
- Cada grupo se codifica como `(número de repeticiones, valor)`.

#### 🧠 Ejemplo:
```plaintext
[1, 1, 1, 2, 2] → [(3,1), (2,2)]
```

#### 🛠 En el script:
- Se codifica cada fila con `rle_encode_line()`.
- Se guarda como `rle_result.png`.
- La imagen reconstruida es **idéntica** a la original.

---

### 🎵 DCT - Discrete Cosine Transform

**Tipo**: Con pérdida  
**Uso**: Fotografías reales (como JPEG).

#### 🔍 Funcionamiento:
- Divide la imagen en bloques 8x8.
- Aplica la transformada DCT a cada bloque (convierte píxeles en frecuencias).
- Se conservan solo los coeficientes más importantes (baja frecuencia).
- Se reconstruye la imagen con IDCT.

#### 🛠 En el script:
- Usamos `dct2()` e `idct2()` para aplicar DCT/IDCT.
- Se puede ajustar la cantidad de datos retenidos con `keep=4`.
- Se guarda como `dct_result.png`.
- Tiene pérdida de calidad, pero es mucho más compacta visualmente.

---

## 🧪 Uso del Script

### 📁 Archivo: `rle_vs_dct_with_image_input.py`

### 📸 Requisitos:
- Imagen de entrada llamada `example.jpeg` (debe estar en el mismo directorio).
- Python 3 y las siguientes dependencias:

```bash
pip install pillow numpy scipy
```

### ▶️ Ejecución:
```bash
python rle_vs_dct_with_image_input.py
```

### 📥 Entrada:
- `example.jpeg` (cualquier imagen, preferentemente cuadrada o se redimensionará a 128x128)

### 📤 Salida:
- `entrada_grayscale.png`: imagen convertida a escala de grises
- `rle_result.png`: resultado de RLE (idéntico visualmente)
- `dct_result.png`: resultado de DCT (con pérdida)
- Tamaños estimados impresos por consola

---

## 📌 Ejemplo de salida por consola:
```plaintext
✅ Imágenes guardadas:
- entrada_grayscale.png
- rle_result.png
- dct_result.png
Tamaño original: 16384 bytes (aprox)
Tamaño estimado RLE: 18942 bytes (cada par cuenta como 2)
```

---

## 🧠 Conclusión

| Método | Tipo        | Calidad    | Mejor en...                  |
|--------|-------------|------------|------------------------------|
| RLE    | Sin pérdida | Perfecta   | Gráficos simples o íconos    |
| DCT    | Con pérdida | Alta/Media | Fotografías reales, compresión JPEG |


---
