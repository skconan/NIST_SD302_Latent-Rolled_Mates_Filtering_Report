# NIST SD302: Data Exploration and Cleaning

## Table of content

- 


## Reading .lffs

- Refrence
    
    - [Data Format for the Interchange of Fingerprint, Facial & Other Biometric Information ANSI/NIST-ITL 1-2011 NIST Special Publication 500-290 Edition 3](https://www.nist.gov/publications/data-format-interchange-fingerprint-facial-other-biometric-information-ansinist-itl-1-1)

    - [Special Publication (NIST SP) - 500-290e3](https://doi.org/10.6028/NIST.SP.500-290e3)

- Field Number

    - 13.999 - LATENT FRICTION RIDGE IMAGE (End with "IEND")

## Filtering the rolled and latent mates

- Reference

    - [SYNTHETIC LATENT FINGERPRINT GENERATOR](https://arxiv.org/abs/2208.13811)

- The finger position annotation in the SD302h subset.

- Use only first impression

- 

ไม่ยึดชื่อไฟล์ แต่เอาชื่อไฟล์ไปเช็ค fgp จาก csv เลยปรากฏว่า อันที่ไฟล์มี X บอกเป็น unknown ใน csv มี fgp บอก เลยเลือกมาแต่ยังเกินอยู่ เลยเลือกเฉพาะ impression แรก ก้ได้พอดีเลยแล้วก็อ่านรูปจาก lffs เอาเลยก็เลยสอดคล้องกับ paper ที่ให้มี่เค้าดูแต่ 302h
