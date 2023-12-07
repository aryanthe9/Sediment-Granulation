

def print_anchor_ascii():
    anchor_ascii = r"""
     _
    /|\
   /_|_\
 ____|____
 \_o_o_o_/
~~ |     ~~~~~
___t_________
"""
    print(anchor_ascii)
    return anchor_ascii


def get_anchor_ascii():
    anchor_ascii = r"""
     _
    /|\
   /_|_\
 ____|____
 \_o_o_o_/
~~ |     ~~~~~
___t_________
"""
    return anchor_ascii


def save_to_file(data, anchor_data, action_name, anchor, total_garbage_grams, total_sand_mass_grams):
    file_name = f"C:/sandsresult/{action_name}.txt"
    with open(file_name, 'w') as file:
        file.write(r"""
     _
    /|\
   /_|_\
 ____|____
 \_o_o_o_/
~~ |     ~~~~~
___t_________

 """)
        file.write(f"Action Name: {action_name.center(46, '=')}\n")
        file.write(f"Longitude: {anchor_data['longitude']}\n")
        file.write(f"Latitude: {anchor_data['latitude']}\n")
        file.write(f"Total Garbage Mass: {total_garbage_grams} grams\n")
        file.write(f"Percentage of Garbage to Total Sand Mass: {total_garbage_grams / (total_sand_mass_grams + total_garbage_grams) * 100:.2f}%\n")
        file.write(data)
        file.write(f"\nCollected by Aryan Salmannezhad\n")
        file.write(anchor)
    print(f"Data saved to {file_name}")

def get_grain_info(total_sand_mass_grams):
    alak_sizes = []
    alak_volumes = []
    garbage_mass_per_grain = []  # Store garbage mass for each grain size

    while True:
        size = float(input("Please enter the size of the grain in Mesh NO. : "))
        volume = float(input(f"Please enter the volume of grains in the {size} Mesh NO. grain size in grams: "))
        garbage_mass_grams = float(input("Please enter the mass of garbage in the sand in grams: "))

        total_sand_mass_grams -= garbage_mass_grams

        alak_sizes.append(size)
        alak_volumes.append(volume)
        garbage_mass_per_grain.append(garbage_mass_grams)  # Store the garbage mass for this grain size

        another_alak = input("Do you want to enter data for another grain size? (y / n ): ")
        if another_alak.lower() != 'y':
            break

    total_garbage_grams = sum(garbage_mass_per_grain)  # Calculate total garbage mass

    return alak_sizes, alak_volumes, total_sand_mass_grams, total_garbage_grams, garbage_mass_per_grain


def main():
    action_name = input("Please enter a name for this action: ")
    longitude = float(input("Please enter the longitude for this sand: "))
    latitude = float(input("Please enter the latitude for this sand: "))

    anchor_data = {'longitude': longitude, 'latitude': latitude}

    total_sand_mass_grams = float(input("Please enter the total mass of sand in grams: "))

    alak_sizes, alak_volumes, total_sand_mass_grams, total_garbage_grams, garbage_mass_per_grain = get_grain_info(total_sand_mass_grams)

    total_alak_volume = sum(alak_volumes)
    data_to_save = ""
    data_to_save += "----------------------------------------------------------------------------------------------------------------\n"
    data_to_save += "Summary for Each Grain Size:\n"
    data_to_save += "----------------------------------------------------------------------------------------------------------------\n"

    for i, size in enumerate(alak_sizes):
        # Additional information about grain size
        micron_size = {
            3: 6730,
            4: 4760,
            5: 4000,
            6: 3360,
            7: 2830,
            8: 2380,
            10: 2000,
            12: 1680,
            14: 1410,
            16: 1190,
            18: 1000,
            20: 841,
            25: 707,
            30: 595,
            35: 500,
            40: 400,
            45: 354,
            50: 297,
            60: 250,
            70: 210,
            80: 177,
            100: 149,
            120: 125,
            140: 105,
            170: 88,
            200: 74,
            230: 63,
            270: 53,
            325: 44,
            400: 37
        }.get(size, None)

        mm_size = micron_size / 1000 if micron_size else None

        ratio = alak_volumes[i] / total_alak_volume
        ratios = alak_volumes[i] / total_sand_mass_grams if total_sand_mass_grams else 0
        percentage_of_total_sediment = (alak_volumes[i] / total_alak_volume) * 100
        percentage_of_total_sand = (alak_volumes[i] / total_sand_mass_grams) * 100 if total_sand_mass_grams else 0

        data_to_save += f"Grain Size: {size} Mesh NO. (Micron: {micron_size}, MM: {mm_size})\n"
        data_to_save += f"Sediment Volume: {alak_volumes[i]} grams\n"
        data_to_save += f"Ratio (Sediment/total sand): {ratios:.2f}\n"
        data_to_save += f"Ratio (Sediment this grain/other grains): {ratio:.2f}\n"
        data_to_save += f"Percentage of Total Sediment/other sediments: {percentage_of_total_sediment:.2f}%\n"
        data_to_save += f"Percentage of Total Sediments/sand: {percentage_of_total_sand:.2f}%\n"

        # Add information about garbage mass for each grain size
        data_to_save += f"Mass of Garbage in Sand for {size} Mesh NO. grain: {garbage_mass_per_grain[i]} grams\n"
        data_to_save += "----------------------------------------------------------------------------------------------------------------\n"

    percentage_of_all_sediment = (total_alak_volume / total_alak_volume) * 100
    percentage_of_all_sand = (total_alak_volume / total_sand_mass_grams) * 100 if total_sand_mass_grams else 0

    data_to_save += "\nOverall Summary with Percentages:\n"
    data_to_save += "----------------------------------------------------------------------------------------------------------------\n"
    data_to_save += f"Total Sand Mass: {total_sand_mass_grams} grams\n"
    data_to_save += f"Total Sediment Volume: {total_alak_volume} grams\n"
    data_to_save += f"Percentage of All Sediment: {percentage_of_all_sediment:.2f}%\n"
    data_to_save += f"Percentage of All Sediments to Sand: {percentage_of_all_sand:.2f}%\n"
    data_to_save += "----------------------------------------------------------------------------------------------------------------\n"

    print(data_to_save)  # Displaying the data (you can save it to a file using save_to_file function)

    anchor = get_anchor_ascii()
    save_to_file(data_to_save, anchor_data, action_name, anchor, total_garbage_grams, total_sand_mass_grams)


if __name__ == "__main__":
    main()
