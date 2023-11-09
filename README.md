# Admin

### Documentation for all Functions

1. **ADD(payments: dict, nr: int, val: dict, changes: list)**
   - Description: The `ADD` function updates a payment dictionary and records the type of operation ('MOD' or 'ADD').
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `nr` (int): The number of the apartment to be modified.
     - `val` (dict): The value to be introduced or modified.
     - `changes` (list): A list where changes are recorded.
   - Returns: Nothing

2. **DEL(payments: dict, nr: int, changes: list)**
   - Description: The `DEL` function deletes a payment dictionary and records the type of operation.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `nr` (int): The number of the apartment to be modified.
     - `changes` (list): A list where changes are recorded.
   - Returns: Nothing

3. **mass_del(start: int, end: int)**
   - Description: The `mass_del` function deletes payments between the indexes `start` and `end` and records the type of operation.
   - Arguments:
     - `start` (int): The starting index of apartments to be deleted.
     - `end` (int): The ending index of apartments to be deleted.
   - Returns: Nothing

4. **mass_undo(rec: int)**
   - Description: The `mass_undo` function iteratively undoes changes in a payment dictionary based on a specified number of records (`rec`).
   - Arguments:
     - `rec` (int): The number of undos to be made.
   - Returns: Nothing

5. **inDEL(payments: dict, nr: int)**
   - Description: The `inDEL` function deletes a payment dictionary.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `nr` (int): The number of the apartment to be modified.
   - Returns: Nothing

6. **inADD(payments: dict, nr: int, val: dict)**
   - Description: The `inADD` function updates a payment dictionary.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `nr` (int): The number of the apartment to be modified.
     - `val` (dict): The value to be introduced or modified.
   - Returns: Nothing

7. **UNDO(payments: dict, changes: list)**
   - Description: The `UNDO` function reverses the most recent payment operation recorded in the `changes` list and updates the `payments` dictionary accordingly.
   - Arguments:
     - `payments` (dict): A dictionary of all payments.
     - `changes` (list): A list where changes are recorded.
   - Returns: Nothing

8. **mass_mod(start,end,key,value)**
   - Description: The `mass_mod` function iteratively modifies payment information within a specified range and records a 'mMOD' operation in the `changes` list to indicate the mass modification.
   - Arguments:
     - `start` (int): The starting index of apartments to be modified.
     - `end` (int): The ending index of apartments to be modified.
     - `key` (str): The key to be modified.
     - `value` (float): The new value of the key to be modified.
   - Returns: Nothing

9. **get_gas_value(entry)**
   - Description: The `get_gas_value` function retrieves the gas value for a specific payment record number from the payments dictionary.
   - Arguments:
      - `entry` (dict): An apartment entity
   - Returns: The gas value.

10. **get_water_value(entry)**
    - Description: The `get_water_value` function retrieves the water value for a specific payment record number from the payments dictionary.
    - Arguments:
      - `entry` (dict): An apartment entity
    - Returns: The water value.

11. **get_heat_value(entry)**
    - Description: The `get_heat_value` function retrieves the heat value for a specific payment record number from the payments dictionary.
    - Arguments:
      - `entry` (dict): An apartment entity
    - Returns: The heat value.

12. **get_sewage_value(entry)**
    - Description: The `get_sewage_value` function retrieves the sewage value for a specific payment record number from the payments dictionary.
    - Arguments:
      - `entry` (dict): An apartment entity
    - Returns: The sewage value.

13. **get_misc_value(entry)**
    - Description: The `get_misc_value` function retrieves the misc value for a specific payment record number from the payments dictionary.
    - Arguments:
      - `entry` (dict): An apartment entity
    - Returns: The misc value.

14. **get_date_value_str(entry)**
    - Description: The `get_date_value_str` function retrieves the date value as a string for a specific payment record number from the payments dictionary.
    - Arguments:
      - `entry` (dict): An apartment entity
    - Returns: The date value as a formatted string.

