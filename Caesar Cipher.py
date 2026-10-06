import os

def caesar_transform(text: str, shift: int, mode: str = 'encrypt') -> str:
    """
    Fungsi Caesar Cipher untuk Enkripsi dan Dekripsi.
    Formula: C = (P + K) mod 26 (Enkripsi)
             P = (C - K) mod 26 (Dekripsi)
    """
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            transformed = chr((ord(char) - start + shift) % 26 + start)
            result.append(transformed)
        else:
            result.append(char)

    return "".join(result)


def mode_manual(is_encrypt: bool):
    """Mode input manual melalui terminal"""
    mode_name = "ENKRIPSI" if is_encrypt else "DEKRIPSI"
    input_label = "Plaintext" if is_encrypt else "Ciphertext"
    output_label = "Ciphertext" if is_encrypt else "Plaintext Hasil Dekripsi"

    print(f"\n--- MODE INPUT MANUAL ({mode_name}) ---")
    user_text = input(f"Masukkan {input_label} : ")
    try:
        user_key = int(input("Masukkan Key (Shift 0-25) : "))
    except ValueError:
        print("[Error]: Key harus berupa angka bulat!")
        return

    mode = 'encrypt' if is_encrypt else 'decrypt'
    hasil = caesar_transform(user_text, user_key, mode)
    print("-" * 40)
    print(f"Hasil {output_label}: {hasil}")
    print("-" * 40)


def mode_file(is_encrypt: bool):
    """Mode pemrosesan file .txt (input .txt -> output .txt)"""
    mode_name = "ENKRIPSI" if is_encrypt else "DEKRIPSI"

    print(f"\n--- MODE BACA/TULIS FILE .TXT ({mode_name}) ---")
    input_path = input("Masukkan nama/path file input (.txt)  : ").strip()

    if not os.path.exists(input_path):
        print(f"[Error]: File '{input_path}' tidak ditemukan!")
        return

    try:
        user_key = int(input("Masukkan Key (Shift 0-25)            : "))
    except ValueError:
        print("[Error]: Key harus berupa angka bulat!")
        return

    output_path = input("Masukkan nama/path file output (.txt) : ").strip()

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        mode = 'encrypt' if is_encrypt else 'decrypt'
        hasil = caesar_transform(content, user_key, mode)

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
        print("\n=== CAESAR CIPHER ===")
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
