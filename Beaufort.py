import os
import re

def beaufort_transform(text: str, key: str) -> str:
    """
    Fungsi inti Beaufort Cipher (Enkripsi & Dekripsi simetris):
    C = (Key - Text) mod 26
    """
    text_clean = re.sub(r'[^A-Z]', '', text.upper())
    key_clean = re.sub(r'[^A-Z]', '', key.upper())

    if not text_clean:
        raise ValueError("Teks tidak mengandung huruf A-Z yang valid.")
    if not key_clean:
        raise ValueError("Kata kunci (key) tidak mengandung huruf A-Z yang valid.")

    result = []
    key_len = len(key_clean)

    for i, char in enumerate(text_clean):
        p_val = ord(char) - ord('A')
        k_val = ord(key_clean[i % key_len]) - ord('A')
        c_val = (k_val - p_val) % 26
        result.append(chr(c_val + ord('A')))

    return "".join(result)


def mode_manual(is_encrypt: bool):
    """Mode input manual melalui terminal"""
    mode_name = "ENKRIPSI" if is_encrypt else "DEKRIPSI"
    input_label = "Plaintext" if is_encrypt else "Ciphertext"
    output_label = "Ciphertext" if is_encrypt else "Plaintext Hasil Dekripsi"

    print(f"\n--- MODE INPUT MANUAL ({mode_name}) ---")
    user_text = input(f"Masukkan {input_label} : ")
    user_key = input("Masukkan Keyword (Key) : ")

    try:
        hasil = beaufort_transform(user_text, user_key)
        print("-" * 40)
        print(f"Hasil {output_label}: {hasil}")
        print("-" * 40)
    except ValueError as e:
        print(f"[Error]: {e}")


def mode_file(is_encrypt: bool):
    """Mode pemrosesan file .txt (input .txt -> output .txt)"""
    mode_name = "ENKRIPSI" if is_encrypt else "DEKRIPSI"

    print(f"\n--- MODE BACA/TULIS FILE .TXT ({mode_name}) ---")
    input_path = input("Masukkan nama/path file input (.txt)  : ").strip()

    if not os.path.exists(input_path):
        print(f"[Error]: File '{input_path}' tidak ditemukan!")
        return

    user_key = input("Masukkan Keyword (Key)                  : ")
    output_path = input("Masukkan nama/path file output (.txt) : ").strip()

    try:
        # Baca konten file input
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Proses enkripsi/dekripsi
        hasil = beaufort_transform(content, user_key)

        # Tulis hasil ke file output
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
    main()