15. **get_date_value(entry)**
    - Description: The `get_date_value` function retrieves the date value as a string for a specific payment record number from the payments dictionary.
    - Arguments:
      - `entry` (dict): An apartment entity
    - Returns: The date value as a formatted string.

16. **get_total_value(nr, payments)**
    - Description: The `get_total_value` function calculates the total for a specific payment record number from the payments dictionary.
    - Arguments:
      - `entry` (dict): An apartment entity
    - Returns: The total value.

17. **key_selector()**
    - Description: The `key_selector` function prompts the user to select a key (e.g., 'gas', 'water', 'heat', 'sewage', 'misc') and returns the selected key based on the user's input.
    - Arguments: None
    - Returns: The selected key as a string based on the user's input.

18. **read_float(msg: str)**
    - Description: The `read_float` function prompts the user to input a float value and handles any input errors.
    - Arguments:
      - `msg` (str): The message to display as a prompt to the user.
    - Returns: A float value entered by the user.

19. **read_int(msg: str)**
    - Description: The `read_int` function prompts the user to input an int value and handles any input errors.
    - Arguments:
      - `msg` (str): The message to display as a prompt to the user.
    - Returns: An int value entered by the user.

20. **read_date()**
    - Description: The `read_date` function prompts the user to input a date or autocompletes with today's date and handles any input errors.
    - Arguments: None
    - Returns: A date entered by the user.

21. **input_payment()**
    - Description: The `input_payment` function allows the user to input payment information and updates the 'payments' dictionary.
    - Arguments: None
    - Returns: Nothing

22. **print_ap(nr)**
    - Description: The `print_ap` function prints all the payments from an apartment.
    - Arguments:
      - `nr` (int): The number of the apartment to retrieve values from.
    - Returns: Nothing

23. **print_grt(value)**
    - Description: The `print_grt` function prints all the apartments with payments greater than a value.
    - Arguments:
      - `value` (float): The value for comparison.
    - Returns: Nothing

24. **print_date_value(date,value)**
    - Description: print_date_value function prints all the apartments with payments before a certain date and with total over a certain value.
    - Arguments:
      - `value` (float):value for comparison
      - `date` (date):date for comparison
    - Returns: Nothing

25. **print_all_key(key)**
    - Description: The `print_all_key` function displays payment information for a specific key (e.g., 'gas', 'water', 'heat') from all apartments.
    - Arguments:
      - `key` (str): The payment category to be displayed (e.g., 'gas', 'water', 'heat').
    - Returns: Nothing

26. **total_by_key(key)**
    - Description: The `total_by_key` function displays the total sum for a specific key (e.g., 'gas', 'water', 'heat') for all apartments.
    - Arguments:
      - `key` (str): The payment category to be displayed (e.g., 'gas', 'water', 'heat').
    - Returns: Nothing

27. **del_under_value(value)**
    - The del_under_value function iteratively modifies payment information under a certain value and records a 'mMOD' operation in the changes list to indicate the mass modification.
    - Arguments:
      - `value` (float): The value for comparison.
    - Returns: Nothing

28. **pak()**
    - Description: The `pak` function asks the user to press a key in order to proceed.
    - Arguments: None
    - Returns: None

29. **del_app()**
    - Description: The `del_app` function passes the command to delete a certain apartment to services.
    - Arguments: None
    - Returns: None

30. **del_app_sf()**
    - Description: The `del_app_sf` function passes the command to delete a apartments in range to services.
    - Arguments: None
    - Returns: None
  
31. **del_key_sf()**
    - Description: The `del_key_sf` function passes the command to delete a payment type from all apartments to services.
    - Arguments: None
    - Returns: None
  
32. **total_app()**
    - Description: The `total_app` function prints the total for a certain apartment.
    - Arguments: None
    - Returns: None

33. **print_without_key(key)**
    - Description: The `print_without_key` function prints the total for a certain apartment.
    - Arguments:
      - `key` (string): Payment type to be removed.
    - Returns: None

