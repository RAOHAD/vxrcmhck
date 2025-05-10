import os
import shutil

def take_photo():
    # ছবির নাম
    photo_name = "captured_photo.jpg"
    
    # রিয়ার ক্যামেরা ব্যবহার (0 = রিয়ার, 1 = ফ্রন্ট)
    camera_id = 0

    # ক্যামেরা দিয়ে ছবি তোলা
    print("Opening camera...")
    os.system(f"termux-camera-photo -c {camera_id} {photo_name}")

    # গ্যালারির মতো ফোল্ডারে কপি করার পথ
    gallery_path = "/sdcard/DCIM/Camera/"  # অনেক ফোনে এটাই ডিফল্ট গ্যালারি ফোল্ডার

    # যদি ফোল্ডারটা থাকে তবে কপি করো
    if os.path.exists(gallery_path):
        shutil.copy(photo_name, gallery_path)
        print(f"\n✅ Photo saved to gallery: {gallery_path}{photo_name}")
    else:
        print(f"\n⚠️ Gallery folder not found. Photo saved in: {photo_name}")

if __name__ == "__main__":
    take_photo()