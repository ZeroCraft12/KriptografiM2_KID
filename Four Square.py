import os
import re

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 25 huruf, J digabung ke I


def make_keysquare(key: str) -> str:
    """Buat 25-char keysquare dari keyword (hapus duplikat, isi sisa alfabet)."""
    key = re.sub(r'[^A-Z]', '', key.upper()).replace('J', 'I')
    seen = []
    for ch in key + ALPHABET:
        if ch not in seen:
            seen.append(ch)
    return ''.join(seen)


def four_square_encipher(plaintext: str, key1: str, key2: str) -> str:
    pt = re.sub(r'[^A-Z]', '', plaintext.upper()).replace('J', 'I')
    if not pt:
        raise ValueError("Teks tidak mengandung huruf A-Z yang valid.")
    if len(pt) % 2 != 0:
        pt += 'X'

    ks1 = make_keysquare(key1)
    ks2 = make_keysquare(key2)
    result = []

    for i in range(0, len(pt), 2):
        r1, c1 = divmod(ALPHABET.index(pt[i]), 5)
        r2, c2 = divmod(ALPHABET.index(pt[i + 1]), 5)
        result.append(ks1[r1 * 5 + c2])
        result.append(ks2[r2 * 5 + c1])

    return ''.join(result)


def four_square_decipher(ciphertext: str, key1: str, key2: str) -> str:
    ct = re.sub(r'[^A-Z]', '', ciphertext.upper()).replace('J', 'I')
    if not ct:
        raise ValueError("Ciphertext tidak mengandung huruf A-Z yang valid.")
    if len(ct) % 2 != 0:
        raise ValueError("Panjang ciphertext harus genap.")

    ks1 = make_keysquare(key1)
    ks2 = make_keysquare(key2)
    result = []

    for i in range(0, len(ct), 2):
        r1, c1 = divmod(ks1.index(ct[i]), 5)
        r2, c2 = divmod(ks2.index(ct[i + 1]), 5)
        result.append(ALPHABET[r1 * 5 + c2])
        result.append(ALPHABET[r2 * 5 + c1])

    return ''.join(result)


def mode_manual(is_encrypt: bool):
    mode_name = "ENKRIPSI" if is_encrypt else "DEKRIPSI"
    input_label = "Plaintext" if is_encrypt else "Ciphertext"
    output_label = "Ciphertext" if is_encrypt else "Plaintext Hasil Dekripsi"

    print(f"\n--- MODE INPUT MANUAL ({mode_name}) ---")
    user_text = input(f"Masukkan {input_label} : ")
    key1 = input("Masukkan Key 1 : ")
    key2 = input("Masukkan Key 2 : ")

    try:
        fn = four_square_encipher if is_encrypt else four_square_decipher
        hasil = fn(user_text, key1, key2)
        print("-" * 40)
        print(f"Hasil {output_label}: {hasil}")
        print("-" * 40)
    except ValueError as e:
        print(f"[Error]: {e}")


def mode_file(is_encrypt: bool):
    mode_name = "ENKRIPSI" if is_encrypt else "DEKRIPSI"

    print(f"\n--- MODE BACA/TULIS FILE .TXT ({mode_name}) ---")
    input_path = input("Masukkan nama/path file input (.txt)  : ").strip()

    if not os.path.exists(input_path):
        print(f"[Error]: File '{input_path}' tidak ditemukan!")
        return

    key1 = input("Masukkan Key 1                         : ")
    key2 = input("Masukkan Key 2                         : ")
    output_path = input("Masukkan nama/path file output (.txt) : ").strip()

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        fn = four_square_encipher if is_encrypt else four_square_decipher
        hasil = fn(content, key1, key2)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(hasil)

        print("-" * 40)
        print(f"[Sukses]: Berhasil memproses file!")
        print(f"Hasil disimpan di: {os.path.abspath(output_path)}")
        print("-" * 40)
    except Exception as e:
        print(f"[Error]: Terjadi kesalahan saat memproses file: {e}")


def main():
    while True:
        print("\n=== FOUR SQUARE CIPHER ===")
        print("1. Enkripsi (Input Manual Terminal)")
        print("2. Dekripsi (Input Manual Terminal)")
        print("3. Enkripsi (Dari File .txt -> Simpan File .txt)")
        print("4. Dekripsi (Dari File .txt -> Simpan File .txt)")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == '1':
            mode_manual(is_encrypt=True)
        elif pilihan == '2':
            mode_manual(is_encrypt=False)
        elif pilihan == '3':
            mode_file(is_encrypt=True)
        elif pilihan == '4':
            mode_file(is_encrypt=False)
        elif pilihan == '5':
            print("\nTerima kasih!")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih angka 1 sampai 5.")


if __name__ == "__main__":
    # Self-check: verifikasi dengan contoh dari referensi
    ct = four_square_encipher("ATTACKATDAWN", "ZGPTFOIHMUWDRCNYKEQAXVSBL", "MFNBDCRHSAXYOGVITUEWLQZKP")
    assert ct == "TIYBFHTIZBSY", f"Encipher gagal: {ct}"
    pt = four_square_decipher("TIYBFHTIZBSY", "ZGPTFOIHMUWDRCNYKEQAXVSBL", "MFNBDCRHSAXYOGVITUEWLQZKP")
    assert pt == "ATTACKATDAWN", f"Decipher gagal: {pt}"
    print("Self-check OK.")
    main()
