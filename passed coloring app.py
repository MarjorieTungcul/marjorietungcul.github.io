
print("Welcome to 🌈 " + "\033[31mR" + "\033[38;2;255;165;0ma" + "\033[33mi" + "\033[32mn" + "\033[34mb" + "\033[38;2;75;0;130mo" + "\033[38;2;238;130;238mw" + " \033[31mR" + "\033[38;2;255;165;0me" + "\033[33mn" + "\033[32md" + "\033[34me" + "\033[38;2;75;0;130mz" + "\033[38;2;238;130;238mv" + "\033[31mo" + "\033[38;2;255;165;0mu" + "\033[33ms" + " \033[32mA" + "\033[34mp" + "\033[38;2;75;0;130mp" + "\033[38;2;238;130;238m!\033[0m")
print("""Choose an option:
1. \033[31mColoring \033[38;2;255;165;0man \033[33mObject\033[0m
2. \033[32mPrinting \033[34mColored \033[38;2;75;0;130mObjects\033[0m
3. \033[38;2;238;130;238mDeleting \033[31mObjects\033[0m
4. \033[38;2;255;165;0mQuitting \033[33mthe \033[32mApplication\033[0m""")

final_name_objects = []
final_color_objects = ()
paired_dict = {}

while True:
    choice = int(input("Enter your choice (1/2/3/4): "))
    if choice == 1:
        object_name = input("Enter the name of the object you want to color:" )

        final_name_objects += []
        final_name_objects.append(object_name)
       
        roygbiv_colors = ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet")
        check_symbol = "✓"

        color_red = (f"\033[31m{roygbiv_colors[0]}\033[0m")
        color_orange = (f"\033[38;2;255;165;0m{roygbiv_colors[1]}\033[0m")
        color_yellow = (f"\033[33m{roygbiv_colors[2]}\033[0m")
        color_green = (f"\033[32m{roygbiv_colors[3]}\033[0m")
        color_blue = (f"\033[34m{roygbiv_colors[4]}\033[0m")
        color_indigo = (f"\033[38;2;75;0;130m{roygbiv_colors[5]}\033[0m")
        color_violet = (f"\033[38;2;238;130;238m{roygbiv_colors[6]}\033[0m")
        
        print("Choose a color from the 🌈 \033[31mR\033[38;2;255;165;0mO\033[33mY\033[32mG\033[34mB\033[38;2;75;0;130mI\033[38;2;238;130;238mV\033[0m colors:")
        print(f"{check_symbol} {color_red}")
        print(f"{check_symbol} {color_orange}")
        print(f"{check_symbol} {color_yellow}")
        print(f"{check_symbol} {color_green}")
        print(f"{check_symbol} {color_blue}")
        print(f"{check_symbol} {color_indigo}")
        print(f"{check_symbol} {color_violet}")

        while True:
            object_color = input("Enter the color you want to use:")  
            if object_color == roygbiv_colors[0]:
                print(f"{object_name} is now colored {color_red}!")    
                final_color_objects+=(object_color,)          
                break
            elif object_color == roygbiv_colors[1]:  
                print(f"{object_name} is now colored {color_orange}!")   
                final_color_objects+=(object_color,)    
                break
            elif object_color == roygbiv_colors[2]:
                print(f"{object_name} is now colored {color_yellow}!") 
                final_color_objects+=(object_color,)    
                break
            elif object_color == roygbiv_colors[3]:  
                print(f"{object_name} is now colored {color_green}!")
                final_color_objects+=(object_color,)    
                break 
            elif object_color == roygbiv_colors[4]:  
                print(f"{object_name} is now colored {color_blue}!")
                final_color_objects+=(object_color,)    
                break  
            elif object_color == roygbiv_colors[5]:
                print(f"{object_name} is now colored {color_indigo}!")
                final_color_objects+=(object_color,)    
                break 
            elif object_color == roygbiv_colors[6]:  
                print(f"{object_name} is now colored {color_violet}!") 
                final_color_objects+=(object_color,)    
                break
            else:
                print("Invalid color choice. Please select a valid color.")
        
        paired_dict = dict(zip(final_name_objects, final_color_objects))   

    elif choice == 2:
        if not paired_dict:
            print("No objects have been colored yet.")
        else:
            print("Colored Objects:")
            for key, value in paired_dict.items():
                if value == roygbiv_colors[0]:
                    print(f"\033[31m{key}\033[0m is colored {color_red}")
                elif value == roygbiv_colors[1]:
                    print(f"\033[38;2;255;165;0m{key}\033[0m is colored {color_orange}")
                elif value == roygbiv_colors[2]:
                    print(f"\033[33m{key}\033[0m is colored {color_yellow}")
                elif value == roygbiv_colors[3]:
                    print(f"\033[32m{key}\033[0m is colored {color_green}")
                elif value == roygbiv_colors[4]:
                    print(f"\033[34m{key}\033[0m is colored {color_blue}")
                elif value == roygbiv_colors[5]:
                    print(f"\033[38;2;75;0;130m{key}\033[0m is colored {color_indigo}")
                elif value == roygbiv_colors[6]:
                    print(f"\033[38;2;238;130;238m{key}\033[0m is colored {color_violet}")
                else:
                    print("No objects have been colored yet.")
        
    elif choice == 3:
        objects_to_delete = input("Enter the name of the object to delete: ")
        if objects_to_delete in paired_dict:
            deleted_color = paired_dict[objects_to_delete]
            del paired_dict[objects_to_delete]
            if deleted_color == roygbiv_colors[0]:
                print(f"\033[31m{objects_to_delete} \033[0m was deleted from the list of colored objects.")
            elif deleted_color == roygbiv_colors[1]:
                print(f"\033[38;2;255;165;0m{objects_to_delete} \033[0m was deleted from the list of colored objects.")
            elif deleted_color == roygbiv_colors[2]:
                print(f"\033[33m{objects_to_delete} \033[0m was deleted from the list of colored objects.")
            elif deleted_color == roygbiv_colors[3]:
                 print(f"\033[32m{objects_to_delete} \033[0m was deleted from the list of colored objects.")
            elif deleted_color == roygbiv_colors[4]:
                 print(f"\033[34m{objects_to_delete} \033[0m was deleted from the list of colored objects.")
            elif deleted_color == roygbiv_colors[5]:
                 print(f"\033[38;2;75;0;130m{objects_to_delete} \033[0m was deleted from the list of colored objects.")
            elif deleted_color == roygbiv_colors[6]:
                 print(f"\033[38;2;238;130;238m{objects_to_delete} \033[0m was deleted from the list of colored objects.")
            else:
                print(f"{objects_to_delete} was deleted from the list of colored objects.")          
        else:
            print(f"{objects_to_delete} was not found in the list of colored objects.")
    elif choice == 4:
        print("Thank you for using 🌈 " + "\033[31mR" + "\033[38;2;255;165;0ma" + "\033[33mi" + "\033[32mn" + "\033[34mb" + "\033[38;2;75;0;130mo" + "\033[38;2;238;130;238mw" + " \033[31mR" + "\033[38;2;255;165;0me" + "\033[33mn" + "\033[32md" + "\033[34me" + "\033[38;2;75;0;130mz" + "\033[38;2;238;130;238mv" + "\033[31mo" + "\033[38;2;255;165;0mu" + "\033[33ms" + " \033[32mA" + "\033[34mp" + "\033[38;2;75;0;130mp\033[0m." + "Goodbye!")
        break
    else:
        print("Invalid number choice. Please enter a valid number.")
    
    print("🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈")
      
    print("""Choose an option:
1. \033[31mColoring \033[38;2;255;165;0man \033[33mObject\033[0m
2. \033[32mPrinting \033[34mColored \033[38;2;75;0;130mObjects\033[0m
3. \033[38;2;238;130;238mDeleting \033[31mObjects\033[0m
4. \033[38;2;255;165;0mQuitting \033[33mthe \033[32mApplication\033[0m""")
    
   