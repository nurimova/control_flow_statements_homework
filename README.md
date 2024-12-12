## Xush kelibsiz  
### Oqim boshqaruvi operatorlari  

Uyga vazifalar va test topshiriqlarini avtomatlashtirilgan baholash  
- Ushbu repozitoriyani fork qiling  
- Vazifani yeching  
- To'g'ri xabar bilan commit qiling  
- To'g'ri xabar bilan commit qiling  

### Vazifalar  
#### if01  

  Agar son musbat bo'lsa, uni 1 ga oshiring, aks holda o'zgarmasdan qoldiring.  

**1-misol:**  

```Python  
Kiritish: a=1  
Natija: 2  
```  

**2-misol:**  

```Python  
Kiritish: a=-5  
Natija: -5  
```  

**Cheklovlar:**  
- -10<sup>18</sup> ≤ num ≤ 10<sup>18</sup>  

---

#### if02  

  Agar son musbat bo'lsa, uni 1 ga oshiring, aks holda uni 2 ga kamaytiring.  

**1-misol:**  

```Python  
Kiritish: a=5  
Natija: 6  
```  

**2-misol:**  

```Python  
Kiritish: a=-1  
Natija: -3  
```  

**Cheklovlar:**  
- -10<sup>18</sup> ≤ num ≤ 10<sup>18</sup>  

---

#### if03  

  Agar son musbat bo'lsa, uni 1 ga oshiring, aks holda uni 2 ga kamaytiring. Agar u 0 bo'lsa, 10 qiymatini bering.  

**1-misol:**  

```Python  
Kiritish: a=-9  
Natija: -11  
```  

**2-misol:**  

```Python  
Kiritish: a=3  
Natija: 4  
```  

**Cheklovlar:**  
- -10<sup>18</sup> ≤ num ≤ 10<sup>18</sup>  

---

#### if04  

  Berilgan sonlarda nechta musbat son borligini toping.  

**1-misol:**  

```Python  
Kiritish: a=-2 b=4 c=1  
Natija: 2  
```  

**2-misol:**  

```Python  
Kiritish: a=3 b=-3 c=-6  
Natija: 1  
```  

**Cheklovlar:**  
- -10<sup>18</sup> ≤ num ≤ 10<sup>18</sup>  

---

#### if05  

  Berilgan sonlarda nechta manfiy son borligini toping.  

**1-misol:**  

```Python  
Kiritish: a=-2 b=4 c=1  
Natija: 1  
```  

**2-misol:**  

```Python  
Kiritish: a=3 b=-3 c=-6  
Natija: 2  
```  

**Cheklovlar:**  
- -10<sup>18</sup> ≤ num ≤ 10<sup>18</sup>  

---

#### if06  

  Berilgan sonlarda nechta musbat va nechta manfiy son borligini toping.  

**1-misol:**  

```Python  
Kiritish: a=-2 b=4 c=1  
Natija: "ko'p musbat sonlar bor"  
```  

**2-misol:**  

```Python  
Kiritish: a=3 b=-3 c=-6  
Natija: "ko'p manfiy sonlar bor"  
```  

**Cheklovlar:**  
- -10<sup>18</sup> ≤ num ≤ 10<sup>18</sup>  

---

#### if07  

  Berilgan a butun soni uchun quyidagi shartlarni tekshiring:  
    "musbat toq son",  
    "musbat juft son",  
    "manfiy toq son",  
    "manfiy juft son",  
    "son nolga teng"  

**1-misol:**  

```Python  
Kiritish: a=57  
Natija: "musbat toq son"  
```  

**2-misol:**  

```Python  
Kiritish: a=-24  
Natija: "manfiy juft son"  
```  

**Cheklovlar:**  
- -10<sup>9</sup> ≤ num ≤ 10<sup>9</sup>  

---

#### if08  

  Berilgan butun son a uchun quyidagi shartlarni tekshiring:  
    "ikki xonali toq son",  
    "ikki xonali juft son",  
    "uch xonali toq son",  
    "uch xonali juft son"  

**1-misol:**  

```Python  
Kiritish: a=57  
Natija: "ikki xonali toq son"  
```  

**2-misol:**  

```Python  
Kiritish: a=-242  
Natija: "uch xonali juft son"  
```  

**Cheklovlar:**  
- -10<sup>3</sup> < num < 10<sup>3</sup>  

---

#### if09  

  Ikki xonali butun son berilgan.  
  Sonning raqamlarini o'rnini almashtiring. Agar hosil bo'lgan son eski sondan kichik yoki unga teng bo'lsa, True, aks holda False qaytaring.  

**1-misol:**  

```Python  
Kiritish: a=57  
Natija: False  
```  

**2-misol:**  

```Python  
Kiritish: a=21  
Natija: True  
```  

**Cheklovlar:**  
- -10<sup>3</sup> < num < 10<sup>3</sup>  

---

#### if10  

  Sizga berilgan harorat sharoitlariga ko'ra xabarni ko'rsating (Selsiusda):  
  - Harorat <0: "Muzlab qoldi"  
  - Harorat 1-10: "Juda sovuq"  
  - Harorat 11-20: "Sovuq"  
  - Harorat 21-30: "Normal"  
  - Harorat 31-40: "Issiq"  
  - Harorat >40: "Juda issiq"  

**1-misol:**  

```Python  
Kiritish: a=21  
Natija: "Normal"  
```  

**2-misol:**  

```Python  
Kiritish: a=-4  
Natija: "Muzlab qoldi"  
```  

**Cheklovlar:**  
- -10<sup>3</sup> < num < 10<sup>3</sup>  

---

### Ogohlantirish  
- Boshqalarning yechimini yoki biror yechimni nusxa ko'chirmang  
- Kommentlarni o'chirmang  
