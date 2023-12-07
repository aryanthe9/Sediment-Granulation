import subprocess

def open_service_process():
    subprocess.run(['python', r'C:\sandsresult\DANE BANDI SEDIMENT.py'])

def export_to_pdf():
    subprocess.run(['python', r'C:\sandsresult\maing.py'])

def check_results():
    subprocess.run(['explorer', 'C:\sandsresult']) # For Windows OS, opens directory in File Explorer

def display_menu():
    print("\n╔════════════════════════════════════╗")
    print("║      Welcome to Sands Result       ║")
    print("╠════════════════════════════════════╣")
    print("║ 1. Open Service/PROCCES            ║")
    print("║ 2. Export files to PDF             ║")
    print("║ 3. Check Results                   ║")
    print("║ 4. Exit                            ║")
    print("║ 5. Credits                         ║")
    print("║ 6. Download Files                  ║")
    print("║ 7. Install Guide                   ║")
    print("╚════════════════════════════════════╝")

def show_credits():
    print("\n╔════════════════════════════╗")
    print("║       Credits:             ║")
    print("║     Aryan Salmannezhad     ║")
    print("╚════════════════════════════╝")

def download_files():
    print("\nDownload files from:")
    print("https://drive.google.com/drive/folders/1bGVKEI_ni6YfxvXkMXA-6shSRDyXdb8u?usp=drive_link")

def install_gauid_instructions():
    print("\nTo install Guide:")
    print("1. Download the Files from menu 6")
    print("2. Move sandsresult to drive C")
    print("3. Run files from SedimentMENU or One by One (every files in folder)")

def main_menu():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            open_service_process()
        elif choice == '2':
            export_to_pdf()
        elif choice == '3':
            check_results()
        elif choice == '4':
            print("\nExiting the program.")
            break
        elif choice == '5':
            show_credits()
        elif choice == '6':
            download_files()
        elif choice == '7':
            install_gauid_instructions()
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main_menu()