34. **print_over_value(value)**
    - Description: The `print_over_value` function prints all the payment types from all the apartments over a certain value.
    - Arguments:
      - `value` (float): value for comparison 
    - Returns: None

35. **clear(KEY)**
    - Description: The `clear` function removes every apartment and every changes in history
    - Arguments:
      - `KEY` (int): generated verification key for safety purposes
    - Returns: None

36. **retrieve_payments()**
    - Description: The `retrieve_payments` function returns a copy of all the payments
    - Arguments:None
    - Returns: A copy of the payment dictionary

37. **retrieve_changes()**
    - Description: The `retrieve_changes` function returns a copy of history
    - Arguments:None
    - Returns: A copy of the history list

38. **validate_entry(entry)**
    - Description: The `validate_entry` function returns a copy of history
    - Arguments:
      - `entry` (dict): An apartment entity
    - Returns: Nothing
    - Raises: ValueError if the `entry` is not valid 

39. **payment_creator(gas,water,heat,sewage,misc,date)**
    - Description: The `retrieve_changes` function returns a copy of history
    - Arguments:
      - `gas` (float): Gas value
      - `water`: Water value
      - `heat` (float): Heat value
      - `sewage` (float): Sewage value
      - `misc` (float): Misc value
      - `date` (date): Date value
    - Returns: Apartment entity

40. **add_payment(nr,entry)**
    - Description: The `add_payment` function sends an apartment entity and a number to be added into the payments or modified
    - Arguments:
      - `nr` (int): Number where the apartment should be added or modifies
      - `entry` (dict): An apartment entity
    - Returns: Nothing

41. **del_payment(nr,entry)**
    - Description: The `del_payment` function sends an apartment number to be deleted from payments or excepts indexError if number is not existent
    - Arguments:
      - `nr` (int): Number of the apartment that should be deleted
    - Returns: Nothing

42. **undo_service()**
    - Description: The `undo_service` function sends an apartment number to be deleted from payments or excepts indexError if number is not existent
    - Arguments: None
    - Returns: Nothing

43. **check_key(sKEY)**
    - Description: The `check_key` function compares the sent KEY to the security key
    - Arguments:
      -`sKEY` (int): sent security key
    - Returns: (security key==`sKEY`)

44. **auto_testing()**
    - Description: The `auto_testing` function is a magical function that makes sure everything works.
    - Arguments: None
    - Returns: Nothing
    - Raises assertionError if you wrote spaghetti code

### Running scenario

| User                 	| Program                                         	| Description                                             	|
|----------------------	|-------------------------------------------------	|---------------------------------------------------------	|
|                      	| Displays menu                                   	| Awaits an input from the user                           	|
| 1                    	|                                                 	| Awaits apartment number                                 	|
| 101 and payment data 	| Awaits payment details                          	| Awaits payment details for Apartment 101 from the user  	|
| 1                    	|                                                 	| Awaits apartment number                                 	|
| 102 and payment data 	| Awaits payment details                          	| Awaits payment details for Apartment 102 from the user  	|
| 1                    	|                                                 	| Awaits apartment number                                 	|
| 103 and payment data 	| Awaits payment details                          	| Awaits payment details for Apartment 103 from the user  	|
| 2                    	| Displays submenu                                	| Awaits choice from user                                 	|
| 2                    	| Awayits start and end positions for delet       	| Asks user for the indexes from where to delete the data 	|
| 102 103              	| Deletes entries from 102 to 103                 	| The only entry remaining is 101                         	|
| 4                    	| Display menu                                    	| User exited submenu                                     	|
| 4                    	| Displays submenu                                	| Awaits choice from user                                 	|
| 3                    	| Enter apartment number:                         	| Asks user for an apartment to calculate the total for   	|
| 101                  	| Displays total value of the payments for ap 101 	|                                                         	|
| 4                    	| Display menu                                    	| User exited submenu                                     	|
| 7                    	| Exits                                           	| User exited the program                                 	|
